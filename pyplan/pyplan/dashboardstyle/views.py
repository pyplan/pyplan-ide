from rest_framework import viewsets

from .models import DashboardStyle
from .permissions import DashboardStylePermissions
from .serializers import DashboardStyleSerializer
from .service import DashboardStyleService


class DashboardStyleViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves dashboard styles relations
    """
    pagination_class = None
    serializer_class = DashboardStyleSerializer
    permission_classes = (DashboardStylePermissions,)

    def get_queryset(self):
        if self.action == "list":
            style_type = self.request.query_params.get('styleType', None)
            service = DashboardStyleService(self.request)
            return service.getByStyleType(style_type)
        elif self.action == "retrieve":
            id = self.kwargs['pk']
            service = DashboardStyleService(self.request)
            return service.getById(id)
        return DashboardStyle.objects.all()
