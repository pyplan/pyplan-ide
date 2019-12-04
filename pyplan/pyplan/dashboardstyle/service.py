from rest_framework import exceptions
from pyplan.pyplan.common.baseService import BaseService
from .models import DashboardStyle

class DashboardStyleService(BaseService):

    def getByStyleType(self, style_type):
        """Get By Style Type"""
        if style_type and isinstance(style_type, int):
            return DashboardStyle.objects.filter(owner_id=self.client_session.userCompanyId, style_type=int(style_type))
        return DashboardStyle.objects.filter(owner_id=self.client_session.userCompanyId)

    def getById(self, id):
        """Get By Style Type"""
        return DashboardStyle.objects.filter(
            owner_id=self.client_session.userCompanyId, pk=id)
