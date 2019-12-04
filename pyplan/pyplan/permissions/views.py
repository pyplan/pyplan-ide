from django.contrib.auth.models import Permission
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from .permissions import PermissionPermissions
from .serializers import PermissionSerializer


class PermissionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Permissions ViewSet
    """
    permission_classes = (PermissionPermissions,)
    serializer_class = PermissionSerializer
    pagination_class = None

    def get_queryset(self):
        app_labels = ['pyplan', 'account', ]
        return Permission.objects.filter(content_type__app_label__in=app_labels).all()
