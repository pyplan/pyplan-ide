import json

import numpy as np
import pandas as pd

import cubepy
from pyplan_engine.common.classes.filterChoices import filterChoices
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq


class BaseEvaluator(object):
    """
    Base Class to manage node evaluators
    """

    def createResult(self, result, resultType, resultIsJson=False, onRow=None, onColumn=None, node=None, pageInfo=None):
        if resultIsJson:

            res = '{"resultType":"' + str(resultType) + '"'
            if not onRow is None:
                res += ',"onRow":"' + onRow + '"'
            if not onColumn is None:
                res += ',"onColumn":"' + onColumn + '"'
            if not pageInfo is None:
                res += ',"pageInfo":' + json.dumps(pageInfo)
            if not node is None and node.numberFormat:
                res += ',"numberFormat":"' + node.numberFormat + '"'
            res += ',"result":'
            res += result
            res += "}"
            return res
        else:

            res = {
                "resultType": str(resultType),
                "result": result,
                "onRow": onRow,
                "onColumn": onColumn
            }
            if not pageInfo is None:
                res["pageInfo"] = pageInfo

            # check if in scenario
            if not node is None:
                if node.model.isNodeInScenario(node.identifier):
                    res["scenario"] = True
                if node.numberFormat:
                    res["numberFormat"] = node.numberFormat

            return json.dumps(res)

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        if isinstance(result, np.ndarray):
            return self.createResult(result.tolist(), type(result), node=nodeDic[nodeId])
        elif callable(result):  # is function
            import inspect
            import jsonpickle
            aux = {
                "params": inspect.getargspec(result)[0]
            }
            return self.createResult(jsonpickle.encode(aux), type(result), node=nodeDic[nodeId])
        else:

            try:
                return self.createResult(result, type(result), node=nodeDic[nodeId])
            except:
                return self.createResult(str(result), type(result), node=nodeDic[nodeId])

    def getCubeValues(self, result, nodeDic, nodeId,
                      query): raise NotImplementedError

    def getCubeDimensionValues(
        self, result, nodeDic, nodeId, query): raise NotImplementedError

    def getCubeMetadata(self, result, nodeDic,
                        nodeId): raise NotImplementedError

    def generateEmptyPreviewResponse(self, nodeDic, nodeId):
        msg = "This node does not return any value"
        if nodeDic[nodeId].nodeClass == "button":
            msg = "Successfully executed"
        res = {
            "resultType": "",
            "dims": [],
            "console": "",
            "preview": msg
        }
        return json.dumps(res)

    def previewNode(self, nodeDic, nodeId):

        if not nodeDic[nodeId].result is None:
            res = {
                "resultType": str(type(nodeDic[nodeId].result)),
                "dims": [],
                "console": nodeDic[nodeId].lastEvaluationConsole,
                "preview": str(nodeDic[nodeId].result)[:1000]
            }

            if callable(nodeDic[nodeId].result):  # is function
                import inspect
                import jsonpickle
                try:
                    res["preview"] += "\nparams: " + \
                        str(inspect.getargspec(nodeDic[nodeId].result)[0])
                except Exception as ex:
                    # in some cases, inspect throws an error when trying to obtain the parameters of a function
                    pass
            return json.dumps(res)
        else:
            return self.generateEmptyPreviewResponse(nodeDic, nodeId)

    def setNodeValueChanges(self, nodeDic, nodeId, changes):
        value = None
        if not changes is None and len(changes["changes"]) == 1 and len(changes["changes"][0]["filterList"]) == 0:
            value = changes["changes"][0]["definition"]
            value = nodeDic[nodeId].sanitizeDefinition(value)

        if not value is None:
            nodeDic[nodeId].definition = value

    def isTable(self, node):
        return "0"

    def isIndexed(self, result):
        return False

    def getIndexes(self, node, result=None):
        return []

    def getIndexesWithLevels(self, node, result=None):
        return []

    def getIndexValues(self, nodeDic, data: IndexValuesReq, result=None):
        res = []
        if data.node_id:
            if (not data.node_id is None) & (data.node_id in nodeDic):
                node = nodeDic[data.node_id]
                if result is None:
                    result = node.result

                if (f"{data.index_id}.{data.node_id}") in self.getIndexes(node):
                    if self.isIndexed(result):
                        for index in result.index.levels:
                            if index.name == data.index_id:
                                res = index.values.tolist()
                                break
                    else:
                        res = result[data.index_id].unique().tolist()
        else:
            if (not data.index_id is None) & (data.index_id in nodeDic):
                node = nodeDic[data.index_id]
                if result is None:
                    result = node.result
                if isinstance(result, cubepy.Index):
                    res = result.values.tolist()
                elif isinstance(result, np.ndarray):
                    res = result.tolist()
                else:
                    res = list(result)
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
        return "S"

    def exportFlatNode(self, nodeDic, nodeId, numberFormat, columnFormat, fileName):
        if columnFormat == "tab":
            columnFormat = "\t"

        decimalSep = "."
        if numberFormat == 'TSPDSC':
            decimalSep = ","

        query = {
            "columns": self.getIndexes(nodeDic[nodeId]),
            "filters": None
        }

        data = self.getCubeValues(
            nodeDic[nodeId].result, nodeDic, nodeId, query)
        realIndexes = [x["field"] for x in data["dims"]]
        realIndexes = realIndexes + ["data_value"]

        dimValues = [x["values"] for x in data["dims"]]

        import itertools
        allCombinations = itertools.product(*dimValues)

        with open(fileName, 'w') as f:
            # headers
            f.write(columnFormat.join(realIndexes) + "\n")
            # data
            nn = 0
            for item in allCombinations:
                aa = 0
                f.write(columnFormat.join(str(e) for e in item) + columnFormat)
                f.write(str(data["values"][nn]).replace(
                    ".", decimalSep) + "\n")
                nn += 1

            f.close()

        return True

    def dumpNodeToFile(self, nodeDic, nodeId, fileName):
        definition = nodeDic[nodeId].definition
        with open(fileName, 'w') as f:
            f.write(definition)
            f.close()

    def geoUnclusterData(self, result, nodeDic, nodeId, rowIndex, attIndex, latField="latitude", lngField="longitude", geoField="geoField",
                         labelField="labelField", sizeField="sizeField", colorField="colorField", iconField="iconField"): raise NotImplementedError

    def postCalculate(self, node, result):
        """Method executed after calculate node
        """
        pass

    def copyAsValues(self, result, nodeDic, nodeId):
        """ Copy node as values """
        raise NotImplementedError

    def checkDateFormat(self, np_array):
        if "date" in np_array.dtype.name:
            def _cut(x): return x[:19]
            vfunc = np.vectorize(_cut)
            return vfunc(np_array.astype(str))
        else:
            return np_array
