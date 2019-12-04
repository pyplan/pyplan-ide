from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.usercompanies.models import UserCompany


class AppPool(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=255)
    usercompany = models.ForeignKey(
        UserCompany, on_delete=models.CASCADE, related_name='app_pool', null=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='app_pool')
    modelinfo = JSONField(blank=True, null=True)
