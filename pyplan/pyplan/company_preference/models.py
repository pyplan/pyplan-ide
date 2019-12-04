from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.preference.models import Preference


class CompanyPreference(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    preference = models.ForeignKey(Preference, on_delete=models.DO_NOTHING)
    definition = JSONField(null=True)
