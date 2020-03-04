from django.db import models

from pyplan.pyplan.preference.models import Preference
from pyplan.pyplan.users.models import User


class Company(models.Model):
    code = models.CharField(max_length=50, db_index=True, unique=True)
    name = models.CharField(max_length=255)
    system = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    licence = models.CharField(null=True, max_length=4000)
    # aDDomain = models.CharField(null=True,max_length=2000)
    users = models.ManyToManyField(User, through='UserCompany')
    preferences = models.ManyToManyField(
        Preference, through='CompanyPreference')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'

        permissions = (
            # Company Manager
            # "GETCOMPANY" -> view_company
            # "CREATECOMPANY" -> add_company
            # "LISTCOMPANIES"
            ("list_companies", "List companies"),
            # "UPDATECOMPANY" -> change_company
            # "DELETECOMPANY" -> delete_company
        )
