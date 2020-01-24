import coreapi
from django.contrib.auth.decorators import permission_required
from django.http import FileResponse
from django.urls import path
from rest_framework import exceptions, parsers, permissions, status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes, schema)
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema, ManualSchema

from pyplan.pyplan.activity.serializers import ActivitySerializer
from pyplan.pyplan.activity.service import ActivityService
from pyplan.pyplan.dashboard.service import DashboardManagerService
from pyplan.pyplan.filemanager.serializers import FileEntrySerializer

from .classes.node import Node
from .serializers.CopyAsValuesParamSerializer import \
    CopyAsValuesParamSerializer
from .serializers.ExportModuleToFileSerializer import \
    ExportModuleToFileSerializer
from .serializers.ExportNodeSerializer import ExportNodeSerializer
from .serializers.ImportModuleDataSerializer import ImportModuleDataSerializer
from .serializers.ModelInfoSerializer import ModelInfoSerializer
from .serializers.ModelPreferenceSerializer import ModelPreferenceSerializer
from .serializers.NavigateDiagramSerializer import NavigateDiagramSerializer
from .serializers.NodeIdentifierSerializer import NodeIdentifierSerializer
from .serializers.NodeIdSerializer import NodeIdSerializer
from .serializers.NodePropertiesSerializer import NodePropertiesSerializer
from .serializers.NodeSearchResultSerializer import NodeSearchResultSerializer
from .serializers.NodeSerializer import NodeSerializer
from .serializers.NodesSerializer import NodesSerializer
from .serializers.NodesSizeAndPositionSerializer import \
    NodesSizeAndPositionSerializer
from .serializers.UploadFilesSerializer import UploadFilesSerializer
from .serializers.WizardRequestSerialzier import WizardRequestSerializer
from .service import ModelManagerService


