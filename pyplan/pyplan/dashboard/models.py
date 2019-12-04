from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.dashboardstyle.models import DashboardStyle
from pyplan.pyplan.report.models import Report
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany


class Dashboard(models.Model):
    model = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_fav = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    definition = JSONField(null=True)
    node = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(null=False, default=0)

    report = models.ForeignKey(
        Report, on_delete=models.CASCADE, null=True, related_name='dashboards')
    owner = models.ForeignKey(
        UserCompany, on_delete=models.DO_NOTHING, related_name='dashboards')

    usercompanies = models.ManyToManyField(
        UserCompany, related_name='shared_dashboards', blank=True)
    departments = models.ManyToManyField(
        Department, related_name='shared_dashboards', blank=True)

    styles = models.ManyToManyField(
        DashboardStyle, related_name='dashboards', blank=True)

    class Meta:
        permissions = (
            # "GETDASHBOARD" >> view_dashboard
            # "CREATEDASHBOARD" >> add_dashboard
            # "DELETEDASHBOARDS" >> delete_dashboard
            # "CHANGENAMEDASHBOARD" >> change_dashboard
            # "SHAREDASHBOARD"
            ("share_dashboard", "Can share a dashboard"),
            # "EXPORTDASHBOARD"
            ("export_dashboard", "Can export a dashboard"),
            # "IMPORTDASHBOARD"
            ("import_dashboard", "Can import a dashboard"),
            # "GENERATEEXTERNALLINK"
            ("generate_external_link", "Can generate external link to a dashboard"),
            # "MANAGEEXTERNALLINK"
            ("manage_external_link", "Can manage external link to a dashboard"),
            # "LASTDASHBOARDS"
            ("list_dashboards", "Can list dashboards"),
        )
