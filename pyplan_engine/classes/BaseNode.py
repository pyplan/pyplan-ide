import datetime as dt
import io
import re
import uuid
from contextlib import redirect_stdout
from sys import exc_info, getsizeof
from types import CodeType

import numpy as np

from pyplan_engine.classes.dynamics.BaseDynamic import BaseDynamic
from pyplan_engine.classes.dynamics.FactoryDynamic import FactoryDynamic
from pyplan_engine.classes.Evaluator import Evaluator
from pyplan_engine.classes.Helpers import Helpers
from pyplan_engine.classes.IOEngine import IOEngine
from pyplan_engine.classes.NodeInfo import NodeInfo
from pyplan_engine.classes.PyplanFunctions import PyplanFunctions, Selector
from pyplan_engine.classes.XHelpers import XHelpers


class BaseNode(object):

    SERIALIZABLE_PROPERTIES = ['identifier', 'definition', 'title', 'nodeClass', 'moduleId', 'x', 'y', 'z', 'w', 'h',
                               "description", "units", "color", "errorInDef", "nodeInfo", "nodeFont", "numberFormat", "originalId", "extraData", "picture", "evaluateOnStart"]

    FORMNODE_TYPE_CHECKBOX = 0
    FORMNODE_TYPE_COMBOBOX = 1
    FORMNODE_TYPE_SCALAR = 2
    FORMNODE_TYPE_BUTTON = 3

    def __init__(self, model, identifier=None, nodeClass=None, moduleId=None, x=None, y=None, originalId=None):
        self._model = model
        self._originalId = originalId
        self._result = None
        self._isCalc = False
        self._title = None
        self.description = None
        self.units = None
        self.numberFormat = None
        self.color = None
        self.errorInDef = False
        self.nodeClass = nodeClass if not nodeClass is None else "variable"
        self._definition = self.getDefaultDefinitionByClass(self.nodeClass)
        self.nodeInfo = self.getDefaultNodeinfoByClass(self.nodeClass)
        self.moduleId = moduleId if not moduleId is None else self._model.modelNode.identifier
        self.x = int(x) if not x is None else 100
        self.y = int(y) if not y is None else 100
        self.z = 1
        if nodeClass == "text":
            self.z = -1
        self.w = 100
        self.h = 50

        self._ioEngine = IOEngine(self)
        self._resultMemory = 0
        self.system = False
        self.lastEvaluationTime = 0
        self.lastEvaluationConsole = ""
        self.evaluationVersion = 0
        self.profileParent = None
        self.nodeFont = None
        self._bypassCircularEvaluator = False
        self.extraData = None
        self.dynamicEvaluator = None
        self.picture = None
        self._hierarchy_parents = None
        self._hierarchy_maps = None
        self._releaseMemory = False
        self._evaluateOnStart = False

        # load default props by toolbar
        nodeFormat = model.getDefaultNodeFormat(self.nodeClass)

        if identifier is None:
            if not nodeClass is None:
                if nodeClass == "alias" or nodeClass == "formnode" or nodeClass == "text":
                    self._identifier = "a"+str(uuid.uuid4().hex).lower()
                elif nodeClass == "index":
                    self._identifier = model.getNextIdentifier("index")
                else:
                    self._identifier = model.getNextIdentifier("node")
            if not nodeFormat is None:
                if not nodeFormat["nodeClass"] is None:
                    if nodeFormat["nodeClass"] == "alias" or nodeFormat["nodeClass"] == "formnode" or nodeFormat["nodeClass"] == "text":
                        self._identifier = "a"+str(uuid.uuid4().hex).lower()
                    elif nodeFormat["nodeClass"] == "index":
                        self._identifier = model.getNextIdentifier("index")
                    else:
                        self._identifier = model.getNextIdentifier("node")
        else:
            self._identifier = identifier

        if not nodeFormat is None:
            self.fromObj(nodeFormat)

    def __del__(self):
        self.release()

    def release(self):
        """Release object"""
        self._model = None
        self._result = None
        self._identifier = None
        self._definition = None
        self.moduleId = None
        self.dynamicEvaluator = None
        if not self.ioEngine is None:
            self.ioEngine.release()
            self._ioEngine = None

    def toObj(self, exceptions=None, properties=None, fillDefaultProperties=False):
        """Convert node to dictionary"""
        res = {}
        if not properties is None:
            for k in properties:
                if k in BaseNode.SERIALIZABLE_PROPERTIES and hasattr(self, k):
                    res[k] = getattr(self, k)
        else:
            for k in BaseNode.SERIALIZABLE_PROPERTIES:
                if ((exceptions is None) or (not k in exceptions)) and hasattr(self, k):
                    res[k] = getattr(self, k)

        if fillDefaultProperties:
            if not "color" in res or res["color"] is None:
                res["color"] = BaseNode.getDefaultColor(self.nodeClass)

            res["hasPicture"] = self.hasPicture

            # fill formnode/alias
            if self.nodeClass in ["formnode", "alias"]:
                res["originalId"] = self.originalId
                res["originalClass"] = self.originalClass

                if self.nodeClass == "formnode":
                    res["formNodeType"] = self.formNodeType
                    res["formNodeExtraValue"] = self.formNodeExtraValue

                    # check if value is serializable
                    try:
                        # jsonify(self.formNodeValue)
                        # comentado porque no se puede utilizar jsonify fuera del contexto del pyplan_engine. (cuando se usa multiprocesador)
                        res["formNodeValue"] = self.formNodeValue
                    except TypeError as ex:
                        res["formNodeValue"] = str(ex)
                        res["formNodeType"] = self.FORMNODE_TYPE_SCALAR

        return res

    def fromObj(self, obj):
        """Convert dictionary to basenode object"""
        for k in BaseNode.SERIALIZABLE_PROPERTIES:
            if k in obj:
                # work around for migrate nodeInfo class
                if k == "nodeInfo":
                    if isinstance(obj[k], dict):
                        obj[k] = NodeInfo(obj[k]["showInputs"], obj[k]["showOutputs"], obj[k]
                                          ["showLabel"], obj[k]["showBorder"], obj[k]["fill"], obj[k]["useNodeFont"])

                setattr(self, k, obj[k])

    # Props

    @property
    def node(self):
        return self

    @property
    def model(self):
        return self._model

    @property
    def result(self):
        try:
            self.calculate()
        except Exception as e:
            err = str(e)
            if not "Error evaluating" in err:
                title = self.title
                if title is None:
                    title = ""
                else:
                    title = title+" "
                title = title + "(" + self.identifier + ") "
                err = "Error evaluating "+title+": " + err

            raise ValueError(err)

        try:
            return self._result
        finally:
            if self.releaseMemory:
                self._isCalc = False
                self.profileParent = None
                self._result = None
                self._resultMemory = 0

    @property
    def isCalc(self):
        return self._isCalc

    @property
    def releaseMemory(self):
        return self._releaseMemory

    @releaseMemory.setter
    def releaseMemory(self, value):
        self._releaseMemory = value

    @property
    def evaluateOnStart(self):
        return self._evaluateOnStart

    @evaluateOnStart.setter
    def evaluateOnStart(self, value):
        self._evaluateOnStart = value

    @property
    def resultType(self):
        if self._isCalc:
            return str(type(self.result))
        else:
            return ""

    @property
    def usedMemory(self):
        return (getsizeof(self.definition) + self._resultMemory) / 1024 / 1024

    @property
    def hasPicture(self):
        if self.picture:
            return True
        return False

    @property
    def title(self):
        if not self.originalId is None:
            if self.model.existNode(self.originalId):
                return self.model.getNode(self.originalId).title
            else:
                return self._title
        else:
            return self._title

    @title.setter
    def title(self, value):
        self._title = value
        if self.isCalc:
            self.postCalculate()

    @property
    def definition(self):
        return self._definition

    @definition.setter
    def definition(self, value):
        if not self.model.isLoadingModel:
            value = self.sanitizeDefinition(value)

        self._definition = value
        if not self.model.isLoadingModel:
            self.invalidate()
            self.generateIO()

        self._isCalc = False

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        if value != self._identifier:
            if self._model.existNode(value):
                raise ValueError("'The id '" + value + "' already exists")
            if self._model.updateNodeIdInDic(self._identifier, value):
                self.ioEngine.updateNodeId(self._identifier, value)
                self._identifier = value
                if self.isCalc:
                    self.invalidate()

    @property
    def isIndexed(self):
        raise ValueError("TODO: Mover isIndexed a clase BaseEvaluator")
        return False

    @property
    def indexes(self):
        res = []
        self.calculate()
        if not self._result is None:
            evaluator = Evaluator.createInstance(self._result)
            return evaluator.getIndexes(self)

    @property
    def ioEngine(self):
        return self._ioEngine

        """
        #comentado porque da error al eliminar alias y dps al grabar modelo
        if self.originalId is not None:            
            return self.model.getNode(self.originalId)._ioEngine
        else:
            return self._ioEngine
        """

    @property
    def inputs(self):
        return self.ioEngine.inputs

    @property
    def outputs(self):
        return self.ioEngine.outputs

    @property
    def originalId(self):
        return self._originalId

    @originalId.setter
    def originalId(self, value):
        self._originalId = value

    @property
    def originalClass(self):
        if self._originalId is not None:
            if self.model.existNode(self._originalId):
                return self.model.getNode(self._originalId).nodeClass
        return None

    @property
    def formNodeType(self):
        if not self.originalId is None:
            try:
                originalNode = self.model.getNode(self.originalId)
                if not originalNode is None:
                    if "choice(" in originalNode.definition or "selector(" in originalNode.definition:
                        return self.FORMNODE_TYPE_COMBOBOX
                    elif str(originalNode.result).isnumeric() or isinstance(originalNode.result, str) or isinstance(originalNode.result, float) or isinstance(originalNode.result, int):
                        return self.FORMNODE_TYPE_SCALAR
                    elif isinstance(originalNode.result, bool):
                        return self.FORMNODE_TYPE_CHECKBOX

            except (RuntimeError, TypeError, NameError, ValueError, SyntaxError):
                pass

        return self.FORMNODE_TYPE_BUTTON

    @property
    def formNodeValue(self):
        if self.formNodeType == self.FORMNODE_TYPE_SCALAR or self.formNodeType == self.FORMNODE_TYPE_CHECKBOX or self.formNodeType == self.FORMNODE_TYPE_COMBOBOX:
            try:
                res = self.model.getNode(self.originalId).result
                if isinstance(res, Selector):
                    if "numpy." in str(type(res.value)):
                        return res.value.item()
                    else:
                        return res.value
                else:
                    return res
            except Exception as e:
                self.errorInDef = True
        return None

    @property
    def formNodeExtraValue(self):
        if self.formNodeType == self.FORMNODE_TYPE_SCALAR or self.formNodeType == self.FORMNODE_TYPE_CHECKBOX:
            try:
                if isinstance(self.result, str):
                    return f'"{self.result}"'
                else:
                    return self.result
            except (RuntimeError, TypeError, NameError, ValueError, SyntaxError):
                pass
        elif self.formNodeType == self.FORMNODE_TYPE_COMBOBOX:
            originalNode = self.model.getNode(self.originalId)
            return originalNode.definition
        return None

    @property
    def hierarchy_parents(self):
        return self._hierarchy_parents

    @property
    def hierarchy_maps(self):
        return self._hierarchy_maps

    # Synonimos
    @property
    def isin(self):
        return self.moduleId

    # Methods
    def invalidate(self, fromCircularNode=False):
        """Invalidate node result"""
        self._isCalc = False
        self.profileParent = None
        self._result = None
        self._resultMemory = 0
        if self.isCircular() and not fromCircularNode:
            circularNodes = self.getSortedCyclicDependencies()
            for node in circularNodes:
                if node != self.identifier:
                    if self._model.existNode(node):
                        self._model.getNode(node).invalidate(
                            fromCircularNode=True)
        self.invalidateOutputs()

    def invalidateOutputs(self):
        """Invalidate outputs of this node"""
        isCircular = self.isCircular()
        for node in self.ioEngine.outputs:
            if not node is None:
                if self._model.existNode(node):
                    if isCircular and self._model.getNode(node).isCircular():
                        pass
                    else:
                        if self._model.getNode(node).isCalc:
                            self._model.getNode(node).invalidate()

    def generateIO(self):
        """Generate inputs and outputs"""
        if self.nodeClass not in ['alias', 'formnode']:
            tmpCode = None
            try:
                tmpCode = self.compileDef(self._definition)
            except SyntaxError:
                aa = 1
                # TODO: get detail of error

            if not tmpCode is None:
                # TODO: if cp.excel.. in def and other node Id is excel then don't generate input for that node
                nameList = self.parseNames(tmpCode)
                finalList = []
                for item in nameList:
                    if item and self.model.existNode(item):
                        rxText = "[^!.a-zA-Z_]\\b(###)\\b(?!={1}(?!={1}))".replace(
                            "###", item)
                        rx = re.compile(rxText)
                        if len(re.findall(rx, self.definition)) > 0:
                            finalList.append(item)
                self.ioEngine.updateInputs(finalList)

    def compileDef(self, definition):
        """Compile definition"""
        try:
            self.errorInDef = False
            tmpCode = compile(str(definition), '<string>', 'exec')
            return tmpCode
        except SyntaxError:
            self.errorInDef = True
            # TODO: get detail of error
            pass
        return None

    def calculate(self, extraParams=None):
        """Calculate result of node"""

        if not self.isCalc or self.nodeClass == "button" or self.nodeClass == "formnode":
            nodeIsCircular = self.isCircular()
            if not self._bypassCircularEvaluator and nodeIsCircular:
                circularNodes = self.getSortedCyclicDependencies()

                if self.dynamicEvaluator is None:
                    self.dynamicEvaluator = FactoryDynamic.createInstance(
                        circularNodes, self)

                params = self.dynamicEvaluator.generateCircularParameters(
                    self, circularNodes)

                if params['dynamicIndex'] is None:
                    raise ValueError("Cyclic dependency detected between nodes: " + ",".join(
                        circularNodes) + ".\nPlease use the cp.dynamic function")
                self.dynamicEvaluator.circularEval(self, params)
            else:

                self.model.currentProcessingNode(self.identifier)

                self._bypassCircularEvaluator = False

                startTime = dt.datetime.now()
                finalDef = str(self._definition)

                # CLEAR circular dependency
                if nodeIsCircular:
                    finalDef = BaseDynamic.clearAllCircularDependency(finalDef)
                tmpCode = self.compileDef(finalDef)

                # check for replace calls to varaibles with next rules:
                # node1  --> change to getNode('node1').result
                # node1.result  --> change to getNode('node1').result
                # node1.title   --> change to getNode('node1').title
                # "node1" --> no change
                # 'node1' --> no change
                if not tmpCode is None:
                    names = self.parseNames(tmpCode)
                    rx = r"('[^'\\]*(?:\\.[^'\\]*)*'|\"[^\"\\]*(?:\\.[^\"\\]*)*\")|\b{0}\b"
                    for node in names:
                        if self._model.existNode(self._model.clearId(node)):
                            finalDef = re.sub(rx.format(node), lambda m:
                                              (
                                m.group(1)
                                if m.group(1)
                                else
                                (
                                    "getNode('"+node+"')"
                                    if (m.endpos > m.regs[0][1]+5) and ((m.string[m.regs[0][1]:m.regs[0][1]+5] == '.node') or (m.string[m.regs[0][1]:m.regs[0][1]+8] == '.timeit('))
                                    else
                                    (node
                                     if (m.string[m.regs[0][0]-1:m.regs[0][0]+len(node)] == ('.'+node))
                                     else "getNode('"+node+"').result"
                                     )
                                )
                            ), finalDef, 0, re.IGNORECASE)
                        elif node == "self":
                            finalDef = re.sub(rx.format(node), lambda m:
                                              (
                                m.group(1)
                                if m.group(1)
                                else
                                "getNode('" + self.identifier + "')"
                                if (m.endpos > m.regs[0][1]+11) and (m.string[m.regs[0][1]:m.regs[0][1]+11] != '._tryFilter')
                                else "self"
                            ), finalDef, 0, re.IGNORECASE)

                localRes = {
                    "getNode": self._model.getNode,
                    "cp": Helpers(self),
                    "pp": XHelpers(self)
                }
                PyplanFunctions.register(localRes)
                if not extraParams is None:
                    for keyParam in extraParams:
                        localRes[keyParam] = extraParams[keyParam]

                if self.identifier != "imports":
                    customImports = self.model.getCustomImports()
                    if customImports:
                        for keyParam in customImports:
                            localRes[keyParam] = customImports[keyParam]

                try:
                    # execute node definition in supervised context
                    memoryIO = io.StringIO()
                    try:
                        with redirect_stdout(memoryIO):
                            exec(compile(finalDef, '<string>', 'exec'), localRes)
                    except Exception as ex:
                        if "_io.StringIO" in str(ex):
                            exec(compile(finalDef, '<string>', 'exec'), localRes)
                        else:
                            raise ex

                    self.lastEvaluationConsole = memoryIO.getvalue()
                    memoryIO = None

                    if 'this' in localRes:
                        self._result = localRes['this']
                        self._resultMemory = Helpers.getResultSize(
                            self._result)
                    elif 'result' in localRes:
                        self._result = localRes['result']
                        self._resultMemory = Helpers.getResultSize(
                            self._result)
                    else:
                        self._result = None
                        if self.nodeClass not in ["button", "module", "text"]:
                            if self.lastEvaluationConsole != "":
                                self._result = str(self.lastEvaluationConsole)
                            else:
                                raise ValueError(
                                    "The result was not found. Did you forget to include the text 'result =' ?")

                    self._isCalc = True
                    self.postCalculate()

                    endTime = dt.datetime.now()
                    self.lastEvaluationTime = (
                        endTime - startTime).total_seconds()
                    self.evaluationVersion = self.model.evaluationVersion
                finally:
                    localRes["cp"].release()
                    localRes["pp"].release()
                    localRes = None
        else:
            self._bypassCircularEvaluator = False

    def postCalculate(self):
        evaluator = Evaluator.createInstance(self._result)
        evaluator.postCalculate(self, self._result)

    def parseNames(self, compiledCode):
        """Parse names used in node definition"""
        res = []
        if not compiledCode is None:
            res = compiledCode.co_names
            for co in compiledCode.co_consts:
                if not co is None and isinstance(co, CodeType):
                    res += co.co_names
        return res

    def updateDefinitionForChangeId(self, oldId, newId):
        """ Search and replace on this node definition the oldId for the newId
        """
        rx = re.compile(r"((?<!\w)(?<!\d)(?<!\.)" + re.escape(oldId) +
                        "(?!\d)(?!\w))(?=(?:[^\"]|[\"][^\"]*[\"])*$)")
        newDef = re.sub(rx, newId, self.definition)
        self.definition = newDef
        pass

    def isCircular(self):
        """ Checks if the node is part of a cycle
        """
        _id = self.identifier if self.originalId is None else self.originalId
        _inputNodes = [_id]

        nn = 0
        while nn < len(_inputNodes):
            _node = _inputNodes[nn]
            if self.model.existNode(_node):
                for _inputId in self.model.getNode(_node).ioEngine.inputs:
                    if _inputId == _id:
                        return True
                    else:
                        if not _inputId in _inputNodes:
                            _inputNodes.append(_inputId)
            nn += 1
        return False

    def getSortedCyclicDependencies(self):
        """
        Return list of nodes in circular dependencyes, sortered by execition order
        """
        res = []
        if self.isCircular():
            res = [self.identifier if self.originalId is None else self.originalId]
            # fill node inputs
            nn = 0
            while nn < len(res):
                _node = res[nn]
                for _inputId in self.model.getNode(_node).ioEngine.inputs:
                    if not _inputId in res and self.model.getNode(_inputId).isCircular():
                        res.append(_inputId)
                nn += 1
        return res

    def profileNode(self, evaluated, response, evaluationVersion, profileParentId):
        """Perform node profile"""
        if not evaluated is None:
            if self.identifier in evaluated:
                return response
            else:
                evaluated.append(self.identifier)
                if self.evaluationVersion == evaluationVersion:
                    if self.profileParent is None:
                        self.profileParent = profileParentId
                    auxVal = {"nodeId": self.identifier, "title": self.identifier if self.model.getNode(self.identifier).title is None else self.model.getNode(self.identifier).title, "moduleId": self.model.getNode(
                        self.identifier).moduleId, "evaluationTime": self.model.getNode(self.identifier).lastEvaluationTime, "usedMemory": self.model.getNode(self.identifier).usedMemory, "calcTime": 0.00},
                    response.extend(auxVal)
                if not response is None:
                    for nodeInputId in self.inputs:
                        if nodeInputId not in evaluated:
                            response = self.model.getNode(nodeInputId).profileNode(
                                evaluated, response, evaluationVersion, self.identifier)
        return response

    def sanitizeDefinition(self, value):
        """
        Sanitize from current front (Ade to py)
        """
        if str(value).isnumeric():
            value = "result = " + str(value)
        return value

    def getDefaultDefinitionByClass(self, nodeClass):
        """Return default definition by node class"""
        if nodeClass == "module":
            return ""
        elif nodeClass == "index":
            return "result = cp.index(['Item 1', 'Item 2', 'Item 3'])"
        elif nodeClass == "button":
            return ""
        else:
            return "result = 0"

    def getDefaultNodeinfoByClass(self, nodeClass):
        """
            Default nodeinfo by class. 
            Positions are:
                showInputs = 0
                showOutputs = 1
                showLabel = 2
                showBorder = 3
                fill = 4
                useNodeFont = 5
        """
        if nodeClass == "text":
            return NodeInfo(0, 0, 1, 0, 0, 0)
        if nodeClass == "alias":
            return NodeInfo(0, 0, 1, 1, 1, 0)
        elif nodeClass == "index":
            return NodeInfo(0, 0, 1, 1, 1, 0)
        elif nodeClass == "function":
            return NodeInfo(0, 0, 1, 1, 1, 0)
        elif nodeClass == "button":
            return NodeInfo(0, 0, 1, 1, 1, 0)
        else:
            return NodeInfo(1, 1, 1, 1, 1, 0)

    def timeit(self, repeat=1):
        """ Get stats after evaluate "repeat" times this node
        """
        import timeit

        def _testNode_():
            self.invalidate()
            self.node.result

        _locals_ = {"_testNode_": _testNode_}
        _res = timeit.repeat("_testNode_() ", repeat=repeat,
                             number=1, globals=_locals_)
        return str({
            "average": float(str(round(np.mean(_res), 3))),
            "best": float(str(round(np.min(_res), 3))),
            "max": float(str(round(np.max(_res), 3))),
        })

    def set_hierarchy(self, parents, maps):
        self._hierarchy_parents = parents
        self._hierarchy_maps = maps

    # ***********************************
    # *** CYCLICK EVALUATOR  METHODS  ***
    # ***********************************

    def bypassCircularEvaluator(self):
        """Mark node for bypass circular evaluator"""
        self._bypassCircularEvaluator = True
        return self

    # *********************************
    # *** CLASS METHODS             ***
    # *********************************

    @staticmethod
    def getDefaultColor(nodeClass):
        dic = {
            "variable": "#4CBCFF",
            "button": "#a6a6a6",
            "decision": "#4cffa6",
            "constant": "#ff794c",
            "module": "#4c83ff",
            "function": "#cc99ff",
            "chance": "#49E4F7",
            "determ": "#076CBC",
            "objective": "#ff4c97",
            "index": "#9999ff",
            "library": "#076CBC",
            "form": "#076CBC",
            "text": "#FEFEFE",
            "picture": "#FEFEFE",
            "formnode": "#076CBC",
            "constraint": "#f2e340"
        }
        return dic[str(nodeClass).lower()] if str(nodeClass).lower() in dic else "#6699FF"
