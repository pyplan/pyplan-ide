from json import dumps

import coreapi
import coreschema
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse
from rest_framework import exceptions, routers, status
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.routers import url
from rest_framework.schemas import AutoSchema, ManualSchema

from pyplan.pyplan.filemanager.service import FileManagerService

from .serializers import (DuplicateItemsSerializer, ExportItemsAndPublishSerializer,
                          ExportItemsSerializer, ImportItemsSerializer,
                          ReportCreateUpdateSerializer, ReportGetNavigatorSerializer,
                          ReportGetSharesSerializer, ReportSerializer,
                          ReportSetSharesSerializer, SearchResultSerializer,
                          SetAsFavSerializer)
from .service import ReportManagerService


class ReportView(object):
    """
    Updates and retrieves reports relations
    """
    def register():
        return [
            url(r'^reportManager/myReports/$', ReportView.myReports),
            url(r'^reportManager/sharedWithMe/$', ReportView.sharedWithMe),
            url(r'^reportManager/mySharedReports/$', ReportView.mySharedReports),
            url(r'^reportManager/$', ReportView.create),
            url(r'^reportManager/(?P<pk>\d+)/$', ReportView.update),
            url(r'^reportManager/getNavigator/$', ReportView.getNavigator),
            url(r'^reportManager/bulkDelete/$', ReportView.bulkDelete),
            url(r'^reportManager/changeOrder/$', ReportView.changeOrder),
            url(r'^reportManager/search/$', ReportView.search),
            url(r'^reportManager/duplicateItems/$', ReportView.duplicateItems),
            url(r'^reportManager/copyToMyReports/$', ReportView.copyToMyReports),
            url(r'^reportManager/setAsFav/$', ReportView.setAsFav),
            url(r'^reportManager/dropOnReport/$', ReportView.dropOnReport),
            url(r'^reportManager/exportItems/$', ReportView.exportItems),
            url(r'^reportManager/exportItemsAndPublish/$',
                ReportView.exportItemsAndPublish),
            url(r'^reportManager/importItems/$', ReportView.importItems),
            url(r'^reportManager/(?P<pk>\d+)/shares/$', ReportView.getShares),
            url(r'^reportManager/(?P<pk>\d+)/setShares/$', ReportView.setShares),
        ]

    @api_view(['GET'])
    @permission_required('pyplan.get_my_reports', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("parent", required=False, location="query", description="Parent report"),
        coreapi.Field("favs", required=False, location="query", description="bool"),
    ]))
    def myReports(request, *args, **kargs):
        parent = request.query_params.get("parent", None)
        favs = bool(request.query_params.get("favs", None))

        service = ReportManagerService(request)
        result = service.myReports(parent, favs)

        return Response(ReportSerializer(result, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.get_my_reports', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("parent", required=False, location="query",
                      description="Parent report")
    ]))
    def sharedWithMe(request, *args, **kargs):
        parent = request.query_params.get("parent", None)

        service = ReportManagerService(request)
        response = service.sharedWithMe(parent)

        return Response(ReportSerializer(response, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.get_my_reports', raise_exception=True)
    def mySharedReports(request, *args, **kargs):
        service = ReportManagerService(request)
        response = service.mySharedReports()

        return Response(ReportSerializer(response, many=True, context={'request': request}).data)

    @api_view(['POST'])
    @permission_required('pyplan.add_report', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("parent", required=False, location="query",
                      description="Parent report")
    ]))
    def create(request, *args, **kargs):
        serializer = ReportCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ReportManagerService(request)
        result = service.createReport(serializer.data)

        return Response(ReportSerializer(result, context={'request': request}).data)

    @api_view(['PUT', 'PATCH'])
    @permission_required('pyplan.change_report', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("pk", required=False, location="query", description="ID")
    ]))
    def update(request, *args, **kargs):
        serializer = ReportCreateUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ReportManagerService(request)
        result = service.updateReport(int(kargs.get("pk")), serializer.data)
        if result:
            return Response(ReportSerializer(result, context={'request': request}).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_id", required=False, location="query",),
        coreapi.Field("dashboard_id", required=False, location="query",)
    ]))
    def getNavigator(request, *args, **kargs):
        report_id = request.query_params.get("report_id", None)
        dashboard_id = request.query_params.get("dashboard_id", None)

        try:
            if not report_id and not dashboard_id:
                raise exceptions.NotAcceptable(
                    "Error in ReportView.getNavigator(): dashboard_id or report_id required, can't both be None")
            service = ReportManagerService(request)
            dashboard = service.getNavigator(report_id, dashboard_id)
            return Response(ReportGetNavigatorSerializer(dashboard).data)
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in ReportView.getNavigator(): {str(ex)}")

    @api_view(['DELETE'])
    @permission_required('pyplan.delete_report', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="body",),
    ]))
    def bulkDelete(request, *args, **kargs):
        ids = request.data.get("values", None)
        if ids is not None:
            service = ReportManagerService(request)
            result = service.bulkDelete(ids)
            return Response(ids)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    @permission_required('pyplan.organize_reports', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="body",),
    ]))
    def changeOrder(request, *args, **kargs):
        ids = request.data.get("values", None)
        if ids is not None:
            service = ReportManagerService(request)
            result = service.changeOrder(ids)
            return Response(ids)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("text", required=True, description="Text to search"),
    ]))
    def search(request, *args, **kargs):
        text = str(request.query_params.get("text", ""))

        try:
            service = ReportManagerService(request)
            result = service.search(text)
            response = SearchResultSerializer(result)
            return Response(response.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array()),
    ]))
    def duplicateItems(request, *args, **kargs):
        serializer = DuplicateItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ReportManagerService(request)
        result = service.duplicateItems(serializer.data)

        return Response(status=status.HTTP_200_OK)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array()),
    ]))
    def copyToMyReports(request, *args, **kargs):
        serializer = DuplicateItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ReportManagerService(request)
        result = service.copyToMyReports(serializer.data)

        return Response(status=status.HTTP_200_OK)

    @api_view(['PUT'])
    @permission_required('pyplan.change_report', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array()),
    ]))
    def setAsFav(request, *args, **kargs):
        serializer = SetAsFavSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ReportManagerService(request)
        result = service.setAsFav(serializer.data)

        return Response(SearchResultSerializer(result, context={'request': request}).data)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("report_id", required=False,
                      location="query", description="Parent report ID"),
    ]))
    def dropOnReport(request, *args, **kargs):
        report_id = request.data.get("report_id", [])
        report_ids = request.data.get("report_ids", [])
        dashboard_ids = request.data.get("dashboard_ids", None)
        if report_ids or dashboard_ids:
            service = ReportManagerService(request)
            result = service.dropOnReport(report_ids, dashboard_ids, report_id)
            return Response(SearchResultSerializer(result, context={'request': request}).data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array()),
    ]))
    def exportItems(request, *args, **kargs):
        serializer = DuplicateItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ReportManagerService(request)
            # 1. get data and file name
            data_to_export, file_name = service.exportItems(serializer.data)
            # 2. serialize data and convert to string
            json_string = dumps(ExportItemsSerializer(
                data_to_export).data, indent=None)
            # 3. make file stream from json string
            file_stream = FileManagerService().makeJsonStream(json_string)
            # 4. stream file as http response
            response = FileResponse(
                file_stream, as_attachment=True, filename=file_name)
            response['Content-Disposition'] = f'attachment; filename={file_name}'
            return response
        except Exception as ex:
            raise exceptions.NotAcceptable(detail=ex)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("username", required=True,
                      location="body", schema=coreschema.String),
        coreapi.Field("uuid", required=True,
                      location="body", schema=coreschema.String),
        coreapi.Field("model_folder", required=True,
                      location="body", schema=coreschema.String),
        coreapi.Field("model_id", required=True,
                      location="body", schema=coreschema.String),
        coreapi.Field("report_ids", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("dashboard_ids", required=True,
                      location="body", schema=coreschema.Array())
    ]))
    def exportItemsAndPublish(request, *args, **kargs):
        serializer = ExportItemsAndPublishSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ReportManagerService(request)
            external_link = service.exportItemsAndPublish(serializer.data)
            if external_link:
                return Response(external_link, status=status.HTTP_200_OK)
            return Response('There was an error publishing the item', status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            raise exceptions.NotAcceptable(detail=ex)

    @api_view(['PUT'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("reports", required=True, location="body",
                      schema=coreschema.Array()),
        coreapi.Field("dashboards", required=True,
                      location="body", schema=coreschema.Array()),
        coreapi.Field("styles", required=True, location="body",
                      schema=coreschema.Array()),
    ]))
    def importItems(request, *args, **kargs):
        serializer = ImportItemsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            result = ReportManagerService(request).importItems(serializer.data)
            return Response(ExportItemsSerializer(result).data)
        except Exception as ex:
            raise exceptions.NotAcceptable(detail=ex)

    @api_view(['GET'])
    @permission_classes((IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_id", required=True, location="query",),
    ]))
    def getShares(request, *args, **kargs):
        report_id = int(kargs.get("pk"))
        if report_id:
            service = ReportManagerService(request)
            # TODO: return accessList
            try:
                result = service.getShares(report_id)
                return Response(ReportGetSharesSerializer(result).data)
            except ObjectDoesNotExist as ex:
                return Response({"message": str(ex)}, status=status.HTTP_404_NOT_FOUND)
            except Exception as ex:
                return Response({"message": str(ex)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    @permission_required('pyplan.change_report', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_id", required=True, location="query",),
    ]))
    def setShares(request, *args, **kargs):
        report_id = int(kargs.get("pk"))
        serializer = ReportSetSharesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if report_id:
            service = ReportManagerService(request)
            result = service.setShares(report_id, serializer.data)
            return Response(ReportGetSharesSerializer(result).data)
        return Response(status=status.HTTP_404_NOT_FOUND)
