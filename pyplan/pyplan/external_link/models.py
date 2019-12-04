import uuid

from django.db import models

from pyplan.pyplan.usercompanies.models import UserCompany


class ExternalLink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_path = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    common_instance = models.BooleanField(default=False)

    owner = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING, related_name='external_links')

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.id)
