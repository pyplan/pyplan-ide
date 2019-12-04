from rest_framework import viewsets

from .models import DashboardComment
from .permissions import DashboardCommentPermissions
from .serializers import DashboardCommentSerializer


class DashboardCommentViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves dashboard comments relations
    """
    queryset = DashboardComment.objects.all()
    serializer_class = DashboardCommentSerializer
    permission_classes = (DashboardCommentPermissions,)
