from rest_framework import viewsets

from .models import Activity
from .permissions import ActivityPermissions
from .serializers import ActivitySerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves activities
    """
    queryset = Activity.objects.all()
    permission_classes = (ActivityPermissions,)
    serializer_class = ActivitySerializer
