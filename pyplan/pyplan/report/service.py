import json
import os
import uuid
from datetime import datetime
from numbers import Number

import requests
from django.conf import settings
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.utils import _zipFiles
from pyplan.pyplan.dashboard.models import Dashboard
from pyplan.pyplan.dashboardstyle.models import DashboardStyle
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import Report
from .serializers import ExportItemsSerializer


class ReportManagerService(BaseService):

    def getReport(self, report_id):
        return Report.objects.get(pk=report_id)

    def myReports(self, parent_id=None, favs=None):
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        reports = Report.objects.filter(
            model=model_id,
        )

        if type(favs) is bool and favs:
            reports = reports.filter(
                owner_id=usercompany_id,
                is_fav=True
            )
        else:
            if parent_id and parent_id.isnumeric():
                reports = reports.filter(
                    parent__pk=int(parent_id),
                )
            else:
                reports = reports.filter(
                    owner_id=usercompany_id,
                    parent__pk__isnull=True,
                )

        return reports.order_by('order').distinct()

    def sharedWithMe(self, parent):
        company_id = self.client_session.companyId
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        reports = Report.objects.filter(
            # shared to specific users, me included
            Q(usercompanies__pk=usercompany_id) |
            # shared to departments where I belong
            Q(departments__usercompanies__pk=usercompany_id) |
            # public but not mine
            (Q(is_public=True) & ~Q(owner_id=usercompany_id)),
            # from the same company
            owner__company__pk=company_id,
            model=model_id,
        )
        if parent and isinstance(parent, int):
            reports = reports.filter(
                parent__pk=int(parent),
            )
        else:
            reports = reports.filter(
                parent__pk__isnull=True,
            )
        return reports.order_by('order').distinct()

    def mySharedReports(self, parent):
        reports = Report.objects.filter(
            Q(departments__isnull=False) | Q(usercompanies__isnull=False) | Q(is_public=True),
            owner__pk=self.client_session.userCompanyId,
            model=self.client_session.modelInfo.modelId
        )
        return reports.order_by('order').distinct()

    def createReport(self, data):
        user_company = UserCompany(id=self.client_session.userCompanyId)
        parent = None
        if "parentId" in data and not data["parentId"] is None:
            parent = Report(id=data["parentId"])

        report = Report.objects.create(
            model=self.client_session.modelInfo.modelId,
            name=data["name"],
            is_fav=data["is_fav"],
            is_public=data["is_public"],
            parent=parent,
            owner=user_company,
        )
        return report

    def updateReport(self, pk, data):
        report = Report.objects.get(pk=pk)
        if report:
            if "name" in data:
                report.name = data["name"]
            report.is_fav = data["is_fav"]
            report.is_public = data["is_public"]
            if "parentId" in data and not data["parentId"] is None:
                report.parent = Report(id=data["parentId"])
            report.save()
        return report

    def getNavigator(self, report_id, dashboard_id):
        result = {
            "priorId": None,
            "priorName": None,
            "nextId": None,
            "nextName": None,
            "list": [],
        }

        report = None
        dashboards = []

        if report_id:
            report = Report.objects.get(pk=report_id) if report_id.isnumeric(
            ) else Report.objects.get(uuid=report_id)
            dashboards = report.dashboards.all()
            dash_count = report.dashboards.count()
            # only next, on click dashboard id will come and sort
            if dash_count > 0:
                next_dashboard = dashboards[1]
                result["nextId"] = next_dashboard['id']
                result["nextName"] = next_dashboard['name']

        if dashboard_id:
            dashboard = Dashboard.objects.get(pk=dashboard_id) if dashboard_id.isnumeric(
            ) else Dashboard.objects.get(uuid=dashboard_id)
            report = report if report_id else dashboard.report
            if report:
                dashboards = report.dashboards
                previous = Dashboard.objects.filter(
                    report=report, order=dashboard.order-1).all()
                if previous.count() > 0:
                    result["priorId"] = previous[0].id
                    result["priorName"] = previous[0].name
                following = Dashboard.objects.filter(
                    report=report, order=dashboard.order+1).all()
                if following.count() > 0:
                    result["nextId"] = following[0].id
                    result["nextName"] = following[0].name
            else:
                dashboards.append(dashboard)

        result['list'] = dashboards
        return result

    def bulkDelete(self, ids):
        return Report.objects.filter(pk__in=ids).delete()

    def changeOrder(self, ids):
        for index, val in enumerate(ids):
            if val.isnumeric():
                report = Report.objects.get(pk=int(val))
                report.order = index + 1
                report.save()

    def search(self, text):
        reports = Report.objects.filter(name__icontains=text)
        dashboards = Dashboard.objects.filter(name__icontains=text)
        return {"reports": reports, "dashboards": dashboards}

    def duplicateItems(self, data):
        for report_id in data["report_ids"]:
            report = Report.objects.get(pk=report_id)
            self._duplicateReport(report, True)

        for dashboard_id in data["dashboard_ids"]:
            dashboard = Dashboard.objects.get(pk=dashboard_id)

            self._duplicateDashboard(dashboard, True)

    def copyToMyReports(self, data):
        owner_id = self.client_session.userCompanyId
        for report_id in data["report_ids"]:
            report = Report.objects.get(pk=report_id)
            self._copyReport(report, owner_id)

        for dashboard_id in data["dashboard_ids"]:
            dashboard = Dashboard.objects.get(pk=dashboard_id)

            self._copyDashboard(dashboard, owner_id)

    def setAsFav(self, data):
        reports = Report.objects.filter(pk__in=data["report_ids"])
        reports.update(is_fav=data["is_fav"])
        dashboards = Dashboard.objects.filter(pk__in=data["dashboard_ids"])
        dashboards.update(is_fav=data["is_fav"])
        return {"reports": reports, "dashboards": dashboards}

    def dropOnReport(self, report_ids, dashboard_ids, report_id=None):
        reports = Report.objects.filter(pk__in=report_ids)
        reports.update(parent_id=report_id)

        dashboards_childrens = None
        order = 0

        if report_id:
            parent_report = Report.objects.get(pk=report_id)
            dashboards_childrens = parent_report.dashboards.all()
            order = dashboards_childrens.latest(
                'order').order if dashboards_childrens else order

        else:
            dashboards_childrens = Dashboard.objects.filter(
                report_id__isnull=True)
            order = dashboards_childrens.latest(
                'order').order if dashboards_childrens else order

        for dash_id in dashboard_ids:
            dash = Dashboard.objects.get(pk=dash_id)
            dash.report_id = report_id
            dash.order = order+1
            dash.save()
            order += 1

        dashboards = Dashboard.objects.filter(pk__in=dashboard_ids)

        return {"reports": reports, "dashboards": dashboards}

    def exportItems(self, data):
        reports = Report.objects.filter(pk__in=data['report_ids'])
        dashboards = Dashboard.objects.filter(pk__in=data['dashboard_ids'])
        styles = []
        styles.extend(DashboardStyle.objects.filter(
            dashboards__id__in=data['dashboard_ids']).all())
        self._getStyles(reports, styles)

        return {
            'dashboards': dashboards,
            'reports': reports,
            'styles': list(set(styles)),
        }, f"dashboards-{datetime.today().strftime('%Y%m%d-%H%M%S')}"

    def exportItemsAndPublish(self, data):

        response = None

        # We create the json file to be imported inside the model folder
        reports = Report.objects.filter(pk__in=data['report_ids'])
        dashboards = Dashboard.objects.filter(pk__in=data['dashboard_ids'])
        styles = []
        styles.extend(DashboardStyle.objects.filter(
            dashboards__id__in=data['dashboard_ids']).all())
        self._getStyles(reports, styles)
        to_save = {
            'dashboards': dashboards,
            'reports': reports,
            'styles': list(set(styles)),
        }
        to_save_serialized = json.dumps(ExportItemsSerializer(
            to_save).data, indent=None)
        storage = FileSystemStorage(
            os.path.join(settings.MEDIA_ROOT, 'models'))
        file_path = os.path.join(
            storage.base_location, os.path.normpath(data['model_folder']), 'itemsToPublish.json')

        # we write the json file
        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, 'w') as json_file:
            json_file.write(to_save_serialized)

        # now that the file is inside the model folder we generate a zipFile to be uploaded
        zip_file = None
        zip_file = _zipFiles([os.path.normpath(data['model_folder'])], storage.base_location,
                             os.path.join(storage.base_location, f'{os.path.normpath(data["model_folder"])}.zip'), True, None)

        if zip_file:
            # we publish the item
            files = {'files': open(zip_file, 'rb')}
            values = {'username': data['username'], 'uuid': data['uuid'],
                      'model_id': data['model_id'], 'zip_name': zip_file[zip_file.rfind(os.path.sep):],
                      'model_name': self.client_session.modelInfo.uri[self.client_session.modelInfo.uri.rfind(os.path.sep)+1:]}
            req = requests.put(
                'https://api.pyplan.com/api/reportManager/publishItems/', files=files, data=values)

            response = req.text

        # remove zip file and interfaces file
        storage.delete(zip_file)
        storage.delete(file_path)

        return response

    def _getStyles(self, reports, styles):
        for report in reports:
            styles.extend(DashboardStyle.objects.filter(pk__in=list(
                set(report.dashboards.all().values_list('styles', flat=True)))).all())
            if report.reports.count() > 0:
                self._getStyles(report.reports.all(), styles)

    def importItems(self, data):
        user_company_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        result = {'reports': [], 'dashboards': [], 'styles': []}
        styles_mappings = dict()
        for style in data['styles']:
            ds, _ = DashboardStyle.objects.update_or_create(
                definition=style['definition'],
                defaults={
                    'name': style['name'],
                    'owner_id': user_company_id,
                    'style_type': style['style_type']
                }
            )
            styles_mappings.update({style['id']: ds.pk})
            result['styles'].append(ds)
        for rep in data["reports"]:
            """
            check the uuid if the report is imported more than one time
            if the report exits with the same owner we update ir else we create a new one (links will be broken in this case)
            """

            use_new_uuid = True
            update = False
            if "uuid" in rep.keys():
                if Report.objects.filter(uuid=rep['uuid']).count() > 0:
                    if Report.objects.filter(uuid=rep['uuid'], owner__pk=user_company_id).count() > 0:
                        # we need to update the old_report with new data
                        use_new_uuid = False
                        update = True
                else:
                    # we need to create a new report with the same uuid
                    use_new_uuid = False

            defaults = {
                'model': model_id,
                'name': rep['name'],
                'is_fav': rep["is_fav"],
                'is_public': rep["is_public"],
                'order': rep["order"]
            }
            if not update:
                # we check if the parent exists
                parent_id = rep['parent_id'] if Report.objects.filter(
                    parent__id=rep['parent_id']).count() > 0 else None
                # if the parent doesnt exist we import it on the root (so parent is none)
                defaults.update({'parent_id': parent_id})
            report, _ = Report.objects.update_or_create(
                uuid=uuid.uuid4() if use_new_uuid else rep["uuid"],
                owner_id=user_company_id,
                defaults=defaults
            )
            self._createChildReportsAndDashboards(report, rep, result, styles_mappings)
        for dash in data["dashboards"]:
            """
            check the uuid if the dashboard is imported more than one time
            if the dashboard exits with the same owner we update ir else we create a new one (links will be broken in this case)
            """
            use_new_uuid = True

            if "uuid" in dash.keys():
                if Dashboard.objects.filter(uuid=dash['uuid']).count() > 0:
                    if Dashboard.objects.filter(uuid=dash['uuid'], owner__pk=user_company_id).count() > 0:
                        # we need to update the old dashboard with new data
                        use_new_uuid = False
                else:
                    # we need to create a new dashboard with the same uuid
                    use_new_uuid = False

            definition = None
            if 'definition' in dash:
                definition = dash['definition']
                self._update_definition(definition, styles_mappings)

            defaults = {
                'model': model_id,
                'name': dash['name'],
                'node': dash["node"] if "node" in dash else None,
                'is_fav': dash["is_fav"],
                'definition': definition,
                'order': dash["order"],
            }
            dash_created, _ = Dashboard.objects.update_or_create(
                uuid=uuid.uuid4() if use_new_uuid else dash["uuid"],
                owner_id=user_company_id,
                defaults=defaults
            )
            dash_created.styles.set(DashboardStyle.objects.filter(pk__in=list(
                map(lambda style: styles_mappings[style], dash["styles"]))))
            result["dashboards"].append(dash_created)
        return result

    def getShares(self, report_id):
        report = Report.objects.get(pk=report_id)
        is_shared = report.usercompanies.count() > 0 or report.departments.count() > 0
        return {
            "departments": Department.objects.filter(company_id=self.client_session.companyId).all(),
            "usercompanies_shares": report.usercompanies,
            "departments_shares": report.departments,
            "sharedToEveryone": report.is_public,
            "sharedTo": is_shared,
            "noShared": not is_shared,
        }

    def setShares(self, report_id, data):
        report = Report.objects.get(pk=report_id)

        report.is_public = data["sharedToEveryone"]

        report.usercompanies.clear()
        report.departments.clear()

        if not data["noShared"]:
            for usercompany_id in data["usercompanies_ids"]:
                usercompany = UserCompany.objects.get(pk=usercompany_id)
                report.usercompanies.add(usercompany)
            for department_id in data["departments_ids"]:
                department = Department.objects.get(pk=department_id)
                report.departments.add(department)
        report.save()
        return {
            "departments": Department.objects.filter(company_id=self.client_session.companyId).all(),
            "usercompanies_shares": report.usercompanies,
            "departments_shares": report.departments,
            "sharedToEveryone": report.is_public,
            "sharedTo": report.usercompanies.count() > 0 or report.departments.count() > 0,
        }

    # private

    def _createChildReportsAndDashboards(self, parent, item, result, styles_mappings):
        user_company_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        for rep in item["reports"]:
            """
            check the uuid if the report is imported more than one time
            if the report exits with the same owner we update ir else we create a new one (links will be broken in this case)
            """
            use_new_uuid = True
            if "uuid" in rep.keys():
                if Report.objects.filter(uuid=rep['uuid']).count() > 0:
                    if Report.objects.filter(uuid=rep['uuid'], owner__pk=user_company_id).count() > 0:
                        # we need to update the old_report with new data
                        use_new_uuid = False
                else:
                    # we need to create a new report with the same uuid
                    use_new_uuid = False

            defaults = {
                'model': model_id,
                'name': rep['name'],
                'is_fav': rep["is_fav"],
                'is_public': rep["is_public"],
                'order': rep["order"],
                'parent_id': rep["parent_id"],
            }
            report, created = Report.objects.update_or_create(
                uuid=uuid.uuid4() if use_new_uuid else rep["uuid"],
                owner_id=user_company_id,
                defaults=defaults
            )
            self._createChildReportsAndDashboards(report, rep, result, styles_mappings)
        for dash in item["dashboards"]:
            """
            check the uuid if the dashboard is imported more than one time
            if the dashboard exits with the same owner we update ir else we create a new one (links will be broken in this case)
            """
            use_new_uuid = True

            if "uuid" in dash.keys():
                if Dashboard.objects.filter(uuid=dash['uuid']).count() > 0:
                    if Dashboard.objects.filter(uuid=dash['uuid'], owner__pk=user_company_id).count() > 0:
                        # we need to update the old_dashboard with new data
                        use_new_uuid = False
                else:
                    # we need to create a new dashboard with the same uuid
                    use_new_uuid = False

            definition = None
            if 'definition' in dash:
                definition = dash['definition']
                self._update_definition(definition, styles_mappings)

            defaults = {
                'model': model_id,
                'name': dash['name'],
                'node': dash["node"] if "node" in dash else None,
                'is_fav': dash["is_fav"],
                'definition': definition,
                'order': dash["order"],
                'report': parent
            }
            dash_created, _ = Dashboard.objects.update_or_create(
                uuid=uuid.uuid4() if use_new_uuid else dash["uuid"],
                owner_id=user_company_id,
                defaults=defaults
            )
            dash_created.styles.set(DashboardStyle.objects.filter(pk__in=list(
                map(lambda item: styles_mappings[item], dash["styles"]))))

        result["reports"].append(parent)

    def _update_definition(self, definition, styles_mappings):
        """
        Updates dashboard definition with new dashboard_style ids.
        Properties checked:
            - 'colorSerie'
        """
        for def_type in ['definitionSmall', 'definitionMedium', 'definitionLarge']:
            if def_type in definition:
                for itemProp in definition[def_type]:
                    if 'itemProperties' in itemProp:
                        try:
                            color_serie = int(itemProp['itemProperties']['colorSerie'])
                            if color_serie in styles_mappings:
                                itemProp['itemProperties']['colorSerie'] = styles_mappings[color_serie]
                        except:
                            pass
                        try:
                            indicator_color = int(itemProp['itemProperties']['indicator']['styleLibrary'])
                            if indicator_color in styles_mappings:
                                itemProp['itemProperties']['indicator']['styleLibrary'] = styles_mappings[indicator_color]
                        except:
                            pass

    def _copyReport(self, report, owner_id, parent_id=None):
        old_report_id = report.pk
        report.owner_id = owner_id
        report.parent_id = parent_id
        report.pk = None
        report.uuid = uuid.uuid4()
        report.is_public = False

        report.save()

        for child_report in Report.objects.filter(parent_id=old_report_id):
            child_report.parent = report
            self._copyReport(child_report, owner_id, report.pk)

        for child_dashboard in Dashboard.objects.filter(report_id=old_report_id):
            child_dashboard.report = report
            self._copyDashboard(child_dashboard, owner_id, report.pk)

    def _copyDashboard(self, dashboard, owner_id, report_id=None):
        dashboard.pk = None
        dashboard.uuid = uuid.uuid4()
        dashboard.owner_id = owner_id
        dashboard.is_public = False
        dashboard.report_id = report_id

        dashboard.save()

    def _duplicateReport(self, report, is_main=False):
        old_report_id = report.pk
        report.pk = None
        report.uuid = uuid.uuid4()
        report.is_public = False

        if is_main:
            report.name += f"_copy {datetime.today().strftime('%Y%m%d-%H:%M:%S')}"
        report.save()

        for child_report in Report.objects.filter(parent_id=old_report_id):
            child_report.parent = report
            self._duplicateReport(child_report)

        for child_dashboard in Dashboard.objects.filter(report_id=old_report_id):
            child_dashboard.report = report
            self._duplicateDashboard(child_dashboard)

    def _duplicateDashboard(self, dashboard, is_main=False):
        dashboard.pk = None
        dashboard.uuid = uuid.uuid4()
        dashboard.is_public = False

        if is_main:
            dashboard.name += f"_copy {datetime.today().strftime('%Y%m%d-%H:%M:%S')}"
        dashboard.save()
