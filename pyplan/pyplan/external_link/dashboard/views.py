from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import DashboardExternalLinkPermissions
from .serializers import DashboardExternalLinkSerializer
from .service import DashboardExternalLinkService


class DashboardExternalLinkViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves dashboard external links relations
    """
    serializer_class = DashboardExternalLinkSerializer
    permission_classes = (DashboardExternalLinkPermissions,)

    def get_queryset(self):
        dashboard_id = self.request.query_params.get('dashboard_id', None)
        service = DashboardExternalLinkService(self.request)
        return service.getDashboardExternalLink(dashboard_id)

    def create(self, request, *args, **kwargs):
        service = DashboardExternalLinkService(self.request)
        dashboard_id = self.request.query_params.get('dashboard_id', None)
        if dashboard_id:
            result = service.createDashboardExternalLink(dashboard_id)
            return Response(DashboardExternalLinkSerializer(result).data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
