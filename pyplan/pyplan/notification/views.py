from rest_framework import exceptions, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .service import NotificationService


class NotificationViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        service = NotificationService(request)
        result = service.retrieveMessages()
        return Response(data=result)

    def partial_update(self, request, *args, **kwargs):
        try:
            id = kwargs.get('pk')
            if id:
                service = NotificationService(request)
                result = service.updateMessage(id)
                return Response()
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)
