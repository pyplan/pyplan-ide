import coreapi
import jsonpickle
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema, ManualSchema

from pyplan_engine.classes.Model import Model
from pyplan_engine.engines import engines
from pyplan_engine.utils.exception_handler import genericApiException

from .serializers import IndexValuesReqSerializer


def manageNoEngine():
    return Response('Your engine is not found. Please close all sessions and login again', status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field("modelFile", required=True, location="form",
                  type="string", description="Model filename"),
    coreapi.Field("modelName", required=True, location="form",
                  type="string", description="Model name"),
]))
def createNewModel(request, uid):
    """Create and open new model"""
    try:
        _modelFile = request.data.get("modelFile")
        _modelName = request.data.get("modelName")
        if uid in engines:
            engines[uid].initializeModel(_modelFile)
            engines[uid].model.createNewModel(_modelFile, _modelName)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field("filename", required=True, location="form",
                  type="string", description="Model filename"),
]))
def openModel(request, uid):
    """Open model from file system"""
    try:
        _fileName = request.data.get("filename")
        if uid in engines:
            engines[uid].initializeModel(_fileName)
            engines[uid].model.openModel(_fileName)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
def closeModel(request, uid):
    """Close the current model"""
    try:
        if uid in engines:
            engines[uid].model.closeModel()
        # no throw error if engine not exists
        return HttpResponse("ok")
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('filename', required=True, location='form',
                  type='string', description='Filename to save'),
]))
def saveModel(request, uid):
    """Save the current Model"""
    try:
        if uid in engines:
            _fileName = request.data.get('filename')
            engines[uid].model.saveModel(_fileName)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('company_code', required=True, location='form',
                  type='string', description='Company Code'),
    coreapi.Field('session_key', required=True, location='form',
                  type='string', description='Session Key'),
]))
def connectToWS(request, uid):
    """Connect to WS"""
    try:
        if uid in engines:
            company_code = request.data.get('company_code')
            session_key = request.data.get('session_key')
            engines[uid].model.connectToWS(company_code, session_key)
            return Response()
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description='ModuleId to export'),
    coreapi.Field('filename', required=True, location='form',
                  type='string', description='Filename to save'),
]))
def exportModule(request, uid):
    """Export module to file"""
    try:
        _moduleId = request.data.get('moduleId')
        _filename = request.data.get('filename')
        if uid in engines:
            if engines[uid].model.exportModule(_moduleId, _filename):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description='ModuleId import to'),
    coreapi.Field('filename', required=True, location='form',
                  type='string', description='Filename to save'),
    coreapi.Field('importType', required=True, location='form',
                  type='string', description='Import type'),
]))
def importModule(request, uid):
    """Import module from file"""
    try:
        if uid in engines:
            _moduleId = request.data.get('moduleId')
            _filename = request.data.get('filename')
            _importType = request.data.get('importType')
            if engines[uid].model.importModule(_moduleId, _filename, _importType):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description='Module for get diagram info'),
]))
def getDiagram(request, uid):
    """Get diagram for moduleId"""
    try:
        _moduleId = request.data.get('moduleId')
        if uid in engines:
            return JsonResponse(engines[uid].model.getDiagram(_moduleId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description='Module for get diagram info'),
]))
def getBreadcrumb(request, uid):
    """Get breadcrumb for a moduleId"""
    try:
        _moduleId = request.data.get('moduleId')
        if uid in engines:
            return JsonResponse(engines[uid].model.getBreadcrumb(_moduleId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('obj', required=True, location='form',
                  type='string', description='Properties to get values'),
]))
def getModelProperties(request, uid):
    """Get model properties"""
    try:
        if uid in engines:
            return JsonResponse(engines[uid].model.getModelProperties(), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('obj', required=True, location='form',
                  type='string', description='Model property object'),
]))
def setModelProperties(request, uid):
    """Set model  properties
            [
                {
                    "name":"sumtype", "value":"1+1"
                }
            ]
        """
    try:
        if uid in engines:
            _obj = jsonpickle.decode(request.data.get('obj'))
            engines[uid].model.setModelProperties(_obj)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='moduleId for get arrows'),
]))
def getArrows(request, uid):
    """Get arrows of the module"""
    try:
        _nodeId = request.data.get('nodeId')
        if uid in engines:
            return JsonResponse(engines[uid].model.getArrows(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('obj', required=True, location='form',
                  type='string', description='Node properties object'),
]))
def getNodeProperties(request, uid):
    """Get node properties
            {
                "node":"nodeId",
                "properties":[
                                {
                                    "name":"identifier"
                                }
                            ]
            }
        """
    try:
        if uid in engines:
            _obj = jsonpickle.decode(request.data.get('obj'))
            return JsonResponse(engines[uid].model.getNodeProperties(_obj), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('obj', required=True, location='form',
                  type='string', description='Node properties object'),
]))
def setNodeProperties(request, uid):
    """Set node properties
            {
                "node":"nodeId",
                "properties":[
                                {
                                    "name":"identifier",
                                    "value":"newId"
                                }
                            ]
            }
        """
    try:
        if uid in engines:
            _obj = jsonpickle.decode(request.data.get('obj'))
            engines[uid].model.setNodeProperties(
                _obj["node"], _obj["properties"])
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId for check if exist'),
]))
def existNode(request, uid):
    """Return 1 if node exists"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            if engines[uid].model.existNode(_nodeId):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId for check if exist in moduleId'),
    coreapi.Field('modulesId', required=True, location='form',
                  type='list of string', description=''),
]))
def isChild(request, uid):
    """Return 1 if node exists in moduleId or your parents"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _modulesId = _nodeList = jsonpickle.decode(
                request.data.get('modulesId'))
            if engines[uid].model.isChild(_nodeId, _modulesId):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='Nodeid for get inputs'),
]))
def getInputs(request, uid):
    """Return inputs of a node"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return JsonResponse(engines[uid].model.getInputs(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='Nodeid for get outputs'),
]))
def getOutputs(request, uid):
    """Return outputs of a node"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return JsonResponse(engines[uid].model.getOutputs(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
]))
def getDefinition(request, uid):
    """Get node definition"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _node = engines[uid].model.getNode(_nodeId)
            return HttpResponse(_node.definition)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
]))
def invalidateNode(request, uid):
    """Invalidate node result"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _node = engines[uid].model.getNode(_nodeId)
            if not _node is None:
                _node.invalidate()
                return HttpResponse("ok")
            return HttpResponse("")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId for preview result'),
]))
def previewNode(request, uid):
    """Preview evaluante node"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            engines[uid].stoppable = True
            _res = engines[uid].model.previewNode(_nodeId)
            if _res is None:
                return HttpResponse('', status=204)
            return HttpResponse(_res)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e, engines[uid])
    finally:
        engines[uid].stoppable = False


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('filterOptions', required=True, location='form',
                  type='string', description='FilterOptions object'),
]))
def searchNodes(request, uid):
    """Search nodes using filterOptions
            {
                "text":"text to search in Identifier and Title",
                "nodeClass":"filter only this class"
                "extraClasses": ["other class","other other class"]
                "moduleId": "only in this module"
                "excludeAlias": false
            }
        """
    try:
        if uid in engines:
            _filterOptions = jsonpickle.decode(
                request.data.get('filterOptions'))
            return JsonResponse(engines[uid].model.searchNodes(_filterOptions), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='nodeId for get profile'),
]))
def profilenode(request, uid):
    """Returns the times of each node calculation used to get the result of this node"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return HttpResponse(engines[uid].model.profileNode(_nodeId))
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('definition', required=True, location='form',
                  type='string', description='definition')
]))
def evaluate(request, uid):
    """Evaluate a definition and return the result"""
    try:
        if uid in engines:
            definition = request.data.get('definition')
            engines[uid].stoppable = True
            _res = engines[uid].model.evaluate(definition)
            if _res is None:
                return HttpResponse('', status=204)
            return JsonResponse(_res, safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e, engines[uid])
    finally:
        engines[uid].stoppable = False


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId'),
    coreapi.Field('params', required=False, location='form',
                  type='string', description='Json with function params'),
]))
def callFunction(request, uid):
    """Call node function and return the result"""
    try:
        if uid in engines:
            nodeId = request.data.get('nodeId')
            params = request.data.get('params')
            if not params is None:
                params = jsonpickle.decode(params)
            engines[uid].stoppable = True
            _res = engines[uid].model.callFunction(nodeId, params)
            if _res is None:
                return HttpResponse('', status=204)
            return JsonResponse(_res, safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e, engines[uid])
    finally:
        engines[uid].stoppable = False


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId'),
]))
def evaluateNode(request, uid):
    """Evaluate node """
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _dims = None
            _rows = None
            _columns = None
            _summaryBy = 'sum'
            _bottomTotal = False
            _rightTotal = False
            _fromRow = 0
            _toRow = 0
            _resultType = request.data.get('resultType', '')

            if not request.data.get('dims') is None:
                _dims = jsonpickle.decode(request.data.get('dims'))
            if not request.data.get('rows') is None:
                _rows = jsonpickle.decode(request.data.get('rows'))
            if not request.data.get('columns') is None:
                _columns = jsonpickle.decode(request.data.get('columns'))
            if not request.data.get('summaryBy') is None:
                _summaryBy = request.data.get('summaryBy')
            if not request.data.get('bottomTotal') is None:
                _bottomTotal = str(request.data.get(
                    'bottomTotal')).lower() == 'true'
            if not request.data.get('rightTotal') is None:
                _rightTotal = str(request.data.get(
                    'rightTotal')).lower() == 'true'
            if not request.data.get('fromRow') is None:
                _fromRow = request.data.get('fromRow')
            if not request.data.get('toRow') is None:
                _toRow = request.data.get('toRow')
            engines[uid].stoppable = True
            _res = engines[uid].model.evaluateNode(
                _nodeId, _dims, _rows, _columns, _summaryBy, _bottomTotal, _rightTotal, _fromRow, _toRow, _resultType)
            if _res is None:
                return HttpResponse('', status=204)
            return HttpResponse(_res)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e, engines[uid])
    finally:
        engines[uid].stoppable = False


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
]))
def executeButton(request, uid):
    """Execute a button node."""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return JsonResponse(engines[uid].model.executeButton(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='nodeId for get indexes'),
]))
def getIndexes(request, uid):
    """Get array of node indexes"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return JsonResponse(engines[uid].model.getIndexes(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='nodeId for get indexes'),
]))
def getIndexesWithLevels(request, uid):
    """Get array of node indexes"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return JsonResponse(engines[uid].model.getIndexesWithLevels(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='nodeId for check if is table '),
]))
def isTable(request, uid):
    """Return 1 if the node is editable table"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            return HttpResponse(engines[uid].model.isTable(_nodeId))
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('indexId', required=True, location='form',
                  type='string', description='Used on pandas'),
]))
def getIndexType(request, uid):
    """Return type of index"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _indexId = request.data.get('indexId')
            return JsonResponse(engines[uid].model.getIndexType(_nodeId, _indexId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('indexId', required=True, location='form',
                  type='string', description='Used on pandas'),
]))
def getIndexValues(request, uid):
    """Return list of values of the index"""
    paginator = PageNumberPagination()
    paginator.page_size = 1000
    try:
        if uid in engines:
            serialized_rq = IndexValuesReqSerializer(
                data=request.data)
            serialized_rq.is_valid(raise_exception=True)

            query_set = engines[uid].model.getIndexValues(
                serialized_rq.create(serialized_rq.validated_data))
            context = paginator.paginate_queryset(query_set, request)

            return paginator.get_paginated_response(context)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('changes', required=True, location='form',
                  type='string', description=''),
]))
def setNodeValueChanges(request, uid):
    """Set changes of values of a node """
    try:
        if uid in engines:
            _changes = jsonpickle.decode(request.data.get('changes'))
            engines[uid].model.setNodeValueChanges(_changes)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeList', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description=''),
]))
def moveNodes(request, uid):
    """Move nodes to other parent"""
    try:
        if uid in engines:
            _nodeList = jsonpickle.decode(request.data.get('nodeList'))
            _moduleId = request.data.get('moduleId')
            return JsonResponse(engines[uid].model.moveNodes(_nodeList, _moduleId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeList', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description=''),
]))
def copyNodes(request, uid):
    """Copy nodes to other parent"""
    try:
        if uid in engines:
            _nodeList = jsonpickle.decode(request.data.get('nodeList'))
            _moduleId = request.data.get('moduleId')
            return JsonResponse(engines[uid].model.copyNodes(_nodeList, _moduleId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('asNewNode', required=False, location='form',
                  type='string', description=''),
]))
def copyAsValues(request, uid):
    """Copy values of node to current nodeo or to new node"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId', '')
            _asNewNode = request.data.get('asNewNode', 'True') == 'True'
            return JsonResponse(engines[uid].model.copyAsValues(_nodeId, _asNewNode), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='')
]))
def setNodeIdFromTitle(request, uid):
    """Generate Node identifier from node title"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId', '')
            return JsonResponse(engines[uid].model.setNodeIdFromTitle(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeList', required=True, location='form',
                  type='string', description=''),
]))
def createInputNodes(request, uid):
    """Create input node for each node in the param nodelist"""
    try:
        if uid in engines:
            _nodeList = jsonpickle.decode(request.data.get('nodeList'))
            return JsonResponse(engines[uid].model.createInputNodes(_nodeList), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeList', required=True, location='form',
                  type='string', description=''),
]))
def createAlias(request, uid):
    """Create alias node for each node in the param nodelist"""
    try:
        if uid in engines:
            _nodeList = jsonpickle.decode(request.data.get('nodeList'))
            return JsonResponse(engines[uid].model.createAlias(_nodeList), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeClass', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('moduleId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('x', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('y', required=True, location='form',
                  type='string', description=''),
]))
def createNode(request, uid):
    """Create new node"""
    try:
        if uid in engines:
            _nodeClass = request.data.get('nodeClass')
            _moduleId = request.data.get('moduleId')
            _x = request.data.get('x')
            _y = request.data.get('y')
            _nodeObj = engines[uid].model.createNode(
                nodeClass=_nodeClass, moduleId=_moduleId, x=_x, y=_y, toObj=True)
            return JsonResponse(_nodeObj, safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('obj', required=True, location='form',
                  type='string', description=''),
]))
def deleteNodes(request, uid):
    """Delete nodes by ids """
    try:
        if uid in engines:
            _obj = jsonpickle.decode(request.data.get('obj'))
            engines[uid].model.deleteNodes(_obj)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
]))
def getCubeMetadata(request, uid):
    """Return metadadata for view node as cube"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _resultType = request.data.get('resultType', '')
            return JsonResponse(engines[uid].model.getCubeMetadata(_nodeId, _resultType), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('query', required=True, location='form',
                  type='string', description=''),
]))
def getCubeDimensionValues(request, uid):
    """Return data for cube dimension values"""
    try:
        if uid in engines:
            _query = jsonpickle.decode(request.data.get('query'))
            return JsonResponse(engines[uid].model.getCubeDimensionValues(_query), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('query', required=True, location='form',
                  type='string', description=''),
]))
def getCubeValues(request, uid):
    """Return data for cube browser"""
    try:
        if uid in engines:
            _query = jsonpickle.decode(request.data.get('query'))
            return JsonResponse(engines[uid].model.getCubeValues(_query), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeList', required=True, location='form',
                  type='string', description=''),
]))
def isCalcNodes(request, uid):
    """Return array of True,False for each node if this is calculated"""
    try:
        if uid in engines:
            _nodeList = jsonpickle.decode(request.data.get('nodeList'))
            return JsonResponse(engines[uid].model.isCalcNodes(_nodeList), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('numberFormat', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('columnFormat', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('fileName', required=True, location='form',
                  type='string', description=''),
]))
def exportFlatNode(request, uid):
    """Export node as flat format"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _numberFormat = request.data.get('numberFormat')
            _columnFormat = request.data.get('columnFormat')
            _fileName = request.data.get('fileName')
            if engines[uid].model.exportFlatNode(_nodeId, _numberFormat, _columnFormat, _fileName):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('filename', required=True, location='form',
                  type='string', description='Filename to save'),
]))
def dumpNodeToFile(request, uid):
    """Dump node definition to file"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _fileName = request.data.get('filename')
            engines[uid].model.dumpNodeToFile(_nodeId, _fileName)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('scenarioData', required=True, location='form',
                  type='string', description=''),
]))
def loadScenario(request, uid):
    """Load scenario into model"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            _scenarioData = request.data.get('scenarioData')
            engines[uid].model.loadScenario(_nodeId, _scenarioData)
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
def unloadScenario(request, uid):
    """Unload all scenarios """
    try:
        if uid in engines:
            engines[uid].model.unloadScenario()
            return HttpResponse("ok")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId'),
    coreapi.Field('rowIndex', required=True, location='form',
                  type='string', description=''),
    coreapi.Field('attIndex', required=True, location='form',
                  type='string', description=''),
]))
def geoUnclusterData(request, uid):
    """Get diagram for moduleId"""
    try:
        nodeId = request.data.get('nodeId')
        rowIndex = request.data.get('rowIndex')
        attIndex = request.data.get('attIndex')
        latField = "latitude"
        if request.data.get('latField'):
            latField = request.data.get('latField')
        lngField = "longitude"
        if request.data.get('lngField'):
            lngField = request.data.get('lngField')
        geoField = "geoField"
        if request.data.get('geoField'):
            geoField = request.data.get('geoField')
        labelField = "labelField"
        if request.data.get('labelField'):
            labelField = request.data.get('labelField')
        sizeField = "sizeField"
        if request.data.get('sizeField'):
            sizeField = request.data.get('sizeField')
        colorField = "colorField"
        if request.data.get('colorField'):
            colorField = request.data.get('colorField')
        iconField = "iconField"
        if request.data.get('geoFiiconFieldeld'):
            iconField = request.data.get('iconField')
        if uid in engines:
            return JsonResponse(engines[uid].model.geoUnclusterData(nodeId, rowIndex, attIndex, latField, lngField, geoField, labelField, sizeField, colorField, iconField), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['GET'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('extraPath', required=True, location='form',
                  type='string', description='')
]))
def getToolbars(request, uid):
    """Return list of default app toolbars"""
    try:
        extraPath = request.data.get('extraPath', '')
        if uid in engines:
            return JsonResponse(engines[uid].model.getToolbars(extraPath), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('params', required=True, location='form',
                  type='string', description='')
]))
def callWizard(request, uid):
    """Call toolbar wizard"""
    try:
        params = request.data.get('params', '')
        if uid in engines:
            return JsonResponse(engines[uid].model.callWizard(params), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId for check if is Selector')
]))
def isSelector(request, uid):
    """Return 1 if node exists and is Selector"""
    try:
        if uid in engines:
            _nodeId = request.data.get('nodeId')
            if engines[uid].model.isSelector(_nodeId):
                return HttpResponse("1")
            return HttpResponse("0")
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('nodeId', required=True, location='form',
                  type='string', description='NodeId for get selector data')
]))
def getSelector(request, uid):
    """Return selector data"""
    try:
        _nodeId = request.data.get('nodeId')
        if uid in engines:
            return JsonResponse(engines[uid].model.getSelector(_nodeId), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['GET'])
