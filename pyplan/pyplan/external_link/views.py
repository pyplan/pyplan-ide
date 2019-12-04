from rest_framework import viewsets

from .models import ExternalLink
from .permissions import ExternalLinkPermissions
from .serializers import ExternalLinkSerializer


class ExternalLinkViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves external links relations
    """
    queryset = ExternalLink.objects.all()
    serializer_class = ExternalLinkSerializer
    permission_classes = (ExternalLinkPermissions,)
