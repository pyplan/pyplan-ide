from abc import ABC, abstractmethod


class IEngineType(ABC):

    from_app_pool = False
    engineParams = ""
    currentSession = None
    engineURI = ""
    engineUID = ""
    engineParams = ""
    lock = None

    @abstractmethod
    def createEngine(self): raise NotImplementedError

    @abstractmethod
    def releaseEngine(self): raise NotImplementedError

    @abstractmethod
    def stop(self): raise NotImplementedError

    @abstractmethod
    def getEngineURI(self): raise NotImplementedError

    @abstractmethod
    def getEngineUID(self): raise NotImplementedError

    @abstractmethod
    def getEngineParams(self): raise NotImplementedError

    @abstractmethod
    def openModel(self, file): raise NotImplementedError

    @abstractmethod
    def connectToWS(self, company_code: str = None, session_key: str = None): raise NotImplementedError

    @abstractmethod
    def getDiagram(self, module_id=None): raise NotImplementedError

    @abstractmethod
    def getArrows(self, module_id=None): raise NotImplementedError

    @abstractmethod
    def getNodeProperty(
        self, node_id, property_name): raise NotImplementedError

    @abstractmethod
    def getNodeProperties(self, node_id, properties): raise NotImplementedError

    @abstractmethod
    def setNodeProperties(self, node_id, properties): raise NotImplementedError

    @abstractmethod
    def saveModel(self, file_path): raise NotImplementedError

    @abstractmethod
    def getNodeInputs(self, node_id): raise NotImplementedError

    @abstractmethod
    def getNodeOutputs(self, node_id): raise NotImplementedError

    @abstractmethod
    def searchNodes(self, text, module_id, node_class,
                    extra_classes, fill_detail): raise NotImplementedError

    @abstractmethod
    def isChild(self, node: str, module_ids: list = []
                ): raise NotImplementedError

    @abstractmethod
    def getModelPreferences(self): raise NotImplementedError

    @abstractmethod
    def setModelProperties(self, modelProperties): raise NotImplementedError

    @abstractmethod
    def closeModel(self): raise NotImplementedError

    @abstractmethod
    def getModelName(self): raise NotImplementedError

    @abstractmethod
    def getModelId(self): raise NotImplementedError

    @abstractmethod
    def previewNode(self, node): raise NotImplementedError

    @abstractmethod
    def evaluate(self, definition): raise NotImplementedError

    @abstractmethod
    def callFunction(self, nodeId, params): raise NotImplementedError

    @abstractmethod
    def evaluateNode(
        self, node_id, dims, rows, columns, summary_by="sum",
        from_row=0, to_row=0, bottom_total=False, right_total=False
    ): raise NotImplementedError

    @abstractmethod
    def getIndexType(self, id): raise NotImplementedError

    @abstractmethod
    def getIndexValues(self, data): raise NotImplementedError

    @abstractmethod
    def isResultComputed(self, nodes): raise NotImplementedError

    @abstractmethod
    def getNodeIndexes(self, node_id): raise NotImplementedError

    @abstractmethod
    def isChoice(self, node_id): raise NotImplementedError

    @abstractmethod
    def isSelector(self, node_id): raise NotImplementedError

    @abstractmethod
    def getSelector(self, node_id): raise NotImplementedError

    @abstractmethod
    def isIndex(self, node_id): raise NotImplementedError

    @abstractmethod
    def isTable(self, node_id): raise NotImplementedError

    @abstractmethod
    def isTime(self, field): raise NotImplementedError

    @abstractmethod
    def getToolbars(self, extra_path): raise NotImplementedError

    @abstractmethod
    def profileNode(self, node_id): raise NotImplementedError

    @abstractmethod
    def createNode(self, node): raise NotImplementedError

    @abstractmethod
    def deleteNodes(self, node_ids): raise NotImplementedError

    @abstractmethod
    def createAlias(self, node_ids): raise NotImplementedError

    @abstractmethod
    def createInputNode(self, node_ids): raise NotImplementedError

    @abstractmethod
    def copyNodes(self, nodes): raise NotImplementedError

    @abstractmethod
    def copyAsValues(self, params): raise NotImplementedError

    @abstractmethod
    def moveNodes(self, nodes): raise NotImplementedError

    @abstractmethod
    def createNewModel(self, modelFile, modelName): raise NotImplementedError

    @abstractmethod
    def existNode(self, nodeId): raise NotImplementedError

    @abstractmethod
    def setNodeIdFromTitle(self, node_id): raise NotImplementedError

    @abstractmethod
    def exportFlatNode(self, nodeId, numberFormat, columnFormat,
                       fileName): raise NotImplementedError

    @abstractmethod
    def exportModule(self, moduleId, filename): raise NotImplementedError

    @abstractmethod
    def importModule(self, moduleId, filename,
                     importType): raise NotImplementedError

    @abstractmethod
    def callWizard(self, wizardRequest): raise NotImplementedError

    @abstractmethod
    def getCubeMetadata(self, query): raise NotImplementedError

    @abstractmethod
    def getCubeValues(self, query): raise NotImplementedError

    @abstractmethod
    def setNodeValueChanges(self, changes): raise NotImplementedError

    @abstractmethod
    def getCubeDimensionValues(self, query): raise NotImplementedError

    @abstractmethod
    def getUnclusterData(self, query): raise NotImplementedError

    @abstractmethod
    def executeButton(self, nodeId): raise NotImplementedError

    @abstractmethod
    def is_healthy(self): raise NotImplementedError

    @abstractmethod
    def getSystemResources(self): raise NotImplementedError

    @abstractmethod
    def installLibrary(self, lib, target): raise NotImplementedError

    @abstractmethod
    def getInstallProgress(self, from_line): raise NotImplementedError
