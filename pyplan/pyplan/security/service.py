import datetime
import json
import os
import platform
import subprocess
import uuid
from shlex import split
from time import sleep

import requests
from django.conf import settings
from django.utils import timezone
from rest_framework.authtoken.models import Token

from pyplan.pyplan.app_pool.models import AppPool
from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.calcEngine import CalcEngine
from pyplan.pyplan.common.logger import PyplanLogger
from pyplan.pyplan.common.redisService import RedisService
from pyplan.pyplan.external_link.models import ExternalLink
from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo
from pyplan.pyplan.modelmanager.service import ModelManagerService
from pyplan.pyplan.usercompanies.models import UserCompany

from .classes.clientSession import ClientSession
from .functions import _getAllSessions
from .serializers import ClientSessionSerializer


class SecurityService(BaseService):

    def createSession(self, companyId):
        """Create new client session
        """
        session_store = self.session_store()

        if self.current_user.usercompanies.count() > 0:

            # TODO: if desktop_mode ?
            current_session = self.getMyFirstSession()
            if not current_session is None:
                client_session = current_session
            else:
                client_session = ClientSession()
                client_session.userId = self.current_user.id
                client_session.userFullName = f"{self.current_user.first_name} {self.current_user.last_name}"
                client_session.userIsSuperUser = self.current_user.is_superuser
                login_action = dict()
                found = False
                for userCompany in self.current_user.usercompanies.all().iterator():
                    if userCompany.active and (userCompany.company.id == companyId or companyId == -1):
                        client_session.companyId = userCompany.company.id
                        client_session.company_code = userCompany.company.code
                        client_session.companyName = userCompany.company.name
                        client_session.userCompanyId = userCompany.id

                        # get login action in user departaments
                        for department in userCompany.departments.all().iterator():
                            client_session.departments.append(department.code)
                            if not department.login_action is None:
                                for key in department.login_action:
                                    login_action[key] = department.login_action[key]

                        found = True
                        break

                client_session.loginAction = login_action
                if not found:
                    # TODO: ver como disparar error
                    raise ValueError("The user has no active companies")

                client_session.process = self.current_user.get_user_permissions()

                # TODO: validate licence
                # TODO: load company/user preferences

                serializer = ClientSessionSerializer(client_session)
                session_store["data"] = serializer.data
                session_store["openAt"] = timezone.now().isoformat()
                session_store["lastUpdate"] = timezone.now().isoformat()
                session_store["status"] = ""
                session_store.create()
                client_session.session_key = session_store.session_key
                self.client_session = client_session
                # TODO: if desktop_mode ?
                self.saveSession(60*60*24*365*10)  # expire in 10 years

                # TODO: autoload model
                if client_session.loginAction and "open_model" in client_session.loginAction and client_session.loginAction["open_model"]:
                    open_model = client_session.loginAction["open_model"]
                    model_service = ModelManagerService(base_service=self)
                    client_session.modelInfo = model_service.openModel(
                        open_model)
                    client_session.autoopenUri = open_model
                    if client_session.modelInfo.new_session_key:
                        client_session.session_key = client_session.modelInfo.new_session_key

            return client_session

    def logout(self):
        """Perform logout of the current session
        """
        if self.checkModelOpen():
            calcEngine = CalcEngine.factory(self.client_session)
            calcEngine.releaseEngine()
        self.removeSession()

    def getAllSessions(self, onlyMySessions=False, company_id=None):
        """Return all sessions
        """
        # TODO: add security
        return _getAllSessions(self, onlyMySessions, company_id)

    def killSessionByKey(self, session_key):
        """Kill the session by param session_key
        """
        if self.existSession(session_key):
            cs = self.getSessionByKey(session_key)
            if not cs is None:
                if cs.userId != self.client_session.userId:
                    self.ensurePermision("pyplan.kill_sessions")

                s = self.session_store(session_key=session_key)
                if s:
                    self._releaseEngineForThisSession(s)
                    s.delete()
                    return True
        elif str(session_key).isnumeric():
            self.ensurePermision("pyplan.kill_sessions")
            app_pool = AppPool.objects.get(pk=session_key)
            app_pool.delete()
            return True

        return False

    def createNewSession(self):
        """Create new session using current credentials
        """
        companyId = self.getSession().companyId
        return self.createSession(companyId)

    def purgeSessions(self):
        """Called internaly. Mark sessions in user and purge expired sessions
        """
        now = timezone.now()
        redis = RedisService()
        in_use = redis.sessions_in_use()

        for session in self.session_store.get_model_class().objects.all():
            try:
                # TODO: check with redis
                if session.session_key in in_use:
                    s = self.session_store(session_key=session.session_key)
                    s["lastUpdate"] = timezone.now().isoformat()
                    if "isGuest" in s and s["isGuest"]:
                        s.set_expiry(int(settings.GUEST_SESSION_TIMEOUT))
                    else:
                        s.set_expiry(int(settings.SESSION_COOKIE_AGE))
                    s.save()
                elif session.expire_date < now:
                    self._releaseEngineForThisSession(session)
            except Exception as ex:
                print(f"Error deleting session {session.session_key}:")
                print(str(ex))
        self.session_store.clear_expired()

    def getSessionFromExternalLink(self, external_link: ExternalLink):
        # 1. get or creates and sets current_session and token
        session, token, is_new = self._getOrCreateGuestSession(
            external_link.owner, external_link)

        # 2. opens model and sets modelInfo of current_session
        if is_new:
            self._openModel(external_link.model_path)

        return session, token

    def useExternalLink(self, guid):
        external_link = ExternalLink.objects.get(pk=guid)

        # 1. get or creates and sets current_session and token
        session, token, is_new = self._getOrCreateGuestSession(
            external_link.owner, external_link)

        # 2. opens model and sets modelInfo of current_session
        if is_new:
            self._openModel(external_link.model_path)

        extra_data = None
        entity_id = None
        entity_type = None
        if hasattr(external_link, "dashboard_external_link"):
            entity_id = external_link.dashboard_external_link.dashboard.id
            entity_type = "dashboard"
        elif hasattr(external_link, "report_external_link"):
            entity_id = external_link.report_external_link.report.id
            extra_data = external_link.report_external_link.report.dashboards.values_list(
                'id', flat=True).order_by("order")
            entity_type = "report"
        elif hasattr(external_link, "node_external_link"):
            entity_id = external_link.node_external_link.node_id
            entity_type = "node"

        return session, token, entity_id, entity_type, extra_data

    # Private

    def _openModel(self, file, reuse_instance=False):
        """
        Opens model and sets modelInfo of current_session
        """
        res = ModelInfo()
        calcEngine = CalcEngine.tryLoadFromAppPool(self.client_session, file)

        res.name = calcEngine.getModelName()
        res.uri = file
        res.daysToExpire = 30
        res.modelId = calcEngine.getModelId()
        res.engineUID = calcEngine.getEngineUID()
        res.engineURI = calcEngine.getEngineURI()
        res.engineParams = calcEngine.getEngineParams()
        res.readonly = True

        current_session = self.getSession()
        current_session.modelInfo = res
        self.saveSession()

        return res

    def _setClientSession(self, usercomp: UserCompany, session_store, external_link: ExternalLink):
        client_session = ClientSession()
        client_session.userId = usercomp.user.id
        client_session.userFullName = usercomp.user.first_name
        client_session.companyId = usercomp.company.id
        client_session.company_code = usercomp.company.code
        client_session.companyName = usercomp.company.name
        client_session.userCompanyId = usercomp.id
        client_session.process = usercomp.user.get_user_permissions()

        serializer = ClientSessionSerializer(client_session)
        session_store["data"] = serializer.data
        session_store["openAt"] = timezone.now().isoformat()
        session_store["lastUpdate"] = timezone.now().isoformat()
        session_store["status"] = ""
        session_store["isGuest"] = True
        if external_link.common_instance:
            session_store["isCommonInstance"] = True
        session_store.create()

        client_session.session_key = session_store.session_key
        return client_session

    def _getOrCreateGuestSession(self, usercompany: UserCompany, external_link: ExternalLink):
        """
        Gets or Creates new user session
        """
        is_new = True

        session_store = self.session_store()
        client_session = None

        guest_usercomp = UserCompany.objects.filter(
            company_id=usercompany.company_id, user__username=f'{usercompany.company.code}-guest').first()

        if external_link.common_instance:
            all_sessions = self.getAllSessions(
                company_id=guest_usercomp.company.id)
            for session in all_sessions:
                if session.isGuest and session.isCommonInstance and session.currentModelFile == external_link.model_path:
                    client_session = self.getSessionByKey(session.session_key)
                    is_new = False
                    break

        if not client_session:
            client_session = self._setClientSession(
                guest_usercomp, session_store, external_link)

            self.client_session = client_session
            self.saveSession()

        token, created = Token.objects.get_or_create(user=guest_usercomp.user)
        return client_session, token, is_new

    def _releaseEngineForThisSession(self, session):
        _decoded = session
        # support session store and session obj
        try:
            _decoded = session.get_decoded()
        except Exception as ex:
            pass
        if _decoded:
            # remove session
            if "data" in _decoded:
                print(f"Deleting session: {session.session_key}")
                # parse session out of baseService for don't activate session
                _data = _decoded["data"]

                ser = ClientSessionSerializer(data=_data)
                ser.is_valid(raise_exception=True)
                cs = ser.save()
                if cs and cs.modelInfo and cs.modelInfo.engineUID:
                    calcEngine = CalcEngine.factory(cs)
                    calcEngine.releaseEngine()
                    print('Engine released')
                PyplanLogger().logEndSession(None, ser.create(ser.validated_data))
        else:
            print(f"Session: {session.session_key} without decoded")

    def getSystemResources(self, session_key):

        def _read_int(file):
            data = 0
            with open(file, 'r') as f:
                data = int(f.read())
                f.close()
            return data

        def _read_cache():
            data = 0
            with open('/sys/fs/cgroup/memory/memory.stat', 'r') as f:
                line = f.readline()
                data = int(str(line).split(" ")[1])
                f.close()
            return data

        def read_disk_space():
            res = dict(size="-", used="-", percent="-")
            model_path = os.path.join(settings.MEDIA_ROOT, "models")
            cmd = f"df -h {model_path} --output=size,used,pcent"
            popen = subprocess.Popen(
                split(cmd), stdout=subprocess.PIPE, universal_newlines=True)
            data = []
            for stdout_line in iter(popen.stdout.readline, ''):
                data.append(stdout_line)

            if len(data) > 0:
                arr = str(data[1]).split(" ")
                full_arr = [xx for xx in arr if xx != ""]
                if len(full_arr) == 3:
                    res["size"] = full_arr[0]
                    res["used"] = full_arr[1]
                    res["percent"] = full_arr[2]

            return res

        mem_limit = _read_int(
            '/sys/fs/cgroup/memory/memory.limit_in_bytes') / 1024/1024/1024
        if mem_limit > 200:  # bug for container whitout limit
            total_host = ""
            with open('/proc/meminfo', 'r') as f:
                line1 = f.readline()
                total_host = str(line1).split(" ")[-2:-1][0]
                mem_limit = int(total_host) / 1024/1024

        mem_used = (_read_int(
            '/sys/fs/cgroup/memory/memory.usage_in_bytes') - _read_cache()) / 1024/1024/1024

        # get cpu usage
        time_1 = datetime.datetime.now()
        cpu_time_1 = _read_int('/sys/fs/cgroup/cpu/cpuacct.usage')
        sleep(0.3)
        time_2 = datetime.datetime.now()
        cpu_time_2 = _read_int('/sys/fs/cgroup/cpu/cpuacct.usage')

        delta_time = (time_2 - time_1).microseconds * 10
        used_cpu = (cpu_time_2 - cpu_time_1) / delta_time
        used_cpu = used_cpu if used_cpu < 100 else 100

        res = {
            "totalMemory": mem_limit,
            "usedMemory": mem_used,
            "usedCPU": used_cpu,
            "disk": read_disk_space()
        }

        if session_key:
            if self.existSession(session_key):
                client_session = self.getSessionByKey(session_key)
                if client_session and client_session.modelInfo and client_session.modelInfo.engineUID:
                    calcEngine = CalcEngine.factory(client_session)
                    res["session"] = calcEngine.getSystemResources()
                    calcEngine = None

        return res

    def setStatistics(self, appVersion):
        try:
            if self.client_session and self.client_session.userId:
                ping_url = 'https://ping.pyplan.com/pings/'
                home_path = os.path.expanduser('~')
                payload = {
                    'id': str(uuid.uuid4()),
                    'uuid': str(self.client_session.userId),
                    'homePath': home_path,
                    'platform': platform.system(),
                    'appVersion': appVersion,
                }
                requests.post(url=ping_url, json=payload)
        except Exception as ex:
            print(ex)
