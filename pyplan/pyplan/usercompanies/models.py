from django.db import models
from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.preference.models import Preference
from pyplan.pyplan.users.models import User

class UserCompany(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='usercompanies')
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)

    active = models.BooleanField(default=True)
    preferences = models.ManyToManyField(Preference, through='UserCompanyPreference')
    departments = models.ManyToManyField(Department, related_name='usercompanies')

    class META:
        unique_together = ('user', 'company',)
        verbose_name_plural = 'usercompanies'

    def __str__(self):
        return f"{self.company} - {self.user}"
