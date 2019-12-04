import coreapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.routers import url
from rest_framework import status, permissions


class HealthcheckView(object):
    """
    Healthcheck Views
    """
    def register():
        urlpatterns = [
            url(r'^healthcheck/$', HealthcheckView.get),
        ]
        return urlpatterns

    @api_view(['GET'])
    @permission_classes((permissions.AllowAny,))
    def get(request, *args, **kargs):
        return Response(status=status.HTTP_200_OK)
