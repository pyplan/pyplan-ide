import json
import math

import numpy as np
import pandas as pd
import xarray as xr

from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from pyplan_engine.classes.evaluators.PandasEvaluator import PandasEvaluator
from pyplan_engine.classes.XHelpers import XHelpers, XIndex
from pyplan_engine.common.classes.filterChoices import filterChoices
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq


class XArrayEvaluator(BaseEvaluator):

    PAGESIZE = 100
    MAX_COLUMS = 5000

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        if isinstance(result, xr.DataArray):
            return self.cubeEvaluate(result, nodeDic, nodeId, dims, rows, columns, summaryBy, bottomTotal, rightTotal, fromRow, toRow)
        elif isinstance(result, XIndex):
            return self.indexEvaluate(result, nodeDic, nodeId, dims, rows, columns, summaryBy, bottomTotal, rightTotal, fromRow, toRow)

    def cubeEvaluate(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        sby = np.sum
        if summaryBy == 'avg':
            sby = np.mean
        elif summaryBy == 'max':
            sby = np.max
        elif summaryBy == 'min':
            sby = np.min

        if (fromRow is None) or int(fromRow) <= 0:
            fromRow = 1
        if (toRow is None) or int(toRow) < 1:
            toRow = 100
        fromRow = int(fromRow)
        toRow = int(toRow)

        result = self.applyHierarchy(
            result, nodeDic, nodeId, dims, rows, columns, sby)

        _filters = {}
        _rows = []
        _columns = []
        if not rows is None:
            for row in rows:
                if self.hasDim(result, str(row["field"])):
                    _rows.append(str(row["field"]).split(".")[0])
                    self.addToFilter(nodeDic, row, _filters)

        if not columns is None:
            for column in columns:
                if self.hasDim(result, str(column["field"])):
                    _columns.append(str(column["field"]).split(".")[0])
                    self.addToFilter(nodeDic, column, _filters)

        if not dims is None:
            for dim in dims:
                if self.hasDim(result, str(dim["field"]).split(".")[0]):
                    self.addToFilter(nodeDic, dim, _filters)

        tmp = None
        filteredResult = result
        if len(_filters) > 0:
            filteredResult = result.sel(_filters)

        if len(_rows) == 0 and len(_columns) == 0 and result.ndim > 0:
            try:
                tmp = sby(filteredResult)
            except Exception as ex:
                if "flexible type" in str(ex):
                    tmp = sby(filteredResult.astype("O"))
                else:
                    raise ex

        else:
            otherDims = [
                xx for xx in filteredResult.dims if xx not in (_rows + _columns)]
            if len(otherDims) > 0:

                try:
                    tmp = filteredResult.reduce(
                        sby, otherDims).transpose(*(_rows + _columns))
                except Exception as ex:
                    if "flexible type" in str(ex):
                        tmp = filteredResult.astype("O").reduce(
                            sby, otherDims).transpose(*(_rows + _columns))

            else:
                tmp = filteredResult.transpose(*(_rows + _columns))

        finalValues = tmp.values
        finalIndexes = []
        if tmp.ndim > 0:
            finalIndexes = tmp.coords[tmp.dims[0]].values
        finalColumns = ["Total"]
        if tmp.ndim == 2:
            finalColumns = tmp.coords[tmp.dims[1]].values

        # Add totales
        _totalRow = None
        if bottomTotal and len(_rows) > 0:
            # add total row
            if tmp.ndim == 1:
                _totalRow = finalValues.sum(axis=0).reshape(1)
            else:
                _totalRow = finalValues.sum(
                    axis=0).reshape(1, len(finalValues[0]))
                _totalRow = _totalRow[0]
                if rightTotal:
                    _totalRow = np.append(_totalRow, finalValues.sum())

        if rightTotal and len(_columns) > 0:
            # add total column
            if tmp.ndim == 1:
                finalIndexes = np.append(finalIndexes, "Total")
                finalValues = np.append(
                    finalValues, finalValues.sum(axis=0).reshape(1), axis=0)
            else:
                finalColumns = np.append(finalColumns, "Total")
                finalValues = np.append(finalValues, finalValues.sum(
                    axis=1).reshape(len(finalValues), 1), axis=1)

        # chek inf
        if self.kindToString(finalValues.dtype.kind) == "numeric":
            if np.isinf(finalValues).any():
                finalValues[np.isinf(finalValues)] = None

        # chec if haver nan values
        if pd.isnull(finalValues).any():
            try:
                finalValues = np.where(
                    np.isnan(finalValues), None, finalValues)
            except:
                finalValues[pd.isnull(finalValues)] = None

        res = {}
        pageInfo = None
        onRow = None
        onColumn = None
        if len(_rows) == 0 and len(_columns) == 0:
            res = {
                "columns": [],
                "index": ["Total"],
                "data": [[finalValues.tolist()]]
            }
        elif len(_rows) == 0:
            onColumn = _columns[0]
            res = {
                "columns": self.checkDateFormat(finalIndexes[:XArrayEvaluator.MAX_COLUMS]).tolist(),
                "index": finalColumns,
                "data": [finalValues[:XArrayEvaluator.MAX_COLUMS].tolist()]
            }
        elif len(_columns) == 0:

            if (len(finalIndexes) > self.PAGESIZE):
                pageInfo = {
                    "fromRow": int(fromRow),
                    "toRow": int(toRow),
                    "totalRows": len(finalIndexes)
                }

            onRow = _rows[0]
            res = {
                "columns": finalColumns,
                "index": self.checkDateFormat(finalIndexes[fromRow-1:toRow]).tolist(),
                "data": [[x] for x in finalValues[fromRow-1:toRow].tolist()]
            }
            # add total rows
            if not _totalRow is None:
                res["index"].append("Total")
                res["data"].append(_totalRow.tolist())

        else:
            onColumn = _columns[0]
            onRow = _rows[0]

            if (len(finalIndexes) > self.PAGESIZE):
                pageInfo = {
                    "fromRow": int(fromRow),
                    "toRow": int(toRow),
                    "totalRows": len(finalIndexes)
                }

            res = {
                "columns": self.checkDateFormat(finalColumns[:XArrayEvaluator.MAX_COLUMS]).tolist(),
                "index": self.checkDateFormat(finalIndexes[fromRow-1:toRow]).tolist(),
                "data": finalValues[fromRow-1:toRow, :XArrayEvaluator.MAX_COLUMS].tolist()
            }

            # add total rows
            if not _totalRow is None:
                res["index"].append("Total")
                res["data"].append(
                    _totalRow[:XArrayEvaluator.MAX_COLUMS].tolist())

        return self.createResult(res, type(tmp), onRow=onRow, onColumn=onColumn, node=nodeDic[nodeId], pageInfo=pageInfo)

    def hasDim(self, result, dim):
        return True if dim.split(".")[0] in result.dims else False

    def addToFilter(self, nodeDic, dim, filters):
        if "values" in dim and dim["values"] is not None and len(dim["values"]) > 0:
            field = str(dim["field"]).split(".")[0]
            # chek if the node id of the index we are using to filter has changed

            nodeId = None
            indexType = None
            indexType = self.getIndexType(nodeDic, nodeId, field)

            # check if the indexes have change
            _values = None
            if indexType == "S":
                _values = [str(xx["value"]) for xx in dim["values"]]
            else:
                _values = [int(xx["value"]) for xx in dim["values"]]

            all_values = None
            npValues = np.array(_values)
            if field in nodeDic:
                all_values = nodeDic[field].result.values
            elif len(dim["field"].split(".")) > 1:
                node_id = str(dim["field"]).split(".")[1]
                if field in nodeDic[node_id].result.dims:
                    all_values = nodeDic[node_id].result.coords[field].values
            serie = pd.Series(all_values)
            if not all_values is None and serie.isin(npValues).any():
                npValues = all_values[serie.isin(npValues)]

            if len(npValues) > 0:
                filters[field] = npValues

    def getIndexes(self, node, result=None):
        if result is None:
            result = node._result
        return [(xx+"."+node.identifier) for xx in result.dims]

    def getIndexesWithLevels(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        if not result is None:
            _model = node.model
            for indexItem in result.dims:
                itemDim = indexItem.split(",")[0]
                item = {"field": itemDim+"."+node.identifier,
                        "name": itemDim, "description": "", "levels": []}

                if _model.existNode(itemDim):
                    levelNode = _model.getNode(itemDim)
                    if levelNode.title:
                        item["name"] = levelNode.title
                        item["description"] = levelNode.description
                    if levelNode.numberFormat:
                        item["numberFormat"] = levelNode.numberFormat

                    # check for levels

                    if not levelNode.hierarchy_parents is None:

                        def buildLevels(parents, levelList):
                            if not isinstance(parents, list):
                                parents = [parents]
                            for parentIndexId in parents:
                                parentIndexNode = _model.getNode(parentIndexId)
                                if parentIndexNode is None:
                                    raise ValueError(
                                        f"Node {parentIndexId} not found")

                                levelItem = {
                                    "field": parentIndexId, "name": parentIndexNode.title or parentIndexId}
                                levelList.append(levelItem)
                                _dummy = parentIndexNode.result  # to force calc
                                if not parentIndexNode.hierarchy_parents is None:
                                    buildLevels(
                                        parentIndexNode.hierarchy_parents, levelList)

                        listOfLevels = [
                            {"field": itemDim, "name": item["name"]}]
                        indexParents = levelNode.hierarchy_parents
                        buildLevels(indexParents, listOfLevels)
                        item["levels"] = listOfLevels
                elif "datetime" in result.coords[itemDim].dtype.name:
                    item["numberFormat"] = "2,DD,0,,0,0,4,0,$,5,FULL,0"

                res.append(item)
        return res

    def isIndexed(self, result):
        if not result is None:
            obj = result
            if isinstance(obj, pd.Series):
                obj = pd.DataFrame({"values": obj})
            if isinstance(obj, pd.DataFrame):
                if (isinstance(obj.index, pd.MultiIndex) or isinstance(obj.index, pd.Index)) and len(obj.index.names) > 0 and (not obj.index.names[0] is None):
                    return True
        return False

    def getIndexValues(self, nodeDic, data: IndexValuesReq, result=None):
        res = []
        if data.node_id:
            if (not data.node_id is None) & (data.node_id in nodeDic):
                node = nodeDic[data.node_id]
                if result is None:
                    result = node.result
                res = self.checkDateFormat(
                    result[data.index_id].values).tolist()
        elif (not data.index_id is None) & (data.index_id in nodeDic):
            node = nodeDic[data.index_id]
            if result is None:
                result = node.result
            if isinstance(result, XIndex):
                res = result.values.tolist()
            elif isinstance(result, np.ndarray):
                res = self.checkDateFormat(result).tolist()
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
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        res = "S"

        if (not indexId is None) & (indexId in nodeDic):
            node = nodeDic[indexId]
            if isinstance(node.result, XIndex) or isinstance(node.result, pd.Index):
                if str(node.result.values.dtype) in numerics:
                    res = "N"
            elif isinstance(node.result, np.ndarray):
                if str(node.result.dtype) in numerics:
                    res = "N"
        elif nodeId:
            if (not nodeId is None) & (nodeId in nodeDic):
                node = nodeDic[nodeId]
                if str(node.result.coords[indexId].values.dtype) in numerics:
                    res = "N"
        return res

    def getCubeValues(self, result, nodeDic, nodeId, query):
        if isinstance(result, xr.DataArray):
            res = {
                "dims": [],
                "values": []
            }

            # fix field.array
            query["columns"] = [xx.split(".")[0] for xx in query["columns"]]

            _filters = {}
            if not query["filters"] is None:
                for dimFilter in query["filters"]:
                    field = str(dimFilter["field"]).split(".")[0]
                    if self.hasDim(result, field):
                        dimFilter["values"] = [{"value": xx}
                                               for xx in dimFilter["values"]]
                        self.addToFilter(nodeDic, dimFilter, _filters)

            _filteredResult = result
            if len(_filters):
                _filteredResult = result.sel(_filters)
            nodeIndexes = self.getIndexes(nodeDic[nodeId], result)
            nodeIndexes = [xx.split(".")[0] for xx in nodeIndexes]
            for col in query["columns"]:
                if col in nodeIndexes:
                    item = {
                        "field": col,
                        "count": 0,
                        "values": [str(v) for v in self.checkDateFormat(_filteredResult.coords[col].values).tolist()]
                        # "values": result.filter(_filters).axis(col).values.tolist()
                    }
                    item["count"] = len(item["values"])
                    res["dims"].append(item)

            otherDims = [
                xx for xx in _filteredResult.dims if xx not in query["columns"]]
            resultValues = None
            if len(otherDims) > 0:
                resultValues = _filteredResult.sum(otherDims)
            else:
                resultValues = _filteredResult
            #resultValues = _filteredResult.sum(keep=query["columns"])

            if isinstance(resultValues, xr.DataArray):
                if len(query["columns"]) > 0:
                    res["values"] = resultValues.transpose(
                        *query["columns"]).values.reshape(resultValues.size).tolist()
                else:
                    res["values"] = [resultValues.values.tolist()]
            else:
                res["values"] = resultValues
            return res

    def getCubeDimensionValues(self, result, nodeDic, nodeId, query):
        if isinstance(result, xr.DataArray):
            if len(query["columns"]) > 0:
                dimension = query["columns"][-1]

            if (dimension+"."+nodeId) in self.getIndexes(nodeDic[nodeId], result):
                finalList = [
                    str(v) for v in self.checkDateFormat(result.coords[dimension].values).tolist()[:1000]]
                finalList.sort()
                return finalList
        return []

    def getCubeMetadata(self, result, nodeDic, nodeId):
        res = None
        if isinstance(result, xr.DataArray):
            res = {
                "dims": [],
                "measures": [],
                "aggregator": "sum",
                "isEditable": True if self.isTable(nodeDic[nodeId]) == "1" else False,
                "nodeProperties": {
                    "title": nodeDic[nodeId].title if not nodeDic[nodeId].title is None else nodeDic[nodeId].identifier,
                    "numberFormat": nodeDic[nodeId].numberFormat
                }
            }

            # check if is in scenario
            if nodeDic[nodeId].model.isNodeInScenario(nodeDic[nodeId].identifier):
                res["nodeProperties"]["scenario"] = True

            for dim in result.dims:
                indexPart = str(dim).split(".")[0]
                itemDim = {
                    "field": dim,
                    "name": indexPart
                }
                if indexPart in nodeDic:
                    if not nodeDic[indexPart].title is None:
                        itemDim["name"] = nodeDic[indexPart].title
                    if nodeDic[indexPart].numberFormat:
                        itemDim["numberFormat"] = nodeDic[indexPart].numberFormat

                res["dims"].append(itemDim)

            res["measures"].append({
                "field": "datavalue",
                "name": "datavalue"
            })

        return res

    def isTable(self, node):
        res = "0"
        if isinstance(node.result, xr.DataArray):
            if not node.definition is None and node.definition != "":
                import re
                deff = re.sub(
                    '[\s+]', '', str(node.definition).strip(' \t\n\r')).lower()
                if (deff.startswith("result=pp.dataarray(") or deff.startswith("result=pp.cube(") or deff.startswith("result=xr.dataarray(") or deff.startswith("result=create_dataarray(")):
                    res = "1"

        return res

    def setNodeValueChanges(self, nodeDic, nodeId, nodeChanges):
        if isinstance(nodeDic[nodeId].result, xr.DataArray):
            for change in nodeChanges["changes"]:
                newValue = change["definition"]
                filters = {}
                for filterItem in change["filterList"]:
                    aux = {
                        "field": filterItem["Key"],
                        "values": [{
                            "value": filterItem["Value"]
                        }]}
                    self.addToFilter(nodeDic, aux, filters)

                for key in filters:
                    filters[key] = slice(filters[key][0], filters[key][0])

                nodeDic[nodeId].result.loc[filters] = newValue

            nodeDic[nodeId].definition = self.generateNodeDefinition(
                nodeDic, nodeId)
            return "ok"

    def generateNodeDefinition(self, nodeDic, nodeId, forceXArray=False):
        array = nodeDic[nodeId].result
        """Generate code for cube definition"""
        np.set_printoptions(threshold=np.prod(array.values.shape))
        data = np.array2string(array.values, separator=",", precision=20, formatter={
                               'float_kind': lambda x: repr(x)}).replace('\n', '')

        indexes = []
        for dim in list(array.dims):
            if dim in nodeDic:
                indexes.append(dim)
            else:
                index_values = np.array2string(array[dim].values, separator=",", precision=20, formatter={
                                               'float_kind': lambda x: repr(x)}).replace('\n', '')
                coord = f"pd.Index({index_values},name='{dim}')"
                indexes.append(coord)

        indexes = "[" + ",".join(indexes).replace("'", '"') + "]"

        if forceXArray or "xr.DataArray" in nodeDic[nodeId].definition or "create_dataarray" in nodeDic[nodeId].definition:
            if self.kindToString(array.values.dtype.kind) == "string" or self.kindToString(array.values.dtype.kind) == "object":
                deff = f'result = xr.DataArray({data},{indexes}).astype("O")'
            else:
                deff = f'result = xr.DataArray({data},{indexes})'
        else:
            if self.kindToString(array.values.dtype.kind) == "string" or self.kindToString(array.values.dtype.kind) == "object":
                deff = "result = pp.cube(" + indexes + \
                    "," + data + ", dtype='O')"
            else:
                deff = "result = pp.cube(" + indexes + "," + data + ")"

        return deff

    def dumpNodeToFile(self, nodeDic, nodeId, fileName):
        definition = self.generateNodeDefinition(nodeDic, nodeId)
        with open(fileName, 'w') as f:
            f.write(definition)
            f.close()

    def applyHierarchy(self, result, nodeDic, nodeId, dims, rows, columns, sby):

        def hierarchize(dataArray, levels, maps, hierarchyDic):

            mapArray = nodeDic[maps[0]].result
            coordValues = mapArray.values.copy()
            targetIndexId = nodeDic[levels[1]].result.name

            for pos, level in enumerate(levels):
                if pos > 0:

                    if not maps[pos] is None:
                        mapArrayLevel = nodeDic[maps[pos]].result

                        for ii in range(len(coordValues)):
                            if not coordValues[ii] is None:
                                try:
                                    newVal = mapArrayLevel.sel(
                                        {mapArrayLevel.dims[0]: coordValues[ii]}, drop=True).values.item(0)
                                    coordValues[ii] = newVal
                                except Exception as ex:
                                    coordValues[ii] = None
                                    #raise ValueError("Hierarchy not found. Level: " + targetIndexId + ", value: " + coordValues[ii])
                                    pass

            # perform aggregate
            dataArray.coords[levels[0]].values = coordValues
            _df = dataArray.to_series()
            _df = _df.groupby(list(dataArray.dims), sort=False).agg(sby)
            _da = _df.to_xarray()
            reindex_dic = dict()
            for dimension in _da.dims:
                if dimension == levels[0]:
                    reindex_dic[dimension] = nodeDic[levels[-1:]
                                                     [0]].result.values
                elif dimension in nodeDic and isinstance(nodeDic[dimension].result, pd.Index):
                    node_id = dimension
                    if not hierarchyDic is None and dimension in hierarchyDic:
                        node_id = hierarchyDic[dimension]

                    reindex_dic[dimension] = nodeDic[node_id].result.values

            _db = _da.reindex(reindex_dic)

            return _db

        allDims = (dims or []) + (rows or []) + (columns or [])

        hierarchyDic = dict()
        for dim in allDims:
            if dim and dim["currentLevel"] and dim["currentLevel"] != str(dim["field"]).split(".")[0]:
                hierarchyDic[str(dim["field"]).split(".")[
                    0]] = dim["currentLevel"]

                # recursive fn for search parent

                def findPath(indexNode, level, levels, maps):
                    if indexNode.identifier == level:
                        levels.append(indexNode.identifier)
                        maps.append(None)
                        return True
                    else:
                        _for_calc = indexNode.result
                        parents = indexNode.hierarchy_parents
                        if parents is None:
                            return False
                        else:
                            if not isinstance(parents, list):
                                parents = [parents]
                            mapArrays = indexNode.hierarchy_maps
                            if not isinstance(mapArrays, list):
                                mapArrays = [mapArrays]

                            mapPos = 0
                            for parentId in parents:
                                parent = nodeDic[parentId]
                                if findPath(parent, level, levels, maps):
                                    levels.append(indexNode.identifier)
                                    maps.append(mapArrays[mapPos])
                                    return True
                                mapPos += 1
                    return False

                field = str(dim["field"]).split(".")[0]
                currentLevel = dim["currentLevel"]
                indexNode = nodeDic[field]

                levels = []
                maps = []
                findPath(indexNode, currentLevel, levels, maps)
                levels.reverse()
                maps.reverse()

                result = hierarchize(result.copy(), levels, maps, hierarchyDic)
        return result

    def geoUnclusterData(self, result, nodeDic, nodeId, rowIndex, attIndex, latField="latitude", lngField="longitude", geoField="geoField", labelField="labelField", sizeField="sizeField", colorField="colorField", iconField="iconField"):
        _tmp_for_geo = XIndex('tmp_for_geo', [
                              latField, lngField, geoField, labelField, sizeField, colorField, iconField])
        attIndex = attIndex.split(".")[0]
        rowIndex = rowIndex.split(".")[0]
        _idx = nodeDic[attIndex].result
        rowIndexObj = nodeDic[rowIndex].result
        #mapCube = result.sel({_idx.name:_tmp_for_geo}).transpose([rowIndex,"tmp_for_geo"]).values
        mapCube = XHelpers.changeIndex(None, result, _idx, _tmp_for_geo).transpose(
            *[rowIndex, "tmp_for_geo"]).values
        res = dict()
        points = []
        pos = 0
        for itemRow in mapCube:
            vo = dict()
            vo["id"] = str(rowIndexObj.values[pos])
            vo["lat"] = itemRow[0]
            vo["lng"] = itemRow[1]
            vo["geoDef"] = itemRow[2]
            vo["labelRes"] = itemRow[3]
            vo["sizeRes"] = itemRow[4]
            vo["colorRes"] = itemRow[5]
            vo["iconRes"] = itemRow[6]
            points.append(vo)
            pos += 1
        res["points"] = points

        for nn, point in enumerate(res["points"]):
            if nn == 0:
                try:
                    if not math.isnan(float(point["sizeRes"])):
                        res["minSize"] = float(point["sizeRes"])
                        res["maxSize"] = float(point["sizeRes"])
                except Exception as ex:
                    pass

                try:
                    if not math.isnan(float(point["colorRes"])):
                        res["minColor"] = float(point["colorRes"])
                        res["maxColor"] = float(point["colorRes"])
                except Exception as ex:
                    pass

                try:
                    if not math.isnan(float(point["iconRes"])):
                        res["minIcon"] = float(point["iconRes"])
                        res["maxIcon"] = float(point["iconRes"])
                except Exception as ex:
                    pass
            else:
                try:
                    if not math.isnan(float(point["sizeRes"])):
                        if point["sizeRes"] > res["maxSize"]:
                            res["maxSize"] = point["sizeRes"]
                        if point["sizeRes"] < res["minSize"]:
                            res["minSize"] = point["sizeRes"]
                except Exception as ex:
                    pass

                try:
                    if not math.isnan(float(point["colorRes"])):
                        if point["colorRes"] > res["maxColor"]:
                            res["maxColor"] = point["colorRes"]
                        if point["colorRes"] < res["minColor"]:
                            res["minColor"] = point["colorRes"]
                except Exception as ex:
                    pass

                try:
                    if not math.isnan(float(point["iconRes"])):
                        if point["iconRes"] > res["maxIcon"]:
                            res["maxIcon"] = point["iconRes"]
                        if point["iconRes"] < res["minIcon"]:
                            res["minIcon"] = point["iconRes"]
                except Exception as ex:
                    pass
        return res

    def postCalculate(self, node, result):
        """Method executed after calculate node
        """
        if isinstance(result, xr.DataArray):
            result.name = node.title

    def copyAsValues(self, result, nodeDic, nodeId):
        """ Copy node as values """

        newDef = ""
        if isinstance(result, float) or isinstance(result, int):
            newDef = "result = " + str(result)
        elif isinstance(result, xr.DataArray):
            newDef = self.generateNodeDefinition(nodeDic, nodeId, True)
        else:
            return False

        nodeDic[nodeId].definition = newDef
        return True

    def previewNode(self, nodeDic, nodeId):
        if not nodeDic[nodeId].result is None:
            _result = nodeDic[nodeId].result
            res = {
                "resultType": str(type(_result)),
                "dims": [],
                "console": nodeDic[nodeId].lastEvaluationConsole,
                "preview": ""
            }
            _preview = ""
            _preview = f"{type(_result)} - dtype: {(_result.dtype)}"
            _preview += f"\n\n{_result.coords}"
            _preview += f"\n\nTotal cells: {_result.sizes} = {_result.size} cells"
            _preview += f"\n\nSample data: \n {_result.data}"
            res["preview"] = _preview

            return json.dumps(res)
        else:
            return self.generateEmptyPreviewResponse(nodeDic, nodeId)

    def kindToString(self, kind):
        """Returns the data type on human-readable string
        """
        if kind in {'U', 'S'}:
            return "string"
        elif kind in {'b'}:
            return "boolean"
        elif kind in {'i', 'u', 'f', 'c'}:
            return "numeric"
        elif kind in {'m', 'M'}:
            return "date"
        elif kind in {'O'}:
            return "object"
        elif kind in {'V'}:
            return "void"
