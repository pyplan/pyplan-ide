from rest_framework import viewsets

from .models import UserCompanyPreference
from .permissions import UserCompanyPreferencePermissions
from .serializers import UserCompanyPreferenceSerializer


class UserCompanyPreferenceViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves user company preference relations
    """
    queryset = UserCompanyPreference.objects.all()
    serializer_class = UserCompanyPreferenceSerializer
    permission_classes = (UserCompanyPreferencePermissions,)
