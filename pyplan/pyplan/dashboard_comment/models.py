from django.db import models
from pyplan.pyplan.dashboard.models import Dashboard
from pyplan.pyplan.usercompanies.models import UserCompany

class DashboardComment(models.Model):
    comment = models.TextField()
    extra_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING)

    class Meta:
        permissions = (
            # "CREATEDASHBOARDCOMMENT" >> add_dashboardcomment
            # "LISTDASHBOARDCOMMENTS"
            ("list_dashboardcomments", "Can list dashboard comments"),
        )
