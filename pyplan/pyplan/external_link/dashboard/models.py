from django.db import models

from pyplan.pyplan.dashboard.models import Dashboard
from pyplan.pyplan.external_link.models import ExternalLink


class DashboardExternalLink(ExternalLink):
    external_link = models.OneToOneField(
        ExternalLink, on_delete=models.CASCADE, parent_link=True, related_name='dashboard_external_link')
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='external_links')
