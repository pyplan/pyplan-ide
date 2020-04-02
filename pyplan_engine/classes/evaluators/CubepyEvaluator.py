import json

import numpy as np
import pandas as pd
import xarray as xr

import cubepy
from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from pyplan_engine.common.classes.filterChoices import filterChoices
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq
from cubepy.cube import kindToString, safemax, safemean, safemin, safesum


class CubepyEvaluator(BaseEvaluator):

    PAGESIZE = 100
    MAX_COLUMS = 5000

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        if isinstance(result, cubepy.Cube):
            return self.cubeEvaluate(result, nodeDic, nodeId, dims, rows, columns, summaryBy, bottomTotal, rightTotal, fromRow, toRow)
        elif isinstance(result, cubepy.Index):
            return self.indexEvaluate(result, nodeDic, nodeId, dims, rows, columns, summaryBy, bottomTotal, rightTotal, fromRow, toRow)

    def cubeEvaluate(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        result_structure = self.getStructure(result)
        sby = safesum
        if summaryBy == 'avg':
            sby = safemean
        elif summaryBy == 'max':
            sby = safemax
        elif summaryBy == 'min':
            sby = safemin

        if (fromRow is None) or int(fromRow) <= 0:
            fromRow = 1
        if (toRow is None) or int(toRow) < 1:
            toRow = 100
        fromRow = int(fromRow)
        toRow = int(toRow)

        result = self.applyHierarchy(
            result, nodeDic, nodeId, dims, rows, columns, sby)

        _filters = []
        _rows = []
        _columns = []
        if not rows is None:
            for row in rows:
                if self.hasDim(result, str(row["field"])):
                    _rows.append(str(row["field"]))
                    self.addToFilter(nodeDic, row, _filters)

        if not columns is None:
            for column in columns:
                if self.hasDim(result, str(column["field"])):
                    _columns.append(str(column["field"]))
                    self.addToFilter(nodeDic, column, _filters)

        if not dims is None:
            for dim in dims:
                if self.hasDim(result, str(dim["field"])):
                    self.addToFilter(nodeDic, dim, _filters)

        tmp = None
        if len(_rows) == 0 and len(_columns) == 0 and result.ndim > 0:
            #_rows.append( result.dims[0] )
            tmp = cubepy.Cube([], result.filter(_filters).reduce(sby))

        else:
            tmp = result.filter(_filters).reduce(sby, keep=(
                _rows + _columns)).transpose(_rows + _columns)

        finalValues = tmp.values
        finalIndexes = []
        if tmp.ndim > 0:
            finalIndexes = tmp.axes[0].values
        finalColumns = ["Total"]
        if tmp.ndim == 2:
            finalColumns = tmp.axes[1].values

        # Add totales
        _totalRow = None
        if bottomTotal and len(_rows) > 0:
            # add total row
            #finalIndexes = np.append(finalIndexes,"Total")
            if tmp.ndim == 1:
                _totalRow = finalValues.sum(axis=0).reshape(1)
                #finalValues = np.append( finalValues, finalValues.sum(axis=0).reshape(1), axis=0)
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

            # con una sola dimension

        # chek inf
        if kindToString(finalValues.dtype.kind) == "numeric":
            if np.isinf(finalValues).any():
                finalValues[np.isinf(finalValues)] = None

        # chec if haver nan values
        # if np.isnan(finalValues).any():
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
                "columns": finalIndexes[:CubepyEvaluator.MAX_COLUMS].tolist(),
                "index": finalColumns,
                "data": [finalValues[:CubepyEvaluator.MAX_COLUMS].tolist()]
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
                "index": finalIndexes[fromRow-1:toRow].tolist(),
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
                "columns": finalColumns[:CubepyEvaluator.MAX_COLUMS].tolist(),
                "index": finalIndexes[fromRow-1:toRow].tolist(),
                "data": finalValues[fromRow-1:toRow, :CubepyEvaluator.MAX_COLUMS].tolist()
            }

            # add total rows
            if not _totalRow is None:
                res["index"].append("Total")
                res["data"].append(
                    _totalRow[:CubepyEvaluator.MAX_COLUMS].tolist())

        return self.createResult(res, result_structure, onRow=onRow, onColumn=onColumn, node=nodeDic[nodeId], pageInfo=pageInfo)

    def applyHierarchy(self, result, nodeDic, nodeId, dims, rows, columns, sby):

        def hierarchize(cube, levels, maps):

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
                                    newVal = mapArrayLevel.filter(
                                        mapArrayLevel.dims[0], coordValues[ii]).values.item(0)
                                    coordValues[ii] = newVal
                                except Exception as ex:
                                    coordValues[ii] = None
                                    #raise ValueError("Hierarchy not found. Level: " + targetIndexId + ", value: " + coordValues[ii])
                                    pass

            # convert to dataarray
            _coords = []
            for _axis in cube.axes:
                _coord = pd.Index(_axis.values, name=_axis.name)
                _coords.append(_coord)
            dataArray = xr.DataArray(cube.values, _coords)

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
                elif dimension in nodeDic and isinstance(nodeDic[dimension].result, cubepy.Index):
                    reindex_dic[dimension] = nodeDic[dimension].result.values

            _db = _da.reindex(reindex_dic)

            # convert to cube
            _indexes = []
            for _dim in _db.dims:
                _index = cubepy.Index(_dim, _db.coords[_dim].values)
                _indexes.append(_index)
            _cube = cubepy.Cube(_indexes, _db.values)

            return _cube

        allDims = (dims or []) + (rows or []) + (columns or [])

        for dim in allDims:
            if dim and dim["currentLevel"] and dim["currentLevel"] != str(dim["field"]).split(".")[0]:
                # Find the path for the current level

                # recursive fn for search parent
                def findPath(indexNode, level, levels, maps):
                    if indexNode.identifier == level:
                        levels.append(indexNode.identifier)
                        maps.append(None)
                        return True
                    else:
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

                result = hierarchize(cubepy.cube.Cube(
                    result._axes, result._values), levels, maps)
        return result

    def indexEvaluate(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        res = result.values[:100].tolist()
        return self.createResult(res, self.getStructure(res), node=nodeDic[nodeId])

    def addToFilter(self, nodeDic, dim, filters):
        if "values" in dim and dim["values"] is not None and len(dim["values"]) > 0:
            #field = str(dim["field"]).split(".")[0]
            field = str(dim["field"])
            nodeId = None
            # if len(str(dim["field"]).split("."))>1:
            #     nodeId = str(dim["field"]).split(".")[1]
            indexType = None
            # is from numpy evaluator
            if "." in field and field.startswith("Axis"):
                indexType = "N"
            else:
                indexType = self.getIndexType(nodeDic, nodeId, field)

            if indexType == "S":
                filters.append(cubepy.Index(
                    field,  [str(v["value"]) for v in dim["values"]]))
            else:
                filters.append(cubepy.Index(
                    field,  [int(v["value"]) for v in dim["values"]]))

    def getCubeValues(self, result, nodeDic, nodeId, query):
        if isinstance(result, cubepy.Cube):
            res = {
                "dims": [],
                "values": []
            }

            _filters = []
            if not query["filters"] is None:
                for dimFilter in query["filters"]:
                    #field = str(dimFilter["field"]).split(".")[0]
                    field = str(dimFilter["field"])
                    if self.hasDim(result, field):
                        indexType = None
                        # is from numpy evaluator
                        if "." in field and field.startswith("Axis"):
                            indexType = "N"
                        else:
                            indexType = self.getIndexType(
                                nodeDic, nodeId, field)

                        if indexType == "S":
                            _filters.append(cubepy.Index(
                                field,  [str(v) for v in dimFilter["values"]]))
                        else:
                            _filters.append(cubepy.Index(
                                field,  [int(v) for v in dimFilter["values"]]))

            _filteredResult = result.filter(_filters)
            for col in query["columns"]:
                if col in self.getIndexes(nodeDic[nodeId], result):
                    item = {
                        "field": col,
                        "count": 0,
                        "values": [str(v) for v in _filteredResult.axis(col).values.tolist()]
                        # "values": result.filter(_filters).axis(col).values.tolist()
                    }
                    item["count"] = len(item["values"])
                    res["dims"].append(item)

            resultValues = _filteredResult.sum(keep=query["columns"])
            if isinstance(resultValues, cubepy.Cube):
                res["values"] = resultValues.transpose(
                    query["columns"]).values.reshape(resultValues.size).tolist()
            elif isinstance(resultValues, str):
                res["values"] = [resultValues]
            else:
                res["values"] = resultValues
            return res

    def getCubeDimensionValues(self, result, nodeDic, nodeId, query):
        if isinstance(result, cubepy.Cube):
            if len(query["columns"]) > 0:
                dimension = query["columns"][-1]

            if dimension in self.getIndexes(nodeDic[nodeId], result):
                finalList = [str(v) for v in result.axis(
                    dimension).values.tolist()[:1000]]
                finalList.sort()
                return finalList
        return []

    def getCubeMetadata(self, result, nodeDic, nodeId):
        res = None
        if isinstance(result, cubepy.Cube):
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
                itemDim = {
                    "field": dim,
                    "name": str(dim).split(".")[0]
                }
                if dim in nodeDic:
                    if not nodeDic[dim].title is None:
                        itemDim["name"] = nodeDic[dim].title
                res["dims"].append(itemDim)

            res["measures"].append({
                "field": "datavalue",
                "name": "datavalue"
            })

        return res

    def setNodeValueChanges(self, nodeDic, nodeId, nodeChanges):
        if isinstance(nodeDic[nodeId].result, cubepy.Cube):
            for change in nodeChanges["changes"]:
                newValue = change["definition"]
                filters = []
                for filterItem in change["filterList"]:
                    aux = {
                        "field": filterItem["Key"],
                        "values": [{
                            "value": filterItem["Value"]
                        }]}
                    self.addToFilter(nodeDic, aux, filters)
                nodeDic[nodeId].result.set_data(filters, newValue)
                # generate and put new definition bypass clear result
                newDeff = nodeDic[nodeId].result.generateDefinition()
                nodeDic[nodeId].definition = newDeff

            return "ok"

    def isTable(self, node):
        res = "0"
        if isinstance(node.result, cubepy.Cube):
            if not node.definition is None and node.definition != "":
                import re
                deff = re.sub(
                    '[\s+]', '', str(node.definition).strip(' \t\n\r')).lower()
                if (deff.startswith("this=cubepy.cube(") or deff.startswith("result=cubepy.cube(")
                        or deff.startswith("this=cp.cube(") or deff.startswith("result=cp.cube(")
                        or deff.startswith("this=cubepy.cube.zeros(") or deff.startswith("result=cubepy.cube.zeros(")
                        or deff.startswith("this=cubepy.cube.ones(") or deff.startswith("result=cubepy.cube.ones(")
                        or deff.startswith("this=cubepy.cube.full(") or deff.startswith("result=cubepy.cube.full(")):
                    res = "1"
        elif isinstance(node.result, np.ndarray):
            if not node.definition is None and node.definition != "":
                import re
                deff = re.sub(
                    '[\s+]', '', str(node.definition).strip(' \t\n\r')).lower()
                if (deff.startswith("result=np.")):
                    res = "1"

        return res

    def hasDim(self, result, dim):
        return True if dim in result.dims else False

    def getIndexes(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        if isinstance(result, cubepy.Cube):
            res = list(result.dims)
        return res

    def getIndexesWithLevels(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        if isinstance(result, cubepy.Cube):
            if not result is None:
                _model = node.model
                for indexItem in result.dims:
                    itemDim = indexItem
                    item = {"field": itemDim, "name": itemDim,
                            "description": "", "levels": []}

                    if node.model.existNode(itemDim):
                        levelNode = node.model.getNode(itemDim)
                        if levelNode.title:
                            item["name"] = levelNode.title
                            item["description"] = levelNode.description

                        # check for levels
                        if not levelNode.hierarchy_parents is None:

                            def buildLevels(parents, levelList):
                                if not isinstance(parents, list):
                                    parents = [parents]
                                for parentIndexId in parents:
                                    parentIndexNode = _model.getNode(
                                        parentIndexId)
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
                    res.append(item)

        return res

    def getIndexType(self, nodeDic, nodeId, indexId):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        res = "S"
        if (not indexId is None) & (indexId in nodeDic):
            node = nodeDic[indexId]
            if isinstance(node.result, cubepy.Index):
                if str(node.result.values.dtype) in numerics:
                    res = "N"
                else:
                    res = "S"
            elif isinstance(node.result, np.ndarray):
                if str(node.result.dtype) in numerics:
                    res = "N"
                else:
                    res = "S"
            else:
                res = "S"
        return res

    def getIndexValues(self, nodeDic, data: IndexValuesReq, result=None):
        res = []
        if (not data.index_id is None) & (data.index_id in nodeDic):
            node = nodeDic[data.index_id]
            if isinstance(node.result, cubepy.Index):
                res = (node.result.values).tolist()
            elif isinstance(node.result, np.ndarray):
                res = (node.result).tolist()
            else:
                res = list(node.result)
        if data.text1:
            text1 = data.text1.lower()
            if data.filter == filterChoices.CONTAINS.value:
                res = list(
                    filter(lambda item: text1 in str(item).lower(), res))
            elif data.filter == filterChoices.NOT_CONTAINS.value:
                res = list(
                    filter(lambda item: not text1 in str(item).lower(), res))
        return res

    def previewNode(self, nodeDic, nodeId):
        from pyplan_engine.classes.Helpers import Helpers
        from sys import getsizeof
        res = {
            "resultType": str(type(nodeDic[nodeId].result)),
            "dims": [],
            "console": nodeDic[nodeId].lastEvaluationConsole,
            "preview": ""
        }
        if isinstance(nodeDic[nodeId].result, cubepy.Cube):
            cube = nodeDic[nodeId].result
            for _axis in cube.axes:
                _nodeTitle = None
                if _axis.name in nodeDic:
                    _nodeTitle = nodeDic[_axis.name].title

                if _nodeTitle is None:
                    _item = _axis.name + " [" + str(len(_axis)) + "]"
                else:
                    _item = _nodeTitle + \
                        " ("+_axis.name+") [" + str(len(_axis)) + "]"
                res["dims"].append(_item)

            res["preview"] += "Dimensions: " + str(cube.ndim)
            res["preview"] += "\nShape: " + str(cube.shape)
            res["preview"] += "\nSize: " + str(cube.size)
            res["preview"] += "\nMemory: " + \
                str(round(getsizeof(cube)/1024/1024, 2)) + " Mb"
            if not cube.values is None:
                res["preview"] += "\nData type: " + \
                    str(cube.values.dtype) + \
                    " (" + kindToString(cube.values.dtype.kind)+")"
                res["preview"] += "\nValues: \n\n" + str(cube.values)[:1000]

        elif isinstance(nodeDic[nodeId].result, cubepy.Index):
            index = nodeDic[nodeId].result

            res["preview"] += "Size: " + str(len(index))
            res["preview"] += "\nMemory: " + \
                str(round(getsizeof(index)/1024/1024, 2)) + " Mb"
            if not index.values is None:
                res["preview"] += "\nData type: " + \
                    str(index.values.dtype) + \
                    " (" + kindToString(index.values.dtype.kind)+")"
                #res["preview"] += "\nValues: \n" + '\n\t'.join([''.join(row) for row in index.values[:100]])
                res["preview"] += "\nValues: \n\t" + \
                    '\n\t'.join([''.join(str(row))
                                 for row in index.values[:100]])

        return json.dumps(res)

    def dumpNodeToFile(self, nodeDic, nodeId, fileName):
        definition = nodeDic[nodeId].result.generateDefinition()
        with open(fileName, 'w') as f:
            f.write(definition)
            f.close()

    def geoUnclusterData(self, result, nodeDic, nodeId, rowIndex, attIndex, latField="latitude", lngField="longitude", geoField="geoField", labelField="labelField", sizeField="sizeField", colorField="colorField", iconField="iconField"):
        latField = "latitude" if latField is None else latField
        lngField = "longitude" if lngField is None else lngField
        geoField = "geoField" if geoField is None else geoField
        labelField = "labelField" if labelField is None else labelField
        sizeField = "sizeField" if sizeField is None else sizeField
        colorField = "colorField" if colorField is None else colorField
        iconField = "iconField" if iconField is None else iconField

        _tmp_for_geo = cubepy.Index('tmp_for_geo', [
                                    latField, lngField, geoField, labelField, sizeField, colorField, iconField])
        _idx = nodeDic[attIndex].result
        rowIndexObj = nodeDic[rowIndex].result
        mapCube = result[_idx == _tmp_for_geo].transpose(
            [rowIndex, "tmp_for_geo"]).values
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

        return res
