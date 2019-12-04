from rest_framework import viewsets

from .models import Preference
from .permissions import PreferencePermissions
from .serializers import PreferenceSerializer


class PreferenceViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves preference relations
    """
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = (PreferencePermissions,)
