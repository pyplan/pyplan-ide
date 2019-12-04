from rest_framework import viewsets

from .models import PreferenceModule
from .permissions import PreferenceModulePermissions
from .serializers import PreferenceModuleSerializer


class PreferenceModuleViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves preference module relations
    """
    queryset = PreferenceModule.objects.all()
    serializer_class = PreferenceModuleSerializer
    permission_classes = (PreferenceModulePermissions,)
