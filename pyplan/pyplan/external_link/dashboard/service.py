from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import DashboardExternalLink


class DashboardExternalLinkService(BaseService):

    def getDashboardExternalLink(self, dashboard_id):
        model_path = self.client_session.modelInfo.uri
        user_company_id = self.client_session.userCompanyId

        external_links = DashboardExternalLink.objects.filter(
            owner=user_company_id,
            model_path=model_path,
        )
        if not dashboard_id is None and dashboard_id.isnumeric():
            external_links = external_links.filter(
                dashboard__pk=int(dashboard_id),
            )
        return external_links.order_by('created_at')

    def createDashboardExternalLink(self, dashboard_id):
        return DashboardExternalLink.objects.create(
            dashboard_id=dashboard_id,
            model_path=self.client_session.modelInfo.uri,
            owner_id=self.client_session.userCompanyId,
        )