class ModelManagerView(object):
    """
    Class to dialog with pyplan model
    """
    @staticmethod
    def register():
        return [
            # model related urls
            path('modelManager/openModel/', ModelManagerView.openModel),
            path('modelManager/getModelInfo/', ModelManagerView.getModelInfo),
            path('modelManager/saveModel/', ModelManagerView.saveModel),
            path('modelManager/saveModelAs/', ModelManagerView.saveModelAs),
            path('modelManager/navigateDiagram/',
                 ModelManagerView.navigateDiagram),
            path('modelManager/getArrows/', ModelManagerView.getArrows),
            path('modelManager/getToolbars/', ModelManagerView.getToolbars),
            path('modelManager/createNewModel/',
                 ModelManagerView.createNewModel),
            path('modelManager/getModelPreferences/',
                 ModelManagerView.getModelPreferences),
            path('modelManager/lastOpenModels/',
                 ModelManagerView.lastOpenModels),
            path('modelManager/changeToOtherModelSession/',
                 ModelManagerView.changeToOtherModelSession),
            path('modelManager/setModelPreferences/',
                 ModelManagerView.setModelPreferences),
            path('modelManager/closeModel/', ModelManagerView.closeModel),
            # node related urls
            path('modelManager/getNodeProperties/',
                 ModelManagerView.getNodeProperties),
            path('modelManager/setNodeProperties/',
                 ModelManagerView.setNodeProperties),
            path('modelManager/setNodesProperties/',
                 ModelManagerView.setNodesProperties),
            path('modelManager/getNodeInputs/',
                 ModelManagerView.getNodeInputs),
            path('modelManager/getNodeOutputs/',
                 ModelManagerView.getNodeOutputs),
            path('modelManager/searchNodes/', ModelManagerView.searchNodes),
            path('modelManager/searchForAutocomplete/',
                 ModelManagerView.searchForAutocomplete),
            path('modelManager/previewNode/', ModelManagerView.previewNode),
            path('modelManager/getSelector/', ModelManagerView.getSelector),
            path('modelManager/setNodesSize/', ModelManagerView.setNodesSize),
            path('modelManager/setNodesPosition/',
                 ModelManagerView.setNodesPosition),
            path('modelManager/getNodeProfile/',
                 ModelManagerView.getNodeProfile),
            path('modelManager/createNode/', ModelManagerView.createNode),
            path('modelManager/deleteNodes/', ModelManagerView.deleteNodes),
            path('modelManager/createAlias/', ModelManagerView.createAlias),
            path('modelManager/createInputNode/',
                 ModelManagerView.createInputNode),
            path('modelManager/copyNodes/', ModelManagerView.copyNodes),
            path('modelManager/copyAsValues/', ModelManagerView.copyAsValues),
            path('modelManager/moveNodes/', ModelManagerView.moveNodes),
            path('modelManager/stop/', ModelManagerView.stop),
            path('modelManager/setNodeZ/', ModelManagerView.setNodeZ),
            path('modelManager/setNodeIdFromTitle/',
                 ModelManagerView.setNodeIdFromTitle),
            path('modelManager/executeForRefresh/',
                 ModelManagerView.executeForRefresh),
            path('modelManager/exportFlatNode/',
                 ModelManagerView.exportFlatNode),
            path('modelManager/exportCurrentNode/',
                 ModelManagerView.exportCurrentNode),
            path('modelManager/exportModuleToFile/',
                 ModelManagerView.exportModuleToFile),
            path('modelManager/importModuleFromFile/',
                 ModelManagerView.importModuleFromFile),
            path('modelManager/getFilesForImportWizard/',
                 ModelManagerView.getFilesForImportWizard),
            path('modelManager/callWizard/', ModelManagerView.callWizard),
            path('modelManager/executeButton/',
                 ModelManagerView.executeButton),
            path('modelManager/isInBackground/',
                 ModelManagerView.isInBackground),
            # helper functions
            path('modelManager/uploadFileToTemp/',
                 ModelManagerView.uploadFileToTemp),
            path('modelManager/installLibrary/',
                 ModelManagerView.installLibrary),
            path('modelManager/listInstalledLibraries/',
                 ModelManagerView.listInstalledLibraries),
            path('modelManager/uninstallLibrary/',
                 ModelManagerView.uninstallLibrary),
            path('modelManager/getInstallProgress/',
                 ModelManagerView.getInstallProgress),
        ]

    # model related methods
    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("file", required=True, description="Model file to open")
    ]))
    def openModel(request, *args, **kargs):
        file = str(request.query_params.get("file", ""))
        if file:
            activity_service = ActivityService(request)
            activity_service.registerOpenModel(file)
            service = ModelManagerService(request)
            model_info = service.openModel(file)
            serializer = ModelInfoSerializer(model_info)
            return Response(serializer.data)
        raise exceptions.NotAcceptable("Model file not found")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def getModelInfo(request, *args, **kargs):
        service = ModelManagerService(request)
        model_info = service.getModelInfo()
        return Response(model_info)

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.change_model', raise_exception=True)
    def saveModel(request, *args, **kargs):
        try:
            service = ModelManagerService(request)
            result = service.saveModel()
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.change_model', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("name", required=True, description="Name of the model")
    ]))
    def saveModelAs(request, *args, **kargs):
        modelName = str(request.query_params.get("name", ""))
        if modelName:
            if len(modelName) > 0:
                service = ModelManagerService(request)
                new_model = service.saveModelAs(modelName)
                serializer = ModelInfoSerializer(new_model)
                return Response(serializer.data)
            else:
                raise exceptions.NotAcceptable("Empty modelName was provided")
        else:
            raise exceptions.NotAcceptable("No modelName was provided")

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.view_influence_diagram', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("moduleId", required=False, description="Module ID"),
        coreapi.Field("includeArrows", required=False,
                      description="Include Arrows")
    ]))
    def navigateDiagram(request, *args, **kargs):
        module_id = str(request.query_params.get("moduleId", ""))
        include_arrows = bool(request.query_params.get("includeArrows", False))
        try:
            service = ModelManagerService(request)
            diagram = service.navigateDiagram(module_id, include_arrows)
            serializer = NavigateDiagramSerializer(diagram)
            return Response(serializer.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("moduleId", required=False, description="Module ID")
    ]))
    def getArrows(request, *args, **kargs):
        module_id = str(request.query_params.get("moduleId", ""))
        try:
            service = ModelManagerService(request)
            result = service.getArrows(module_id)
            serializer = NavigateDiagramSerializer(
                {
                    "arrows": result["arrows"],
                    "nodes": [],
                    "breadcrumb": [],
                    "moduleId": result["module_id"]
                }
            )
            return Response(serializer.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def getToolbars(request, *args, **kargs):
        try:
            service = ModelManagerService(request)
            result = service.getToolbars()
            if result:
                return Response(result)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.change_model', raise_exception=True)
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("modelName", required=True,
                      description="Name of the model")
    ]))
    def createNewModel(request, *args, **kargs):
        modelName = str(request.query_params.get("modelName", ""))
        if modelName:
            if len(modelName) > 0:
                service = ModelManagerService(request)
                new_model = service.createNewModel(modelName)
                serializer = ModelInfoSerializer(new_model)
                return Response(serializer.data)
            else:
                raise exceptions.NotAcceptable("Empty modelName was provided")
        else:
            raise exceptions.NotAcceptable("No modelName was provided")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def getModelPreferences(request, *args, **kargs):
        try:
            service = ModelManagerService(request)
            result = service.getModelPreferences()
            return Response(result)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_required('pyplan.list_last_models', raise_exception=True)
    def lastOpenModels(request, *args, **kargs):
        service = ActivityService(request)
        serializer = ActivitySerializer(service.lastModels(), many=True)
        return Response(serializer.data)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def changeToOtherModelSession(request, *args, **kargs):
        new_session_key = request.query_params.get("new_session_key", "")
        model_info = ModelManagerService(
            request).changeToOtherModelSession(new_session_key)
        serializer = ModelInfoSerializer(model_info)
        return Response(serializer.data)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("modelPreferences", required=False,
                      description="Model Preferences Object")
    ]))
    def setModelPreferences(request, *args, **kargs):
        serializer = ModelPreferenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            return Response(service.setModelPreferences(serializer.validated_data))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in setting model preferences:{str(ex)}")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[]))
    def closeModel(request, *args, **kargs):
        service = ModelManagerService(request)
        result = service.closeModel()
        return Response(result)

    # node related methods
    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, description="Node ID"),
        coreapi.Field("properties", required=False,
                      description="Required node properties")
    ]))
    def getNodeProperties(request, *args, **kargs):
        serializer = NodePropertiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            result = service.getNodeProperties(
                serializer.validated_data["node"], serializer.validated_data["properties"]
            )
            response = NodePropertiesSerializer(result)
            return Response(response.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, description="Node ID"),
        coreapi.Field("properties", required=False,
                      description="Node properties")
    ]))
    def setNodeProperties(request, *args, **kargs):
        serializer = NodePropertiesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            service = ModelManagerService(request)
            result = service.setNodeProperties(
                serializer.validated_data["node"], serializer.validated_data["properties"]
            )
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, description="Node ID"),
        coreapi.Field("properties", required=False,
                      description="Node properties")
    ]))
    def setNodesProperties(request, *args, **kargs):
        result = True
        try:
            if request.data:
                if len(request.data) > 0:
                    serializer = NodePropertiesSerializer(
                        data=request.data, many=True)
                    serializer.is_valid(raise_exception=True)
                    service = ModelManagerService(request)
                    for data in serializer.validated_data:
                        result = service.setNodeProperties(
                            data["node"], data["properties"]) and result
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, description="Node ID")
    ]))
    def getNodeInputs(request, *args, **kargs):
        node_id = str(request.query_params.get("node", ""))
        try:
            service = ModelManagerService(request)
            result = service.getNodeInputs(node_id)
            return Response(result)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, description="Node ID")
    ]))
    def getNodeOutputs(request, *args, **kargs):
        node_id = str(request.query_params.get("node", ""))
        try:
            service = ModelManagerService(request)
            result = service.getNodeOutputs(node_id)
            return Response(result)
        except Exception as ex:
            raise exceptions.NotFound(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("text", required=True, location="query",
                      description="Text to search"),
        coreapi.Field("nodeClass", required=True,
                      location="query", description="Node Class"),
        coreapi.Field("moduleId", required=True,
                      location="query", description="Module ID"),
        coreapi.Field("fillDetail", required=True,
                      location="query", description="Fill Detail"),
        coreapi.Field("extraClasses", required=True,
                      location="body", description="Extra Classes"),
    ]))
    def searchNodes(request, *args, **kargs):
        text = str(request.query_params.get("text", ""))
        module_id = request.query_params.get("moduleId", None)
        node_class = request.query_params.get("nodeClass", None)
        fill_detail = request.query_params.get("fillDetail", None)
        extra_classes = request.data.get("extraClasses", [])

        try:
            service = ModelManagerService(request)
            result = service.searchNodes(
                text, module_id, node_class, extra_classes, fill_detail)
            response = NodeSearchResultSerializer(result, many=True)
            return Response(response.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("text", required=True, description="Text to search")
    ]))
    def searchForAutocomplete(request, *args, **kargs):
        text = str(request.query_params.get("text", ""))
        try:
            service = ModelManagerService(request)
            result = service.searchForAutocomplete(text)
            response = NodeSearchResultSerializer(result, many=True)
            return Response(response.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True,
                      description="Node to evaluate and get preview")
    ]))
    def previewNode(request, *args, **kargs):
        node = str(request.data.get("node", ""))
        if node:
            service = ModelManagerService(request)
            result = service.previewNode(node)
            return Response(result)
        raise exceptions.NotAcceptable("Node not found")

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, description="Node properties")
    ]))
    def setNodesSize(request, *args, **kargs):
        serializer = NodesSizeAndPositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            service = ModelManagerService(request)
            result = service.setNodesSize(serializer.validated_data["values"])
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, description="Node properties")
    ]))
    def setNodesPosition(request, *args, **kargs):
        serializer = NodesSizeAndPositionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            service = ModelManagerService(request)
            result = service.setNodesPosition(
                serializer.validated_data["values"])
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=False,
                      location="query", description="Node ID")
    ]))
    def getNodeProfile(request, *args, **kargs):
        node_id = request.query_params.get("nodeId", None)
        service = ModelManagerService(request)
        result = service.getNodeProfile(node_id)
        if result:
            return Response(result)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True, location="query",
                      description="Node Object")
    ]))
    def createNode(request, *args, **kargs):
        serializer = NodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ModelManagerService(request)
        result = service.createNode(serializer.create(serializer.data))
        if result:
            return Response(result)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    @api_view(['DELETE'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True,
                      description="Array of nodes ids")
    ]))
    def deleteNodes(request, *args, **kargs):
        serializer = NodeIdentifierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ModelManagerService(request)
        try:
            result = service.deleteNodes(serializer.data["values"])
            if result:
                return Response(result)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True,
                      description="Array of nodes ids")
    ]))
    def createAlias(request, *args, **kargs):
        serializer = NodeIdentifierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ModelManagerService(request)
        try:
            result = service.createAlias(serializer.data["values"])
            if result:
                res = []
                if len(result) > 0:
                    for nodeId in result:
                        res.append({"id": nodeId})
                        # TODO: fillNodeProperties ? is comented in .net
                    return Response(res)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True,
                      description="Array of nodes ids")
    ]))
    def createInputNode(request, *args, **kargs):
        serializer = NodeIdentifierSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = ModelManagerService(request)
        try:
            result = service.createInputNode(serializer.data["values"])
            if result:
                res = []
                if len(result) > 0:
                    for nodeId in result:
                        res.append({"id": nodeId})
                    return Response(res)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    # TODO: Implement createOutputNode

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="query",
                      description="Array of Node Objects")
    ]))
    def copyNodes(request, *args, **kargs):
        if request.data is not None:
            if "values" in request.data:
                if len(request.data["values"]) > 0:
                    nodes = []
                    for node in request.data["values"]:
                        nodes.append(Node(**node))
                    service = ModelManagerService(request)
                    try:
                        result = service.copyNodes(nodes)
                        if result:
                            return Response(result)
                        else:
                            raise exceptions.NotAcceptable(
                                "Error on copy nodes")
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    except Exception as ex:
                        raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=True, location="query",
                      description="Id of the node to be copied"),
        coreapi.Field("asNewNode", required=True, location="query",
                      description="(True/False) if the node is copied as a new node")
    ]))
    def copyAsValues(request, *args, **kargs):
        serializer = CopyAsValuesParamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            service = ModelManagerService(request)
            result = service.copyAsValues(
                serializer.create(serializer.validated_data))
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="query",
                      description="Array of Node Objects")
    ]))
    def moveNodes(request, *args, **kargs):
        if request.data is not None:
            if "values" in request.data:
                if len(request.data["values"]) > 0:
                    nodes = []
                    for node in request.data["values"]:
                        nodes.append(Node(**node))
                    service = ModelManagerService(request)
                    try:
                        result = service.moveNodes(nodes)
                        if result:
                            return Response(result)
                        else:
                            raise exceptions.NotAcceptable(
                                "Error on move nodes")
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    except Exception as ex:
                        raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    def stop(request, *args, **kargs):
        try:
            service = ModelManagerService(request)
            result = service.stop()
            if result:
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("values", required=True, location="query",
                      description="Array of Node Objects")
    ]))
    def setNodeZ(request, *args, **kargs):
        if request.data is not None:
            if "values" in request.data:
                if len(request.data["values"]) > 0:
                    nodes = []
                    for node in request.data["values"]:
                        nodes.append(Node(**node))
                    service = ModelManagerService(request)
                    try:
                        result = service.setNodeZ(nodes)
                        if result:
                            return Response(status=status.HTTP_200_OK)
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                    except Exception as ex:
                        raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("value", required=True,
                      location="query", description="Node Id")
    ]))
    def setNodeIdFromTitle(request, *args, **kargs):
        if request.data is not None:
            if "value" in request.data:
                if len(request.data["value"]) > 0:
                    node_id = request.data["value"]
                    service = ModelManagerService(request)
                    try:
                        result = service.setNodeIdFromTitle(node_id)
                        if result:
                            return Response(result)
                        else:
                            raise exceptions.NotAcceptable(
                                "Error on setting the node id from the title")
                    except Exception as ex:
                        raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    def executeForRefresh(request, *args, **kargs):
        try:
            service = ModelManagerService(request)
            if service.executeForRefresh():
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=True,
                      location="query", description="Node Id"),
        coreapi.Field("fileFormat", required=True,
                      location="query", description="(csv or xls)"),
        coreapi.Field("numberFormat", required=True, location="query",
                      description="The format of the decimal point, etc ..."),
        coreapi.Field("columnFormat", required=True, location="query",
                      description="(tab,;,...) The format of the columns separator"),
        coreapi.Field("compressed", required=True, location="query",
                      description="(1/0) If the file needs to be compressed, if true then returns a file with the fileformat compressed on a .zip file"),
        coreapi.Field("nodeQuery", required=True, location="query",
                      description="The query for the node")
    ]))
    def exportFlatNode(request, *args, **kargs):
        serializer = ExportNodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            file_stream, file_name = service.exportFlatNode(
                serializer.create(serializer.validated_data))
            response = FileResponse(
                file_stream, as_attachment=True, filename=file_name)
            # content disposition to retrieve filename in the ui
            response['Access-Control-Allow-Headers'] = 'Content-Disposition'
            response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            return response
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=True,
                      location="query", description="Node Id"),
        coreapi.Field("fileFormat", required=True,
                      location="query", description="(csv or xls)"),
        coreapi.Field("numberFormat", required=True, location="query",
                      description="The format of the decimal point, etc ..."),
        coreapi.Field("columnFormat", required=True, location="query",
                      description="(tab,;,...) The format of the columns separator"),
        coreapi.Field("compressed", required=True, location="query",
                      description="(1/0) If the file needs to be compressed, if true then returns a file with the fileformat compressed on a .zip file"),
        coreapi.Field("nodeQuery", required=True, location="query",
                      description="The query for the node")
    ]))
    def exportCurrentNode(request, *args, **kargs):
        """
        Reminder: Pyplan Excel Addin uses this endpoint.
        """
        serializer = ExportNodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            dashboardManagerService = DashboardManagerService(request)
            objectExport = serializer.create(serializer.validated_data)
            file_stream, file_name = service.exportCurrentNode(
                objectExport, dashboardManagerService)
            response = FileResponse(
                file_stream, as_attachment=True, filename=file_name)
            # content disposition to retrieve filename in the ui
            response['Access-Control-Allow-Headers'] = 'Content-Disposition'
            response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            return response
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    # TODO: Método exportEntireNode en visual no esta siendo usado por la UI.
    # tiene un comentario en visual que dice implementar tal cual ADE

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("moduleId", required=True,
                      location="query", description="Module Id"),
        coreapi.Field("exportType", required=True, location="query",
                      description="(1/2) If 1 exports to the tmp folder, 2 exports to the current module folder")
    ]))
    def exportModuleToFile(request, *args, **kargs):
        serializer = ExportModuleToFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            file_stream, file_name = service.exportModuleToFile(
                serializer.create(serializer.validated_data))
            response = FileResponse(
                file_stream, as_attachment=True, filename=file_name)
            # content disposition to retrieve filename in the ui
            response['Access-Control-Allow-Headers'] = 'Content-Disposition'
            response['Access-Control-Expose-Headers'] = 'Content-Disposition'
            return response
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("ImportModuleData", required=True,
                      location="query", description="Object")
    ]))
    def importModuleFromFile(request, *args, **kargs):
        """
        Imports a module from a file
        """
        serializer = ImportModuleDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            res = ImportModuleDataSerializer(service.importModuleFromFile(
                serializer.create(serializer.validated_data)))
            return Response(res.data)
        except Exception as ex:
            raise exceptions.NotAcceptable(ex)

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("extension", required=False,
                      description="extension of the looked files")
    ]))
    @schema(AutoSchema(manual_fields=[]))
    def getFilesForImportWizard(request, *args, **kargs):
        """
        Get files for use in import wizard 
        """
        extension = str(request.query_params.get("extension", None))
        if extension:
            try:
                service = ModelManagerService(request)
                res = FileEntrySerializer(service.getFilesForImportWizard(
                    extension), many=True, context={'client_session': service.client_session})
                return Response(res.data)
            except Exception as ex:
                raise exceptions.NotAcceptable(
                    f"There was an error trying to getFilesForImportWizard: {str(ex)}")
        else:
            raise exceptions.NotAcceptable(
                "There was no file extension provided")

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("params", required=False,
                      description="Wizard Request Object")
    ]))
    def callWizard(request, *args, **kargs):
        serializer = WizardRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            return Response(service.callWizard(request.data))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error when trying to callWizard: {str(ex)}")

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=False,
                      description="Id of the node to be excecuted")
    ]))
    def executeButton(request, *args, **kargs):
        serializer = NodeIdSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            if service.executeButton(serializer.validated_data['nodeId']):
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in executeButton: {str(ex)}")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("nodeId", required=False,
                      description="Id of the node to be evaluated")
    ]))
    def isInBackground(request, *args, **kargs):
        try:
            node_id = request.query_params.get("nodeId", None)
            service = ModelManagerService(request)
            return Response(service.isInBackground(node_id))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in isInBackground: {str(ex)}")

    # helper functions

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("file", required=False, description="File Object")
    ]))
    @parser_classes((parsers.MultiPartParser, parsers.FormParser,))
    def uploadFileToTemp(request, *args, **kargs):
        """
        uploads single file to temp
        """
        serializer = UploadFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            service = ModelManagerService(request)
            res = service.uploadFile(
                serializer.data.get("action"),
                request.FILES["files"],
                serializer.data.get("folder_path"),
                serializer.data.get("name"),
                serializer.data.get("chunk")
            )
            return Response(res)
        except Exception as ex:
            raise exceptions.NotFound(
                f"There was an error when trying to upload the file: {str(ex)}")

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field("node", required=True,
                      description="Node to evaluate and get selector definition")
    ]))
    def getSelector(request, *args, **kargs):
        node = str(request.data.get("node", ""))
        if node:
            service = ModelManagerService(request)
            result = service.getSelector(node)
            return Response(result)
        raise exceptions.NotAcceptable("Node not found")

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field('lib', required=True, location='form',
                      type='string', description='Library to install'),
    ]))
    def installLibrary(request, *args, **kargs):
        """Install python library"""
        try:
            _lib = request.data.get('lib')
            service = ModelManagerService(request)
            return Response(service.installLibrary(_lib))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in installLibrary: {str(ex)}")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    def listInstalledLibraries(request, *args, **kargs):
        """List python installed libraries"""
        try:
            service = ModelManagerService(request)
            response = service.listInstalledLibraries()
            return Response(response)
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error listing installed libraries: {str(ex)}")

    @staticmethod
    @api_view(['DELETE'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field('lib', required=True, location='form',
                      type='string', description='Library to uninstall'),
    ]))
    def uninstallLibrary(request, *args, **kargs):
        """Uninstall python library"""
        try:
            _lib = request.data.get('lib')
            _target = request.data.get('target')
            service = ModelManagerService(request)
            return Response(service.uninstallLibrary(_lib, _target))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in uninstallLibrary: {str(ex)}")

    @staticmethod
    @api_view(['GET'])
    @permission_classes((permissions.IsAuthenticated,))
    @schema(AutoSchema(manual_fields=[
        coreapi.Field('from_line', required=True, location='form', type='string',
                      description='Get install progress from this line')
    ]))
    def getInstallProgress(request, *args, **kargs):
        """Get current install progress"""
        try:
            from_line = request.query_params.get("from_line", None)
            service = ModelManagerService(request)
            return Response(service.getInstallProgress(from_line))
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in getInstallProgress: {str(ex)}")
