from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.preference_module.models import PreferenceModule


class Preference(models.Model):
    code = models.CharField(max_length=50, blank=False, null=False)
    module = models.ForeignKey(PreferenceModule, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    definition = JSONField(null=True)

    def __str__(self):
        return f"[{self.module}] - {self.code}"
