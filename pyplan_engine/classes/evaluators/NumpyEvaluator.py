import json

import numpy as np

import cubepy
from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from pyplan_engine.classes.evaluators.CubepyEvaluator import CubepyEvaluator
from pyplan_engine.common.classes.filterChoices import filterChoices
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq
from cubepy.cube import kindToString


class NumpyEvaluator(BaseEvaluator):

    AXISNAME = "Axis "

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        evaluator = CubepyEvaluator()
        cube = self.createCube(nodeDic[nodeId].identifier, result)
        return evaluator.evaluateNode(cube, nodeDic, nodeId, dims, rows, columns, summaryBy, bottomTotal, rightTotal, fromRow, toRow)

    def hasDim(self, result, dim):
        return True if dim in result.dims else False

    def getIndexes(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        res = [self.AXISNAME +
               str(x)+"."+node.identifier for x in range(result.ndim)]
        return res

    def getIndexesWithLevels(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        if not result is None:
            for x in range(result.ndim):
                item = {"field": self.AXISNAME + str(x)+"."+node.identifier, "name": self.AXISNAME + str(
                    x), "description": "", "levels": []}
                res.append(item)
        return res

    def getIndexValues(self, nodeDic, data: IndexValuesReq, result=None):
        res = []
        if data.node_id:
            if (not data.node_id is None) & (data.node_id in nodeDic):
                node = nodeDic[data.node_id]
                if result is None:
                    result = node.result
                axe = int(data.index_id.split(" ")[1])
                lenAxe = result.shape[axe]
                res = list(range(lenAxe))
        if data.text1:
            text1 = data.text1.lower()
            if data.filter == filterChoices.CONTAINS.value:
                res = list(
                    filter(lambda item: text1 in str(item).lower(), res))
            elif data.filter == filterChoices.NOT_CONTAINS.value:
                res = list(
                    filter(lambda item: not text1 in str(item).lower(), res))
        return res

    def getIndexType(self, nodeDic, nodeId, indexId):
        return "N"

    def getCubeValues(self, result, nodeDic, nodeId, query):
        cube = self.createCube(nodeDic[nodeId].identifier, result)
        evaluator = CubepyEvaluator()
        return evaluator.getCubeValues(cube, nodeDic, nodeId, query)

    def getCubeDimensionValues(self, result, nodeDic, nodeId, query):
        cube = self.createCube(nodeDic[nodeId].identifier, result)
        evaluator = CubepyEvaluator()
        return evaluator.getCubeDimensionValues(cube, nodeDic, nodeId, query)

    def getCubeMetadata(self, result, nodeDic, nodeId):
        cube = self.createCube(nodeDic[nodeId].identifier, result)
        evaluator = CubepyEvaluator()
        return evaluator.getCubeMetadata(cube, nodeDic, nodeId)

    def createCube(self, nodeId, npArray):
        _dimsNames = [self.AXISNAME +
                      str(x)+"."+nodeId for x in range(npArray.ndim)]
        _dimsValues = [list(x) for x in (range(npArray.shape[y])
                                         for y in range(npArray.ndim))]
        _indexes = [cubepy.Index(_dimsNames[x], _dimsValues[x])
                    for x in range(len(_dimsNames))]
        _cube = cubepy.Cube(_indexes, npArray)
        return _cube

    def isTable(self, node):
        res = "0"
        if isinstance(node.result, np.ndarray):
            if not node.definition is None and node.definition != "":
                import re
                deff = re.sub(
                    '[\s+]', '', str(node.definition).strip(' \t\n\r')).lower()
                if (deff.startswith("result=np.")):
                    res = "1"
        return res

    def setNodeValueChanges(self, nodeDic, nodeId, nodeChanges):
        result = nodeDic[nodeId].result
        for change in nodeChanges["changes"]:
            newValue = change["definition"]
            slices = [slice(None)] * nodeDic[nodeId].result.ndim
            for filterItem in change["filterList"]:
                pos = int(filterItem["Value"])
                axis = int(
                    str(str(filterItem["Key"]).split(".")[0]).split(" ")[1])
                slices[axis] = pos

            result[tuple(slices)] = newValue

        np.set_printoptions(threshold=np.prod(result.shape))
        data = np.array2string(result, separator=",").replace('\n', '')
        newDeff = "result = np.array(" + data + ")"
        nodeDic[nodeId].definition = newDeff
        return "ok"

    def previewNode(self, nodeDic, nodeId):
        from pyplan_engine.classes.Helpers import Helpers
        from sys import getsizeof

        result = nodeDic[nodeId].result
        res = {
            "resultType": str(type(result)),
            "dims": [],
            "console": nodeDic[nodeId].lastEvaluationConsole,
            "preview": ""
        }

        for nn in range(result.ndim):
            _item = self.AXISNAME+str(nn) + " [" + str(result.shape[nn]) + "]"
            res["dims"].append(_item)

        res["preview"] += "Dimensions: " + str(result.ndim)
        res["preview"] += "\nShape: " + str(result.shape)
        res["preview"] += "\nSize: " + str(result.size)
        res["preview"] += "\nMemory: " + \
            str(round(result.nbytes/1024/1024, 2)) + " Mb"
        res["preview"] += "\nData type: " + \
            str(result.dtype) + " (" + kindToString(result.dtype.kind)+")"
        res["preview"] += "\nValues: \n\n" + str(result)[:1000]

        result = None

        return json.dumps(res)
