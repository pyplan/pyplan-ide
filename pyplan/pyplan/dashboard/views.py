import coreapi
from django.contrib.auth.decorators import permission_required
from rest_framework import exceptions, permissions, routers, status
from rest_framework.decorators import api_view, permission_classes, schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.routers import url
from rest_framework.schemas import AutoSchema

from pyplan.pyplan.activity.serializers import ActivitySerializer
from pyplan.pyplan.activity.service import ActivityService

from .serializers.nodeDimension import NodeDimensionSerializer
from .serializers.nodeDimensionValue import NodeDimensionValueSerializer
from .serializers.nodeFullData import NodeFullDataSerializer
from .serializers.nodeQueryResult import NodeQueryResultSerializer
from .serializers.nodeResult import NodeResultSerializer
from .serializers.pivot import (PivotMetadataSerializer,
                                PivotNodeValueChangesSerializer,
                                PivotQuerySerializer)
from .serializers.serializers import (DashboardCreateSerializer,
                                      DashboardGetIndexValuesSerializer,
                                      DashboardGetSerializer,
                                      DashboardGetSharesSerializer,
                                      DashboardModelSerializer,
                                      DashboardSerializer,
                                      DashboardUpdateSerializer,
                                      DashboarSetSharesSerializer)
from .service import DashboardManagerService


