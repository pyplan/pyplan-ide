from django.db import models


class PreferenceModule(models.Model):
    code = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.code
