from rest_framework import status, viewsets
from rest_framework.response import Response

from .permissions import ReportExternalLinkPermissions
from .serializers import ReportExternalLinkSerializer
from .service import ReportExternalLinkService


class ReportExternalLinkViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves report external links relations
    """
    serializer_class = ReportExternalLinkSerializer
    permission_classes = (ReportExternalLinkPermissions,)

    def get_queryset(self):
        report_id = self.request.query_params.get('report_id', None)
        service = ReportExternalLinkService(self.request)
        return service.getReportExternalLink(report_id)

    def create(self, request, *args, **kwargs):
        service = ReportExternalLinkService(self.request)
        report_id = self.request.query_params.get('report_id', None)
        if report_id:
            result = service.createReportExternalLink(report_id)
            return Response(ReportExternalLinkSerializer(result).data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
