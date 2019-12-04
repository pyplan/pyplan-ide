from django.db import models

from pyplan.pyplan.usercompanies.models import UserCompany


class DiagramShortcut(models.Model):
    model = models.CharField(max_length=255)
    node_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    usercompany = models.ForeignKey(UserCompany, on_delete=models.CASCADE, related_name='diagram_shortcuts')

    def __str__(self):
        return f"[{self.usercompany.user.first_name}] - {self.model}{self.node_id}"