class DashboardView(object):
    """
    Updates and retrieves dashboards relations
    """
    def register():
        return [
            url(r'^dashboardManager/myDashboards/$', DashboardView.myDashboards),
            url(r'^dashboardManager/companyDashboards/$',
                DashboardView.companyDashboards),
            url(r'^dashboardManager/sharedWithMe/$', DashboardView.sharedWithMe),
            url(r'^dashboardManager/allMyDashboards/',
                DashboardView.allMyDashboards),
            url(r'^dashboardManager/mySharedDashboards/$',
                DashboardView.mySharedDashboards),
            url(r'^dashboardManager/by_id/(?P<pk>\d+)/$', DashboardView.get),
            url(r'^dashboardManager/getNodeFullData/$',
                DashboardView.getNodeFullData),
            url(r'^dashboardManager/evaluateNode/$', DashboardView.evaluateNode),
            url(r'^dashboardManager/getOrCreate/$', DashboardView.getOrCreate),
            url(r'^dashboardManager/$', DashboardView.create),
            url(r'^dashboardManager/(?P<pk>\d+)/$', DashboardView.update),
            url(r'^dashboardManager/bulkDelete/$', DashboardView.bulkDelete),
            url(r'^dashboardManager/changeOrder/$', DashboardView.changeOrder),
            url(r'^dashboardManager/getIndexValues/$',
                DashboardView.getIndexValues),
            url(r'^dashboardManager/getNodeIndexes/$',
                DashboardView.getNodeIndexes),
            url(r'^dashboardManager/isResultComputed/$',
                DashboardView.isResultComputed),
            url(r'^dashboardManager/lastOpenDashboards/$',
                DashboardView.lastOpenDashboards),
            url(r'^dashboardManager/copy/$', DashboardView.copy),
            url(r'^dashboardManager/(?P<pk>\d+)/shares/$', DashboardView.getShares),
            url(r'^dashboardManager/(?P<pk>\d+)/setShares/$',
                DashboardView.setShares),
            url(r'^dashboardManager/(?P<pk>\d+)/externalLink/$',
                DashboardView.getExternalLink),
            url(r'^dashboardManager/pivotGrid/getCubeMetadata/$',
                DashboardView.getCubeMetadata),
            url(r'^dashboardManager/pivotGrid/getCubeValues/$',
                DashboardView.getCubeValues),
            url(r'^dashboardManager/pivotGrid/setCubeChanges/$',
                DashboardView.setCubeChanges),
            url(r'^dashboardManager/pivotGrid/getDimensionValues/$',
                DashboardView.getDimensionValues),
        ]

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_id", required=False,
                      location="query", description="Report ID"),
        coreapi.Field("favs", required=False,
                      location="query", description="bool"),
    ]))
    def myDashboards(request, *args, **kargs):
        report_id = request.query_params.get("report_id", None)
        favs = bool(request.query_params.get("favs", None))

        service = DashboardManagerService(request)
        result = service.myDashboards(report_id, favs)

        return Response(DashboardSerializer(result, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    @schema(AutoSchema(manual_fields=[]))
    def companyDashboards(request, *args, **kargs):
        service = DashboardManagerService(request)
        result = service.companyDashboards()
        return Response(DashboardSerializer(result, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("parent", required=False, location="query",
                      description="Parent report")
    ]))
    def sharedWithMe(request, *args, **kargs):
        report_id = request.query_params.get("report_id", None)

        service = DashboardManagerService(request)
        response = service.sharedWithMe(report_id)

        return Response(DashboardSerializer(response, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    def allMyDashboards(request, *args, **kargs):
        service = DashboardManagerService(request)
        response = service.allMyDashboards()

        return Response(DashboardSerializer(response, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("parent", required=False, location="query",
                      description="Parent report")
    ]))
    def mySharedDashboards(request, *args, **kargs):
        report_id = request.query_params.get("report_id", None)

        service = DashboardManagerService(request)
        response = service.mySharedDashboards(report_id)

        return Response(DashboardSerializer(response, many=True, context={'request': request}).data)

    @api_view(['GET'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("pk", required=False, location="query", description="ID")
    ]))
    def get(request, *args, **kargs):
        dashboard_id = int(kargs.get("pk"))
        if dashboard_id:
            service = DashboardManagerService(request)
            dashboard = service.getDashboard(dashboard_id)

            activity_service = ActivityService(request)
            activity_service.registerOpenDashboard(dashboard)
            return Response(DashboardGetSerializer(dashboard, context={'request': request}).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        # coreapi.Field("pk", required=False, location="query", description="ID")
    ]))
    def getNodeFullData(request, *args, **kargs):
        serializer = NodeQueryResultSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        service = DashboardManagerService(request)
        node_data = service.getNodeFullData(serializer.create(serializer.data))

        serialized_response = NodeFullDataSerializer(node_data)
        return Response(serialized_response.data)

    @api_view(['POST'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    def evaluateNode(request, *args, **kargs):
        serializer = NodeQueryResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = DashboardManagerService(request)
        data = serializer.create(serializer.data)
        if service.existNode(data.node):
            node_data = service.evaluateNode(data)
            serialized_response = NodeResultSerializer(node_data)
            return Response(serialized_response.data)
        return Response({"message": f"Node {data.node} does not exist."}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'POST'])
    @permission_required(['pyplan.add_dashboard', 'pyplan.change_dashboard', ], raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=False,
                      location="query", description="ID")
    ]))
    def getOrCreate(request, *args, **kargs):
        node_id = request.query_params.get("node", None)
        if node_id:
            service = DashboardManagerService(request)
            node_data = service.getOrCreate(node_id)

            serialized_response = DashboardModelSerializer(
                node_data, context={'request': request})
            return Response(serialized_response.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    @permission_required('pyplan.add_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("report_id", required=False,
                      location="query", description="Report ID")
    ]))
    def create(request, *args, **kargs):
        serializer = DashboardCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = DashboardManagerService(request)
        result = service.createDashboard(serializer.data)

        return Response(DashboardSerializer(result, context={'request': request}).data)

    @api_view(['PUT', 'PATCH'])
    @permission_required('pyplan.change_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("pk", required=False, location="query", description="ID")
    ]))
    def update(request, *args, **kargs):
        dashboard_id = int(kargs.get("pk"))
        if dashboard_id:
            serializer = DashboardUpdateSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            service = DashboardManagerService(request)
            dashboard = service.getDashboard(dashboard_id)
            # ToDo: return result?
            result = service.updateDashboard(dashboard, serializer.data)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['DELETE'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="body",),
    ]))
    @permission_required('pyplan.delete_dashboard', raise_exception=True)
    def bulkDelete(request, *args, **kargs):
        ids = request.data.get("values", None)
        if ids is not None:
            service = DashboardManagerService(request)
            result = service.bulkDelete(ids)
            # ToDo: return result?
            return Response(ids)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['PUT'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="body",),
    ]))
    @permission_classes((permissions.IsAuthenticated,))
    def changeOrder(request, *args, **kargs):
        ids = request.data.get("values", None)
        if ids is not None:
            service = DashboardManagerService(request)
            result = service.changeOrder(ids)
            return Response(ids)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("id", required=True, location="query",),
    ]))
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    def getIndexValues(request, *args, **kargs):
        serialized_rq = DashboardGetIndexValuesSerializer(
            data=request.query_params)
        serialized_rq.is_valid(raise_exception=True)

        service = DashboardManagerService(request)
        query_set = service.getIndexValues(serialized_rq.validated_data)

        if query_set:

            paginator = PageNumberPagination()
            paginator.page_size = 1000

            new_query_set = []
            for item in query_set['results']:
                new_query_set.append(item)
            try:
                context = paginator.paginate_queryset(new_query_set, request)

                paginated_context = paginator.get_paginated_response(context)

                serializer = NodeDimensionValueSerializer(
                    context, many=True)
                # absolute_uri = request.build_absolute_uri()
                return Response({
                    'next': paginated_context.data['next'],
                    'previous': paginated_context.data['previous'],
                    'count': paginated_context.data['count'],
                    'results': serializer.data,
                })
            except Exception as ex:
                pass
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, location="query")
    ]))
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    def getNodeIndexes(request, *args, **kargs):
        node_id = request.query_params.get("node", None)
        if node_id:
            service = DashboardManagerService(request)
            index_list = service.getNodeIndexes(node_id)
            serialized_response = NodeDimensionSerializer(
                index_list, many=True)
            return Response(serialized_response.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @api_view(['POST'])
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodes", required=True, location="body",),
    ]))
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    def isResultComputed(request, *args, **kargs):
        nodes = request.data.get("nodes", [])
        if nodes and len(nodes) > 0:
            service = DashboardManagerService(request)
            result = service.isResultComputed(nodes)
            if result:
                return Response(result)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    def lastOpenDashboards(request, *args, **kargs):
        service = ActivityService(request)
        serializer = ActivitySerializer(service.lastDashboards(), many=True)
        return Response(serializer.data)

    @api_view(['PUT'])
    @permission_required('pyplan.add_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("dashboard_id", required=True, location="body",),
        coreapi.Field("name", required=False, location="body",),
    ]))
    def copy(request, *args, **kargs):
        dashboard_id = request.data.get("dashboard_id", None)
        name = request.data.get("name", None)
        if dashboard_id:
            service = DashboardManagerService(request)
            dash_id = service.copy(dashboard_id, name)
            return Response({"id": dash_id})
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    @permission_required('pyplan.list_dashboards', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("dashboard_id", required=True, location="query",),
    ]))
    def getShares(request, *args, **kargs):
        dashboard_id = int(kargs.get("pk"))
        if dashboard_id:
            service = DashboardManagerService(request)

            result = service.getShares(dashboard_id)
            return Response(DashboardGetSharesSerializer(result).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    @permission_required('pyplan.share_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("dashboard_id", required=True, location="query",),
    ]))
    def setShares(request, *args, **kargs):
        dashboard_id = int(kargs.get("pk"))
        serializer = DashboarSetSharesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if dashboard_id:
            service = DashboardManagerService(request)
            result = service.setShares(dashboard_id, serializer.data)
            return Response(DashboardGetSharesSerializer(result).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    @permission_required('pyplan.generate_external_link', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("dashboard_id", required=True, location="query",),
    ]))
    def getExternalLink(request, *args, **kargs):
        dashboard_id = int(kargs.get("pk"))
        if dashboard_id:
            service = DashboardManagerService(request)
            result = service.getDashboard(dashboard_id)
            return Response(DashboardGetSharesSerializer(result).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Pivot

    @api_view(['POST'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("query", required=True, location="body",),
    ]))
    def getCubeMetadata(request, *args, **kargs):
        serializer = PivotQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = DashboardManagerService(request)
        result = service.getCubeMetadata(serializer.create(serializer.data))

        if result:
            return Response(PivotMetadataSerializer(result).data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['POST'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("query", required=True, location="body",),
    ]))
    def getCubeValues(request, *args, **kargs):
        serializer = PivotQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = DashboardManagerService(request)
        result = service.getCubeValues(serializer.create(serializer.data))

        if result:
            return Response(result)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['POST'])
    @permission_required('pyplan.change_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, location="body",),
        coreapi.Field("changes", required=True, location="body",),
    ]))
    def setCubeChanges(request, *args, **kargs):
        serializer = PivotNodeValueChangesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = DashboardManagerService(request)
        result = service.setCubeChanges(serializer.create(serializer.data))

        if result:
            return Response(result)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['POST'])
    @permission_required('pyplan.view_dashboard', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("query", required=True, location="body",),
    ]))
    def getDimensionValues(request, *args, **kargs):
        serializer = PivotQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = DashboardManagerService(request)
        result = service.getCubeDimensionValues(
            serializer.create(serializer.data))

        if result:
            return Response(result)
        return Response(status=status.HTTP_204_NO_CONTENT)
