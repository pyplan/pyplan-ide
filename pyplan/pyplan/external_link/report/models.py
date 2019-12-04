from django.db import models

from pyplan.pyplan.report.models import Report
from pyplan.pyplan.external_link.models import ExternalLink


class ReportExternalLink(ExternalLink):
    external_link = models.OneToOneField(
        ExternalLink, on_delete=models.CASCADE, parent_link=True, related_name='report_external_link')
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='external_links')

    def __str__(self):
        return self.report.name
