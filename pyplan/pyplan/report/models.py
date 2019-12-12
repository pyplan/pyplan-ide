import uuid
from django.db import models
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany


class Report(models.Model):
    model = models.CharField(max_length=255, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_fav = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    order = models.IntegerField(null=False, default=0)
    uuid = models.UUIDField(default=uuid.uuid4, null=True)

    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, related_name='reports')
    owner = models.ForeignKey(
        UserCompany, on_delete=models.DO_NOTHING, related_name='reports')

    usercompanies = models.ManyToManyField(
        UserCompany, related_name='shared_reports', blank=True)
    departments = models.ManyToManyField(
        Department, related_name='shared_reports', blank=True)

    class Meta:
        permissions = (
            # "VIEWREPORTMANAGER" >> view_report
            # "MYREPORTS"
            ("get_my_reports", "Can get my reports"),
            # "ORGANIZEUSERDASHBOARD"
            ("organize_reports", "Can organize reports"),
        )
