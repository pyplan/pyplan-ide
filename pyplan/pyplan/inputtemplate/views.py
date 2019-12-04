import coreapi
from django.contrib.auth.decorators import permission_required
from django.urls import path
from rest_framework import exceptions
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes, schema)
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .models import InputTemplate
from .serializers.inputTemplateSerializer import (
    InputTemplateGetDataSerializer, InputTemplateListSerializer,
    InputTemplateSerializer)
from .serializers.inputTemplateSetDataSerializer import (
    InputTemplateSetDataParamsSerializer,
    OutputTemplateSetDataParamsSerializer)
from .service import InputTemplateService


class InputTemplateView(object):
    """
    Updates and retrieves InputTemplate relations
    """
    @staticmethod
    def register():
        return [
            # model related urls
            path('inputTemplates/list/', InputTemplateView.list),
            path('inputTemplates/getMetadata/', InputTemplateView.getMetadata),
            path('inputTemplates/getData/', InputTemplateView.getData),
            path('inputTemplates/setData/', InputTemplateView.setData),
        ]

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.view_all_input_templates', raise_exception=True)
    def list(request, *args, **kargs):

        try:
            service = InputTemplateService(request)
            serializer = InputTemplateListSerializer(service.list(), many=True)
            return Response(serializer.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.view_inputtemplate', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("id", required=True, description="Input template id")
    ]))
    def getMetadata(request, *args, **kargs):
        id = str(request.query_params.get("id", ""))
        try:
            service = InputTemplateService(request)
            return Response(service.getMetadata(id))
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_required('pyplan.view_inputtemplate', raise_exception=True)
    def getData(request, *args, **kargs):
        try:
            serializer = InputTemplateGetDataSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            service = InputTemplateService(request)
            return Response(service.getData(serializer.validated_data))
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_required('pyplan.change_inputtemplate', raise_exception=True)
    def setData(request, *args, **kargs):
        try:
            serializer = InputTemplateSetDataParamsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            service = InputTemplateService(request)
            data = service.setData(serializer.validated_data)

            serialized_response = OutputTemplateSetDataParamsSerializer(data, many=True)
            return Response(serialized_response.data)

        except Exception as ex:
            raise exceptions.NotAcceptable(ex)
