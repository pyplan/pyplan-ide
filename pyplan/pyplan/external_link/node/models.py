from django.db import models

from pyplan.pyplan.external_link.models import ExternalLink


class NodeExternalLink(ExternalLink):
    external_link = models.OneToOneField(
        ExternalLink, on_delete=models.CASCADE, parent_link=True, related_name='node_external_link')
    node_id = models.CharField(max_length=255, blank=False, null=False)
