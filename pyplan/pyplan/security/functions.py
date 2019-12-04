from django.conf import settings
from pyplan.pyplan.common.baseService import BaseService
from .classes.activeSession import ActiveSession
from pyplan.pyplan.app_pool.models import AppPool
from pyplan.pyplan.common.redisService import RedisService

from django.utils import timezone
import datetime
import math


def _getAllSessions(service: BaseService, onlyMySessions=False, company_id=None):
    """Return all sessions
    """

    redis = RedisService()
    result = []
    now = timezone.now()
    for session in service.session_store.get_model_class().objects.all().order_by('session_key'):
        item = ActiveSession()
        _decoded = session.get_decoded()
        item.session_key = session.session_key

        if _decoded and "data" in _decoded:
            if not company_id is None and _decoded["data"]["companyId"] == company_id  \
                    or not service.current_user is None and service.current_user.has_perm("pyplan.list_sessions") \
                    or not service.current_user is None and service.current_user.has_perm("pyplan.list_company_sessions") \
                    and not not service.client_session is None and service.client_session.companyId == _decoded["data"]["companyId"]  \
                    or not service.client_session is None and service.client_session.userId == _decoded["data"]["userId"]:

                if onlyMySessions and _decoded["data"]["userId"] != str(service.client_session.userId):
                    continue

                item.userName = _decoded["data"]["userFullName"]
                item.currentModel = _decoded["data"]["modelInfo"]["modelId"]
                item.currentModelFile = _decoded["data"]["modelInfo"]["uri"]
                item.currentModelName = _decoded["data"]["modelInfo"]["name"]
                item.readonly = _decoded["data"]["modelInfo"]["readonly"]
                item.status = "processing" if redis.is_active_session(item.session_key) else ""

                item.isGuest = "isGuest" in _decoded
                item.isCommonInstance = "isCommonInstance" in _decoded

                if "openAt" in _decoded:
                    openAt = datetime.datetime.fromisoformat(_decoded["openAt"])
                    item.openAgo = (now-openAt).total_seconds()/60
                if "lastUpdate" in _decoded:
                    time_timeout = settings.SESSION_COOKIE_AGE
                    if item.isGuest:
                        time_timeout = settings.GUEST_SESSION_TIMEOUT
                    if item.status == "processing":
                        item.activeAgo = 0
                        item.timeoutIn = int(math.ceil(time_timeout/60))
                    else:
                        lastUpdate = datetime.datetime.fromisoformat(_decoded["lastUpdate"])
                        item.activeAgo = (now-lastUpdate).total_seconds()/60
                        if time_timeout:
                            _timeOutAt = lastUpdate + \
                                datetime.timedelta(seconds=int(time_timeout))
                            item.timeoutIn = int(max(math.ceil((_timeOutAt - now).total_seconds()/60), 0))

                result.append(item)

    # add app pool sessions
    if not onlyMySessions:
        current_company_id = company_id if not company_id is None else service.client_session.companyId
        for app_pool in AppPool.objects.filter(company_id=current_company_id):

            if not company_id is None and app_pool.company_id == company_id  \
                    or service.current_user.has_perm("pyplan.list_sessions") \
                    or service.current_user.has_perm("pyplan.list_company_sessions") \
                    and app_pool.company_id == service.client_session.companyId:

                modelinfo = app_pool.modelinfo
                item = ActiveSession()
                item.session_key = app_pool.id
                item.openAgo = (now-app_pool.created_at).total_seconds()/60

                if app_pool.usercompany is None:
                    item.userName = "for everyone"
                else:
                    item.userName = f"for {app_pool.usercompany.user.first_name} {app_pool.usercompany.user.last_name}"

                item.currentModel = modelinfo["modelId"]
                item.currentModelFile = modelinfo["uri"]
                item.currentModelName = modelinfo["name"]
                item.isPool = True
                item.readonly = True
                result.append(item)

    return result
