from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.preference.models import Preference
from pyplan.pyplan.usercompanies.models import UserCompany


class UserCompanyPreference(models.Model):
    user_company = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING)
    preference = models.ForeignKey(Preference, on_delete=models.DO_NOTHING)
    definition = JSONField(null=True)