@schema(AutoSchema(manual_fields=[]))
def getPID(request, uid):
    """Return PID of current model"""
    try:
        if uid in engines:
            return JsonResponse(engines[uid].model.getPID(), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['GET'])
@schema(AutoSchema(manual_fields=[]))
def getSystemResources(request, uid):
    """Return current system resources"""
    try:
        if uid in engines:
            return JsonResponse(engines[uid].model.getSystemResources(), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('lib', required=True, location='form',
                  type='string', description='Library to install'),
    coreapi.Field('target', required=True, location='form',
                  type='string', description='Target instalation')
]))
def installLibrary(request, uid):
    """Install python library"""
    try:
        _lib = request.data.get('lib')
        _target = request.data.get('target')
        if uid in engines:
            return JsonResponse(engines[uid].model.installLibrary(_lib, _target), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['GET'])
def listInstalledLibraries(request, uid):
    """List python installed libraries"""
    try:
        if uid in engines:
            return JsonResponse(engines[uid].model.listInstalledLibraries(), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['POST'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('lib', required=True, location='form',
                  type='string', description='Library to uninstall'),
    coreapi.Field('target', required=True, location='form',
                  type='string', description='Target instalation')
]))
def uninstallLibrary(request, uid):
    """Uninstall python library"""
    try:
        _lib = request.data.get('lib')
        _target = request.data.get('target')
        if uid in engines:
            return JsonResponse(engines[uid].model.uninstallLibrary(_lib, _target), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)


@api_view(['GET'])
@schema(AutoSchema(manual_fields=[
    coreapi.Field('from_line', required=True, location='form',
                  type='string', description='Get install progress from this line')
]))
def getInstallProgress(request, uid):
    """Get current install progress"""
    try:
        if uid in engines:
            from_line = request.data.get('from_line', '0')
            return JsonResponse(engines[uid].model.getInstallProgress(from_line), safe=False)
        return manageNoEngine()
    except Exception as e:
        return genericApiException(e)
