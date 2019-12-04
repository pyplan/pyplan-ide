from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.companies.models import Company


class Department(models.Model):
    code = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True, null=True)
    engine_definitions = JSONField(blank=True, null=True)
    login_action = JSONField(blank=True, null=True)

    # denied folders and modules
    denied_items = JSONField(
        blank=True, null=True, help_text='{ "folders": ["folder_a"], "modules": [{ "model_id": "model_a", "modules_ids": ["id_of_module"] }] }')

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.company.code}] - {self.code} - {self.name}"
