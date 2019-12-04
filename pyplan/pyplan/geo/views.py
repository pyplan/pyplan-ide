import coreapi
from django.urls import path
from rest_framework import exceptions, permissions
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.schemas import AutoSchema, ManualSchema
from rest_framework.response import Response
from .serializers.geoquery import GeoQuerySerializer
from .serializers.geodata import GeoDataSerializer
from .service import GeoService

class GeoView(object):
    """
    Perform Geo calls
    """

    @staticmethod
    def register():
        urlpatterns = [
            path('geo/getGeoData/', GeoView.getGeoData),
            path('geo/getGeoDetail/', GeoView.getGeoDetail),
            path('geo/getBubbleInfo/', GeoView.getBubbleInfo),
        ]
        return urlpatterns

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("quey", required=True, description="Geo query")
    ]))
    def getGeoData(request, *args, **kargs):

        serializer = GeoQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        service = GeoService(request)
        node_data = service.getGeoData(serializer.create(serializer.data))

        serializer = GeoDataSerializer(node_data)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("quey", required=True, description="Geo query")
    ]))
    def getGeoDetail(request, *args, **kargs):

        pass

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("quey", required=True, description="Geo query")
    ]))
    def getBubbleInfo(request, *args, **kargs):
        raise exceptions.NotFound("NOT YEY IMPLEMENTED")
