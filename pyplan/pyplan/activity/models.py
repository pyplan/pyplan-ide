import uuid
from enum import Enum

from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.usercompanies.models import UserCompany


class ActivityType(Enum):
    MODEL = "model"
    DASHBOARD = "dashboard"

    def __str__(self):
        return self.value


class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    updated_at = models.DateTimeField(auto_now=True)
    usercompany = models.ForeignKey(
        UserCompany, on_delete=models.CASCADE, related_name='activities')

    type = models.CharField(
        max_length=50,
        choices=[(tag, tag.value)
                 for tag in ActivityType]  # Choices is a list of Tuple
    )
    model_path = models.CharField(max_length=500, blank=False, null=False)
    model_name = models.CharField(max_length=254, blank=False, null=False)

    info = JSONField(null=True)

    class Meta:
        ordering = ["-updated_at"]
