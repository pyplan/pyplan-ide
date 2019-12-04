import json

import numpy as np
import pandas as pd

from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from pyplan_engine.common.classes.filterChoices import filterChoices
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq
from cubepy.cube import kindToString


class PandasEvaluator(BaseEvaluator):

    PAGESIZE = 100

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        sby = np.nansum
        if summaryBy == 'avg':
            sby = np.nanmean
        elif summaryBy == 'max':
            sby = np.nanmax
        elif summaryBy == 'min':
            sby = np.nanmin

        if (fromRow is None) or int(fromRow) <= 0:
            fromRow = 1
        if (toRow is None) or int(toRow) < 1:
            toRow = 100
        fromRow = int(fromRow)
        toRow = int(toRow)

        _filters = {}
        _rows = []
        _columns = []

        theResult = self.prepareDataframeForTable(result)

        if not rows is None:
            for row in rows:
                if self.hasDim(theResult, str(row["field"]).split(".")[0]):
                    _rows.append(str(row["field"]).split(".")[0])
                    self.addToFilter(row, _filters)

        if not columns is None:
            for column in columns:
                if self.hasDim(theResult, str(column["field"]).split(".")[0]):
                    _columns.append(str(column["field"]).split(".")[0])
                    self.addToFilter(column, _filters)

        if not dims is None:
            for dim in dims:
                if self.hasDim(theResult, str(dim["field"]).split(".")[0]):
                    self.addToFilter(dim, _filters)

        res = None
        pageInfo = None
        dfResult = None
        if len(_rows) == 0 and len(_columns) == 0:
            dfResult = self.applyFilter(theResult, _filters)

            # if have indexes sum all
            if not dfResult.index is None and not dfResult.index.names is None and len(dfResult.index.names) > 0 and not dfResult.index.names[0] is None:
                serieResult = dfResult.agg(sby)
                dfResult = pd.DataFrame({"total": serieResult}).T

        else:
            needT = False
            if len(_rows) == 0:
                needT = True
                aux = _rows
                _rows = _columns
                _columns = aux

            _filteredDataFrame = self.applyFilter(theResult, _filters)

            # Don't use margins = True to obtain totals. This have a bug for dataframes with more than 5 level indexes
            dfResult = pd.DataFrame.pivot_table(
                _filteredDataFrame, index=_rows, columns=_columns, aggfunc=sby, margins=False, margins_name="Total")

            if needT:
                dfResult = dfResult.T
                aux = _rows
                _rows = _columns
                _columns = aux

            if bottomTotal and dfResult.shape[0] > 1:
                row_total = sby(dfResult.values, axis=0)
                new_values = np.concatenate(
                    [dfResult.values, [row_total]], axis=0)
                new_index = pd.Index(np.concatenate(
                    [dfResult.index.values, ["Total"]]))
                _df = pd.DataFrame(
                    data=new_values, columns=dfResult.columns, index=new_index)
                dfResult = _df

            if rightTotal and dfResult.shape[1] > 1:
                row_total = sby(dfResult.values, axis=1)
                new_values = np.concatenate(
                    [dfResult.values, row_total.reshape(row_total.size, 1)], axis=1)
                new_columns = np.concatenate([dfResult.columns, ["Total"]])
                _df = pd.DataFrame(
                    data=new_values, columns=new_columns, index=dfResult.index)
                dfResult = _df

        if (dfResult.shape[0] > self.PAGESIZE):
            if int(toRow) > dfResult.shape[0]:
                toRow = dfResult.shape[0]
            pageInfo = {
                "fromRow": int(fromRow),
                "toRow": int(toRow),
                "totalRows": dfResult.shape[0]
            }
            #res = dfResult[fromRow-1:toRow].to_json(orient='split')
            _range = list(range(fromRow-1, toRow))
            if bottomTotal:
                _range = _range + [len(dfResult)-1]
            res = dfResult.iloc[_range].to_json(
                orient='split', date_format='iso')
        else:
            res = dfResult[:300].to_json(orient='split', date_format='iso')

        return self.createResult(res, type(theResult), resultIsJson=True, pageInfo=pageInfo, node=nodeDic[nodeId],  onRow=(_rows[0] if len(_rows) > 0 else None), onColumn=(_columns[0] if len(_columns) > 0 else None))

    def addToFilter(self, dim, filters):
        if "values" in dim and dim["values"] is not None and len(dim["values"]) > 0:
            for itemValue in dim["values"]:
                field = str(dim["field"]).split(".")[0]
                # if (field in filters):
                #     filters[field] += " or " + field + "==" + "'" + itemValue["value"] + "'"
                # else:
                #     filters[field] = "( " + field + "==" + "'" + itemValue["value"] + "'"
                if (field in filters):
                    filters[field].append(itemValue["value"])
                else:
                    filters[field] = [itemValue["value"]]

    def applyFilter(self, result, filters):
        if not result is None:
            if len(filters) > 0:
                res = result
                for key in filters:
                    res = res[res.index.get_level_values(
                        key).isin(filters[key])]
                return res
            else:
                return result

    def hasDim(self, result, dim):
        if dim in result.index.names:
            return True
        elif dim in result.dtypes.index:
            return True
        elif dim in result.columns:
            return True
        else:
            return False

    def isIndexed(self, result):
        if not result is None:
            result = self.prepareDataframeForTable(result)
            obj = result
            if isinstance(obj, pd.DataFrame):
                return self._isIndexedDataframe(obj)
        return False

    def getIndexes(self, node, result=None):
        res = []
        if not node._result is None:

            obj = self.prepareDataframeForTable(node._result)
            if isinstance(obj, pd.DataFrame):
                if self.isIndexed(obj):
                    res = list(obj.index.names)
                    res = [x + "." + node.identifier for x in res]

        return res

    def getIndexesWithLevels(self, node, result=None):
        res = []
        if result is None:
            result = node._result

        if not result is None:
            result = self.prepareDataframeForTable(result)

            if self.isIndexed(result):
                for indexItem in result.index.names:
                    itemDim = indexItem.split(",")[0]
                    item = {"field": itemDim+"."+node.identifier,
                            "name": itemDim, "description": "", "levels": []}

                    if node.model.existNode(itemDim):
                        levelNode = node.model.getNode(itemDim)
                        if levelNode.title:
                            item["name"] = levelNode.title
                            item["description"] = levelNode.description
                        if levelNode.numberFormat:
                            item["numberFormat"] = levelNode.numberFormat
                    else:
                        # try generate default formatter
                        if "datetime" in result.index.get_level_values(itemDim).dtype.name:
                            item["numberFormat"] = "2,DD,0,,0,0,4,0,$,5,FULL,0"

                    res.append(item)
        return res

    def getIndexValues(self, nodeDic, data: IndexValuesReq, result=None):
        res = []
        if data.node_id:
            if (not data.node_id is None) & (data.node_id in nodeDic):
                node = nodeDic[data.node_id]
                if result is None:
                    result = node.result
                if (f"{data.index_id}.{data.node_id}") in self.getIndexes(node):
                    if self.isIndexed(result):
                        prepared_result = self.prepareDataframeForTable(
                            node.result)
                        for index in prepared_result.index.levels:
                            if index.name == data.index_id:
                                res = self.checkDateFormat(
                                    index.values).tolist()
                                break
                    else:
                        res = result[data.index_id].unique().tolist()
        elif data.index_id:
            if result is None:
                result = nodeDic[data.index_id].result
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
        if nodeId:
            if (not nodeId is None) & (nodeId in nodeDic):
                node = nodeDic[nodeId]
                nodeIndexes = self.getIndexes(node)
                if (indexId+"."+nodeId) in nodeIndexes:
                    if self.isIndexed(node.result):
                        prepared_result = self.prepareDataframeForTable(
                            node.result)
                        for index in prepared_result.index.levels:
                            if index.name == indexId:
                                res = "S"
                                break
                    else:
                        #res = list(node.result[indexId].unique())[:1000]
                        res = "S"
                elif indexId in nodeIndexes and isinstance(node.result, cubepy.Cube):
                    if str(node.result.axis(indexId).values.dtype) in numerics:
                        res = "N"
                    else:
                        res = "S"
        return res

    def getCubeMetadata(self, result, nodeDic, nodeId):
        res = None

        _result = self.prepareDataframeForPivot(result)

        if isinstance(_result, pd.DataFrame):
            res = {
                "dims": [],
                "measures": [],
                "aggregator": "sum",
                "isEditable": False,
                "nodeProperties": {
                    "title": nodeDic[nodeId].title if not nodeDic[nodeId].title is None else nodeDic[nodeId].identifier,
                    "numberFormat": nodeDic[nodeId].numberFormat
                }
            }

            for dim in self.getCubeIndexes(_result, nodeDic, nodeId):
                field = dim.split(".")[0]
                itemDim = {
                    "field": dim,
                    "name": field
                }
                if field in nodeDic:
                    if nodeDic[field].numberFormat:
                        itemDim["numberFormat"] = nodeDic[field].numberFormat
                else:
                    if "datetime" in _result.index.get_level_values(field).dtype.name:
                        itemDim["numberFormat"] = "2,DD,0,,0,0,4,0,$,5,FULL,0"
                res["dims"].append(itemDim)

            res["dims"].append({
                "field": "data_index",
                "name": "Data Index"
            })

            numerics = ['int16', 'int32', 'int64',
                        'float16', 'float32', 'float64']

            for col in _result.columns:
                res["measures"].append({
                    "field": str(col),
                    "name": str(col)
                })

            _result = None
        return res

    def getCubeIndexes(self, result, nodeDic, nodeId):
        res = list(result.index.names)
        res = [x + "." + nodeDic[nodeId].identifier for x in res]
        return res

    def getCubeValues(self, result, nodeDic, nodeId, query):

        _result = self.prepareDataframeForPivot(result)

        if isinstance(_result, pd.DataFrame):
            cube_indexes = self.getCubeIndexes(_result, nodeDic, nodeId)
            _filters = {}
            if not query["filters"] is None:
                for dim in query["filters"]:
                    if "values" in dim and dim["values"] is not None and len(dim["values"]) > 0:
                        for itemValue in dim["values"]:
                            field = str(dim["field"]).split(".")[0]
                            if (field in _filters):
                                _filters[field].append(itemValue)
                            else:
                                _filters[field] = [itemValue]

            _filteredResult = self.applyFilter(_result, _filters)
            for col in query["columns"]:
                if col in cube_indexes:
                    item = {
                        "field": col,
                        "count": 0,
                        "values": _filteredResult.index.get_level_values(col.split(".")[0]).unique().tolist()
                    }
                    # "values": _filteredResult[col.split(".")[0]].unique().tolist()
                    item["count"] = len(item["values"])

            _cols = [x.split(".")[0] for x in query["columns"]]
            if len(_cols) == 0:
                listResult = _filteredResult[query["measures"]].sum(
                ).reset_index().values.tolist()
                if len(listResult) > 0 and len(listResult[0]) > 1:
                    if np.isinf(listResult[0][1]):
                        listResult[0][1] = None
                return [["data_index", "data_value"]] + listResult
            else:
                """
                # cambiado por lo de abajo para tome columnas con string
                dfValues = pd.DataFrame.pivot_table(_filteredResult, index=_cols, aggfunc=np.sum)
                firstCol = query["columns"] + ["data_index","data_value"]
                res = [firstCol] + dfValues.reset_index().melt(id_vars=_cols,  value_vars=query["measures"]).values.tolist()
                return res
                """

                """
                @cambiado por lo de abajo para permitir multiples agrupaciones por medida...muy picante
                t1= _filteredResult.stack() 
                t1.index.set_names("data_index",level=t1.index.nlevels-1,inplace=True)
                t2 = t1.iloc[t1.index.get_level_values("data_index").isin(query["measures"]) ].reset_index()[_cols + ["data_index",0]]  

                firstCol = query["columns"] + ["data_index","data_value"]
                t3 = t2.groupby( _cols + ["data_index"]).aggregate({0:"sum"}).reset_index()
                res = [firstCol] + t3.values[:10000].tolist()
                t1=None
                t2=None
                t3=None
                _result = None
                return res

                @cambiado por lo de abajo para permitir custom measures ... extra picante
                """
                _measures = list(query["measures"])
                useCustomFillMeasures = False
                try:
                    # test if have groupMeasures property
                    _aa = _result.groupMeasures
                    useCustomFillMeasures = True
                except AttributeError as ex:
                    pass

                _groupedDF = None
                if useCustomFillMeasures:
                    _groupedDF = _filteredResult.groupby(
                        _cols, sort=False).sum()
                else:
                    _agg = dict()
                    for measure in _measures:
                        # TODO: POR AHORA sum, Mas adelante tomar de la query el tipo de agrupamiento
                        _agg[measure] = "sum"
                    _groupedDF = _filteredResult.groupby(
                        _cols, sort=False).agg(_agg)

                if useCustomFillMeasures:
                    for key in _result.groupMeasures:
                        _groupedDF[key] = _result.groupMeasures[key](
                            _groupedDF)

                finalDF = _groupedDF.reset_index().melt(id_vars=_cols,
                                                        value_vars=query["measures"], var_name="data_index", value_name="data_value")

                # fill inf values only if is numeric
                _kind = finalDF["data_value"].dtype.kind
                if _kind in {'i', 'u', 'f', 'c'}:
                    if np.isinf(finalDF["data_value"]).any():
                        finalDF["data_value"][np.isinf(
                            finalDF["data_value"])] = 0

                # fill nan values
                finalDF["data_value"].fillna(0, inplace=True)

                firstCol = query["columns"] + ["data_index", "data_value"]
                sortedColumns = [
                    x.split(".")[0] for x in query["columns"]] + ["data_index", "data_value"]
                res = [firstCol] + \
                    finalDF[sortedColumns].values[:1000000].tolist()
                _result = None
                return res

    def getCubeDimensionValues(self, result, nodeDic, nodeId, query):
        _result = self.prepareDataframeForPivot(result)

        if isinstance(_result, pd.DataFrame):
            if len(query["columns"]) > 0:
                dimension = query["columns"][-1]

            if dimension in nodeDic[nodeId].indexes:
                #uniquelist = _result[dimension.split(".")[0]].unique()
                uniquelist = _result.index.get_level_values(
                    dimension.split(".")[0]).unique()
                # uniquelist.sort()
                return uniquelist.sort_values().tolist()[:1000]

        return []

    def previewNode(self, nodeDic, nodeId):
        from pyplan_engine.classes.Helpers import Helpers
        from sys import getsizeof
        res = {
            "resultType": str(type(nodeDic[nodeId].result)),
            "dims": [],
            "columns": [],
            "console": nodeDic[nodeId].lastEvaluationConsole,
            "preview": ""
        }
        if isinstance(nodeDic[nodeId].result, pd.DataFrame):
            cube = nodeDic[nodeId].result

            if self.isIndexed(cube):
                res["dims"] = list(cube.index.names)

            for idx, col in enumerate(cube.columns.values[:500]):
                res["columns"].append(
                    str(col) + " (" + kindToString(cube.dtypes[idx].kind) + ")")

            res["preview"] += "Rows: " + str(len(cube.index))
            #res += "\nColumns: " + ', '.join([''.join(row) for row in cube.columns.values[:500]])
            res["preview"] += "\nShape: " + str(cube.shape)
            res["preview"] += "\nMemory: " + \
                str(round(cube.memory_usage(deep=True).sum() / 1024/1024, 2)) + " Mb"
            #res["preview"] += "\nValues: \n" + str(cube.head(20))
            res["preview"] += "\nValues: \n" + cube.head(20).to_string()
        elif isinstance(nodeDic[nodeId].result, pd.Series):
            serie = nodeDic[nodeId].result
            if self.isIndexed(serie):
                res["dims"] = list(serie.index.names)
            res["preview"] += "Rows: " + str(len(serie.index))
            res["preview"] += "\nMemory: " + \
                str(round(serie.memory_usage(deep=True) / 1024/1024, 2)) + " Mb"
            #res["preview"] += "\nValues: \n" + str(serie.head(20))
            res["preview"] += "\nValues: \n" + serie.head(20).to_string()
        elif isinstance(nodeDic[nodeId].result, pd.Index):
            res["preview"] = str(nodeDic[nodeId].result)[:1000]

        return json.dumps(res)

    def ensureDataFrame(self, result):
        res = result
        if isinstance(res, pd.Series):
            res = pd.DataFrame({"values": res})
        return res

    def exportFlatNode(self, nodeDic, nodeId, numberFormat, columnFormat, fileName):
        if columnFormat == "tab":
            columnFormat = "\t"

        decimalSep = "."
        if numberFormat == 'TSPDSC':
            decimalSep = ","

        _result = self.ensureDataFrame(nodeDic[nodeId].result)

        if isinstance(_result, pd.DataFrame):
            _result.to_csv(fileName, sep=columnFormat, encoding="iso-8859-1")

            return True

        return False

    def postCalculate(self, node, result):
        """Method executed after calculate node
        """
        if node.nodeClass == "index":
            if isinstance(result, pd.Index) and result.name is None:
                result.name = node.identifier

    def copyAsValues(self, result, nodeDic, nodeId):
        """ Copy node as values """

        newDef = ""
        if isinstance(result, pd.Index):
            np.set_printoptions(threshold=np.prod(result.values.shape))
            values = np.array2string(result.values, separator=",", precision=20, formatter={
                                     'float_kind': lambda x: repr(x)}).replace('\n', '')
            newDef = f"result = pd.Index({values})"
        else:
            return False

        nodeDic[nodeId].definition = newDef
        return True

    def _isIndexedDataframe(self, dataframe):
        """Return True if dataframe is an indexed dataframe"""
        return len(dataframe.index.names) > 1 or not dataframe.index.names[0] is None

    def prepareDataframeForTable(self, result):
        """ Prepare dataframe for use un tables and charts """
        df = result
        if isinstance(df, pd.Series):
            df = pd.DataFrame({"values": df})

        if self._isIndexedDataframe(df):
            if df.size == 0:
                df["values"] = np.nan
            elif len(df.columns) > 1:
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.map(' | '.join)
                df = df.stack()
                if isinstance(df, pd.Series):
                    df = pd.DataFrame({"values": df})
                current_columns_name = list(df.index.names)
                current_columns_name[len(current_columns_name)-1] = "Measures"
                df.index.names = current_columns_name

        return df

    def prepareDataframeForPivot(self, result):
        """ Prepare dataframe for use in pivot cube"""
        df = result
        if isinstance(df, pd.Series):
            df = pd.DataFrame({"values": df})
        if self._isIndexedDataframe(df):
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.map(' | '.join)
            df = df.select_dtypes(include=['float64', 'int64'])
            if df.size == 0:
                df["values"] = np.nan
            # try to keep group measures
            try:
                df.groupMeasures = result.groupMeasures
            except:
                pass
        return df
