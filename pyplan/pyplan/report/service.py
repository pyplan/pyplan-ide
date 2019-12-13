import uuid
from datetime import datetime

from django.db.models import Q

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.dashboard.models import Dashboard
from pyplan.pyplan.dashboardstyle.models import DashboardStyle
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import Report


class ReportManagerService(BaseService):

    def getReport(self, report_id):
        return Report.objects.get(pk=report_id)

    def myReports(self, parent_id=None, favs=None):
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        reports = Report.objects.filter(
            model=model_id,
        )
        if parent_id and parent_id.isnumeric():
            reports = reports.filter(
                parent__pk=int(parent_id),
            )
        else:
            reports = reports.filter(
                owner_id=usercompany_id,
                parent__pk__isnull=True,
            )
        if type(favs) is bool and favs:
            reports = reports.filter(
                is_fav=True,
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
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        reports = Report.objects.filter(
            Q(departments__isnull=False) | Q(
                usercompanies__isnull=False) | Q(is_public=True),
            owner__pk=usercompany_id,
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
        return reports.order_by("order").distinct()

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
            order = dashboards_childrens.latest('order').order

        else:
            dashboards_childrens = Dashboard.objects.filter(
                report_id__isnull=True)
            order = dashboards_childrens.latest('order').order

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

    def _getStyles(self, reports, styles):
        for report in reports:
            styles.extend(DashboardStyle.objects.filter(pk__in=list(
                set(report.dashboards.all().values_list('styles', flat=True)))).all())
            if report.reports.count() > 0:
                self._getStyles(report.reports.all(), styles)

    def importItems(self, data):
        user_company_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        result = {"reports": [], "dashboards": [], "styles": []}
        styles = dict()
        for item in data["styles"]:
            ds = DashboardStyle.objects.create(
                name=item["name"],
                definition=item["definition"],
                style_type=item["style_type"],
                owner_id=user_company_id,
            )
            styles.update({item["id"]: ds.pk})
        for item in data["reports"]:
            use_new_uuid = True

            # check the uuid if the report is imported more than one time
            # the first time we import the uuid, else we create a new one
            if "uuid" in item.keys():
                use_new_uuid = Report.objects.filter(
                    uuid=item['uuid']).count() is 0

            report = Report.objects.create(
                model=model_id,
                name=item["name"],
                is_fav=item["is_fav"],
                is_public=item["is_public"],
                order=item["order"],
                parent_id=item["parent_id"],
                uuid=uuid.uuid4() if use_new_uuid else item["uuid"],
                owner_id=user_company_id,
            )
            self._createChildReportsAndDashboards(report, item, result, styles)
        for item in data["dashboards"]:
            use_new_uuid = True

            # check the uuid if the dashboard is imported more than one time
            # the first time we import the uuid, else we create a new one
            if "uuid" in item.keys():
                use_new_uuid = Dashboard.objects.filter(
                    uuid=item['uuid']).count() is 0

            dash_created = Dashboard.objects.create(
                model=model_id,
                name=item["name"],
                node=item["node"] if "node" in item else None,
                is_fav=item["is_fav"],
                definition=item["definition"] if "definition" in item else None,
                order=item["order"],
                uuid=uuid.uuid4() if use_new_uuid else item["uuid"],
                owner_id=user_company_id,
            )
            dash_created.styles.set(DashboardStyle.objects.filter(pk__in=list(
                map(lambda style: styles[style], item["styles"]))))
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

    def _createChildReportsAndDashboards(self, parent, item, result, styles):
        user_company_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        for rep in item["reports"]:
            report = Report.objects.create(
                model=model_id,
                name=rep["name"],
                is_fav=rep["is_fav"],
                is_public=rep["is_public"],
                order=item["order"],
                parent=parent,
                owner_id=user_company_id,
            )
            self._createChildReportsAndDashboards(report, rep, result, styles)
        for dash in item["dashboards"]:
            dash_created = Dashboard.objects.create(
                model=model_id,
                name=dash["name"],
                node=dash["node"] if "node" in dash else None,
                is_fav=dash["is_fav"],
                definition=dash["definition"] if "definition" in dash else None,
                order=item["order"],
                report=parent,
                owner_id=user_company_id
            )
            dash_created.styles.set(DashboardStyle.objects.filter(pk__in=list(
                map(lambda item: styles[item], dash["styles"]))))

        result["reports"].append(parent)

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
