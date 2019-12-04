from rest_framework import viewsets

from .models import CompanyPreference
from .permissions import CompanyPreferencePermissions
from .serializers import CompanyPreferenceSerializer


class CompanyPreferenceViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves company preference relations
    """
    queryset = CompanyPreference.objects.all()
    serializer_class = CompanyPreferenceSerializer
    permission_classes = (CompanyPreferencePermissions,)
