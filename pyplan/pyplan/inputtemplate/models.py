from jsonfield import JSONField
from django.db import models
from pyplan.pyplan.usercompanies.models import UserCompany
from pyplan.pyplan.department.models import Department


class InputTemplate(models.Model):
    code = models.CharField(max_length=50, blank=False,
                            null=False, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    filepath = models.CharField(max_length=255, blank=True, null=True)
    definition = JSONField(blank=True, null=True)
    owner = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING)
    departments = models.ManyToManyField(Department, blank=True)

    class Meta:
        permissions = (
            # "VIEWINPUTTEMPLATES"
            ("view_my_input_templates", "View my input templates"),
            # "VIEWALLTEMPLATES"
            ("view_all_input_templates", "View all input templates"),
            # "MANAGETEMPLATES"
            ("manage_input_templates", "Manage templates"),
        )
