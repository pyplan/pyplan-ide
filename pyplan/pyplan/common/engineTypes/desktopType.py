import json
import os

from django.conf import settings
from django.contrib.sessions.models import Session
from rest_framework import exceptions

from pyplan.pyplan.common.classes.eNodeProperty import eNodeProperty
from pyplan.pyplan.common.engineTypes.engineType import IEngineType
from pyplan.pyplan.modelmanager.classes.modelInfo import ModelInfo
from pyplan_engine.classes.CalcEngine import CalcEngine

from .serializers import IndexValuesReqSerializer


class DesktopType(IEngineType):

    calcEngine = None

    def __init__(self, clientSession):

        if DesktopType.calcEngine is None:
            self.currentSession = clientSession
            self.createEngine(clientSession)

    def createEngine(self, clientSession):
        """ Create a new engine endpoint"""
        DesktopType.calcEngine = CalcEngine()
        DesktopType.calcEngine.initializeModel()
        if not clientSession is None and not clientSession.modelInfo is None and clientSession.modelInfo.uri:
            file_path = os.path.join(
                settings.MEDIA_ROOT, "models", clientSession.modelInfo.uri)
            self.openModel(file_path)
        print(f"Calcengine pid: {DesktopType.calcEngine.pid}")

    def releaseEngine(self):
        if not DesktopType.calcEngine is None:
            DesktopType.calcEngine.release()
        DesktopType.calcEngine = None

    def openModel(self, file):
        """Open model"""
        result = DesktopType.calcEngine.model.openModel(file)
        if result:
            self.setInfoToModel()
        return result

    def setInfoToModel(self):
        """Set current session info to model"""
        if not self.currentSession is None:
            user_dic = dict()
            user_dic["companyId"] = self.currentSession.companyId
            user_dic["companyName"] = self.currentSession.companyName
            user_dic["companyCode"] = self.currentSession.company_code
            user_dic["userCompanyId"] = self.currentSession.userCompanyId
            user_dic["userId"] = str(self.currentSession.userId)
            user_dic["userFullName"] = self.currentSession.userFullName
            user_dic["session_key"] = str(self.currentSession.session_key)
            user_dic["departments"] = self.currentSession.departments
            self.setNodeProperties(
                "pyplan_user", [{"name": "definition", "value": f"result = {json.dumps(user_dic)}"}])
            # Connect to WS
            self.connectToWS(self.currentSession.company_code, self.currentSession.session_key)

    def connectToWS(self, company_code: str = None, session_key: str = None):
        """Connect to WebSocket"""
        if company_code and session_key:
            response = DesktopType.calcEngine.model.connectToWS(
                company_code, session_key)
            return response.status_code is 200
        return None

    def getModelName(self):
        """Return model name"""
        res_obj = self.getModelPreferences()
        if res_obj and "title" in res_obj and res_obj["title"]:
            return res_obj["title"]
        return ""

    def getModelId(self):
        """Return current model identifier"""
        res_obj = self.getModelPreferences()
        if res_obj and "identifier" in res_obj and res_obj["identifier"]:
            return res_obj["identifier"]
        return ""

    def getModelPreferences(self):
        """Get model preferences"""
        return DesktopType.calcEngine.model.getModelProperties()

    def connectToWS(self, company_code: str = None, session_key: str = None):
        """Connect to WebSocket"""
        return DesktopType.calcEngine.model.connectToWS(company_code, session_key)

    def getDiagram(self, module_id=None):
        """Get diagram"""
        return DesktopType.calcEngine.model.getDiagram(module_id)

    def isChild(self, node: str, module_ids: list = []):
        """Returns True if node is child of any module in list"""

        return DesktopType.calcEngine.model.isChild(node, module_ids)

    def getArrows(self, module_id=None):
        """Get arrows"""
        return DesktopType.calcEngine.model.getArrows(module_id)

    def stop(self):
        """Try to stop the current process"""
        try:
            DesktopType.calcEngine.stop()
            return True
        except Exception as ex:
            return False

    def getEngineURI(self):
        """Return current engineURI"""
        return self.engineURI

    def getEngineUID(self):
        """Return current engineUID"""
        return self.engineUID

    def getEngineParams(self):
        """Return current engineParams"""
        return self.engineParams

    def getNodeProperty(self, node_id, property_name):
        """Get node property"""
        return self.getNodeProperties(node_id, [{"name": property_name}])["properties"][0]["value"]

    def getNodeProperties(self, node_id, properties):
        """Get node properties"""
        return DesktopType.calcEngine.model.getNodeProperties({"node": node_id, "properties": properties})

    def setNodeProperties(self, node_id, properties):
        """Set node properties"""
        DesktopType.calcEngine.model.setNodeProperties(node_id, properties)
        return True

    def saveModel(self, file_path):
        """Save Model"""
        DesktopType.calcEngine.model.saveModel(file_path)
        return True

    def getNodeInputs(self, node_id):
        """Get node inputs"""
        return DesktopType.calcEngine.model.getInputs(node_id)

    def getNodeOutputs(self, node_id):
        """Get node outputs"""
        return DesktopType.calcEngine.model.getOutputs(node_id)

    def searchNodes(self, text, module_id, node_class, extra_classes, fill_detail):
        """Search Nodes"""
        return DesktopType.calcEngine.model.searchNodes({
            "text": text,
            "moduleId": module_id,
            "nodeClass": node_class,
            "extraClasses": extra_classes,
            "fillDetail": fill_detail
        })

    def setModelProperties(self, modelProperties):
        """Set model properties"""
        DesktopType.calcEngine.model.setModelProperties(modelProperties)
        return True

    def closeModel(self):
        """Close current model"""
        try:
            DesktopType.calcEngine.model.closeModel()
        except Exception as ex:
            print(f"Error on close model: {str(ex)}")
        return True

    def previewNode(self, node):
        """Evaluate and return node result preview"""
        return DesktopType.calcEngine.model.previewNode(node)

    def evaluate(self, definition):
        """Evaluate a definition and return result"""

        response = DesktopType.calcEngine.model.evaluate(definition)
        if isinstance(response, dict):
            return response
        else:
            return {"data": f"{response}"}

    def callFunction(self, nodeId, params):
        """Call function node and return result"""
        response = DesktopType.calcEngine.model.callFunction(nodeId, params)
        if isinstance(response, dict):
            return response
        else:
            return {"data": f"{response}"}

    def evaluateNode(
            self, node_id, dims, rows, columns, summary_by="sum",
            from_row=0, to_row=0, bottom_total=False, right_total=False
    ):

        response = DesktopType.calcEngine.model.evaluateNode(
            node_id, dims, rows, columns, summary_by, bottom_total, right_total, from_row, to_row)

        try:
            return json.loads(response)
        except:
            try:
                return {
                    "result": {
                        "indexValues": None,
                        "columns": {
                            "name": None,
                            "categories": ["Total"],
                        },
                        "index": ["Total"],
                        "data": [f"{response}"],
                        "nodeProperties": {
                            "hasDescription": False,
                            "hasWorkflowTask": False,
                        },
                        "newDims": [],
                        "indexOnRow": None,
                        "indexOnColumn": None,
                        "pageInfo": None,
                    }
                }
            except Exception as e:
                raise exceptions.NotAcceptable(e)

    def getIndexType(self, id):
        index_id = id
        node_id = ""
        if "." in id:
            index_id = id.split(".")[0]
            node_id = id.split(".")[1]
        return DesktopType.calcEngine.model.getIndexType(node_id, index_id)

    def getIndexValues(self, data):
        """
        Retrieves index values from engine.
        Warning!: Paginated response.
        """
        index_id = data['id']
        node_id = ''

        if '.' in data['id']:
            index_id, node_id = data['id'].split('.')

        page = ''
        if 'page' in data:
            page = f"?page={data['page']}"

        content = {
            'node_id': node_id,
            'index_id': index_id,
        }
        if 'filter' in data:
            content['filter'] = data['filter']
        if 'text1' in data:
            content['text1'] = data['text1']
        if 'text2' in data:
            content['text2'] = data['text2']

        serialized_rq = IndexValuesReqSerializer(
            data=content)
        serialized_rq.is_valid(raise_exception=True)

        query_set = DesktopType.calcEngine.model.getIndexValues(
            serialized_rq.create(serialized_rq.validated_data))

        return query_set

    def isResultComputed(self, nodes):
        return DesktopType.calcEngine.model.isCalcNodes(nodes)

    def getNodeIndexes(self, node_id):
        return DesktopType.calcEngine.model.getIndexesWithLevels(node_id)

    def isChoice(self, node_id):
        definition = self.getNodeProperty(
            node_id, eNodeProperty.DEFINITION.value)
        return (not definition is None or not definition == "") and "choice(" in definition

    def isSelector(self, node_id):
        return DesktopType.calcEngine.model.isSelector(node_id)

    def getSelector(self, node_id):
        return DesktopType.calcEngine.model.getSelector(node_id)

    def isIndex(self, node_id):
        node_class = self.getNodeProperty(node_id, eNodeProperty.CLASS.value)
        return (not node_class is None or not node_class == "") and node_class == "index"

    def isTable(self, node_id):
        return DesktopType.calcEngine.model.isTable(node_id) == '1'

    def isTime(self, field):
        time_indexes = ["time", "tiempo", "_time", ".timeframe"]
        for time_index in time_indexes:
            if time_index in field.lower():
                return True
        return False

    def getToolbars(self, extra_path):
        return DesktopType.calcEngine.model.getToolbars(extra_path)

    def profileNode(self, node_id):
        return DesktopType.calcEngine.model.profileNode(node_id)

    def createNode(self, node):
        return DesktopType.calcEngine.model.createNode(nodeClass=node.nodeClass, moduleId=node.moduleId, x=node.x - 50, y=node.y - 25, toObj=True)

    def deleteNodes(self, node_ids):
        DesktopType.calcEngine.model.deleteNodes(node_ids)
        return True

    def createAlias(self, node_ids):
        return DesktopType.calcEngine.model.createAlias(node_ids)

    def createInputNode(self, node_ids):
        return DesktopType.calcEngine.model.createInputNodes(node_ids)

    def copyNodes(self, nodes):
        """copy nodes to module"""
        node_ids = []
        for node in nodes:
            node_ids.append(node.id)
        result = DesktopType.calcEngine.model.copyNodes(
            node_ids, nodes[0].moduleId)
        return ",".join(result)

    def copyAsValues(self, params):
        """copy nodes to module"""
        return DesktopType.calcEngine.model.copyAsValues(params.nodeId, True if params.asNewNode else False)

    def moveNodes(self, nodes):
        """move nodes to another module"""
        node_ids = []
        for node in nodes:
            node_ids.append(node.id)
        result = DesktopType.calcEngine.model.moveNodes(
            node_ids, nodes[0].moduleId)
        return ",".join(result)

    def createNewModel(self, modelFile, modelName):
        """Creates a new model"""
        try:
            DesktopType.calcEngine.model.createNewModel(modelFile, modelName)
            return True
        except Exception as ex:
            print(f'Error creating a new model: {str(ex)}')
            return False

    def existNode(self, nodeId):
        """Checks for node existence"""
        return DesktopType.calcEngine.model.existNode(nodeId)

    def setNodeIdFromTitle(self, node_id):
        return DesktopType.calcEngine.model.setNodeIdFromTitle(node_id)

    def exportFlatNode(self, nodeId, numberFormat, columnFormat, fileName):
        """Exports a node"""
        return DesktopType.calcEngine.model.exportFlatNode(nodeId, numberFormat, columnFormat, fileName)

    def exportModule(self, moduleId, filename):
        """Exports a module"""
        return DesktopType.calcEngine.model.exportModule(moduleId, filename)

    def importModule(self, moduleId, filename, importType):
        """Imports a module"""
        return DesktopType.calcEngine.model.importModule(moduleId, filename, importType)

    def callWizard(self, wizardRequest):
        """Imports a module"""
        return DesktopType.calcEngine.model.callWizard(json.dumps(wizardRequest))

    # Pivot
    def getCubeMetadata(self, query):
        return DesktopType.calcEngine.model.getCubeMetadata(query["cube"])

    def getCubeValues(self, query):
        return DesktopType.calcEngine.model.getCubeValues(query)

    def setNodeValueChanges(self, changes):
        DesktopType.calcEngine.model.setNodeValueChanges(changes)
        return True

    def getCubeDimensionValues(self, query):
        return DesktopType.calcEngine.model.getCubeDimensionValues(query)

    def getUnclusterData(self, query):
        return DesktopType.calcEngine.model.geoUnclusterData(query.node, query.rowIndex, query.attIndex, query.latField, query.lngField, query.geoField, query.labelField, query.sizeField, query.colorField, query.iconField)

    def executeButton(self, nodeId):
        return DesktopType.calcEngine.model.executeButton(nodeId)

    def is_healthy(self):
        try:
            return DesktopType.calcEngine.model.getPID()
            return True
        except:
            return False

    def getSystemResources(self):
        """ Return container system resources"""
        return DesktopType.calcEngine.model.getSystemResources()

    def installLibrary(self, lib, target):
        """Install python library"""
        return DesktopType.calcEngine.model.installLibrary(lib, target)

    def listInstalledLibraries(self):
        """List python installed libraries"""
        return json.loads(DesktopType.calcEngine.model.listInstalledLibraries())

    def uninstallLibrary(self, lib, target):
        """Uninstall python library"""
        return DesktopType.calcEngine.model.uninstallLibrary(lib, target)

    def getInstallProgress(self, from_line):
        """Get install python library progress"""
        return DesktopType.calcEngine.model.getInstallProgress(from_line)
