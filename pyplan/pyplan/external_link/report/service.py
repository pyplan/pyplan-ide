from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import ReportExternalLink


class ReportExternalLinkService(BaseService):

    def getReportExternalLink(self, report_id):
        model_path = self.client_session.modelInfo.uri
        user_company_id = self.client_session.userCompanyId

        external_links = ReportExternalLink.objects.filter(
            owner=user_company_id,
            model_path=model_path,
        )
        if not report_id is None and report_id.isnumeric():
            external_links = external_links.filter(
                report__pk=int(report_id),
            )
        return external_links.order_by('created_at')

    def createReportExternalLink(self, report_id):
        return ReportExternalLink.objects.create(
            report_id=report_id,
            model_path=self.client_session.modelInfo.uri,
            owner_id=self.client_session.userCompanyId,
        )
