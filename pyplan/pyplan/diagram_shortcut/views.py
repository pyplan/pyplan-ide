from rest_framework import viewsets
from rest_framework.response import Response

from .models import DiagramShortcut
from .permissions import DiagramShortcutPermissions
from .serializers import (DiagramShortcutCreateSerializer,
                          DiagramShortcutSerializer)
from .service import DiagramShortcutService


class DiagramShortcutViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves diagram shortcut relations
    """
    queryset = DiagramShortcut.objects.all()
    serializer_class = DiagramShortcutSerializer
    permission_classes = (DiagramShortcutPermissions,)
    pagination_class = None

    def list(self, request, *args, **kwargs):
        service = DiagramShortcutService(self.request)
        shortcuts = service.list()
        return Response(DiagramShortcutSerializer(shortcuts, many=True).data)

    def create(self, request, *args, **kwargs):
        service = DiagramShortcutService(self.request)

        serializer = DiagramShortcutCreateSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        shortcut = service.create(serializer.data)

        return Response(DiagramShortcutSerializer(shortcut).data)
