from jsonfield import JSONField
from django.db import models

from pyplan.pyplan.usercompanies.models import UserCompany


class DashboardStyle(models.Model):
    name = models.CharField(max_length=500)
    definition = JSONField(null=True)

    ALL = -1
    RANGE_MAP_COLOR = 0
    RANGE_INDICATOR = 1
    RANGE_GAUGE = 2
    COLOR_SERIES = 3
    ICONS = 4

    STYLE_TYPES = (
        (ALL, 'All'),
        (RANGE_MAP_COLOR, 'Range map color'),
        (RANGE_INDICATOR, 'Range indicator'),
        (RANGE_GAUGE, 'Range gauge'),
        (COLOR_SERIES, 'Color series'),
        (ICONS, 'Icons'),
    )
    style_type = models.IntegerField(
        choices=STYLE_TYPES,
        default=ALL,
    )

    owner = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING)

    # permissions
    # "UPDATESTYLELIBRARY" >> change_dashboardstyle
    # "CREATESTYLELIBRARY" >> add_dashboardstyle
    # "DELETESTYLELIBRARY" >> delete_dashboardstyle
