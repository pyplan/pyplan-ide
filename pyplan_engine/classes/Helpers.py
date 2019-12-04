import inspect
import numbers
import os
from sys import exc_info, getsizeof

import numpy as np
import numpydoc
import pandas as pd

import cubepy
import cubepy.factory as cpf


class Helpers(object):

    random = -123798
    exact = 1
    start_with = 2
    end_with = 3
    contain = 4
    byVal = 1
    byPos = 2

    @property
    def currentNodeId(self):
        return self.node.identifier

    def __init__(self, node):
        self.node = node

    def release(self):
        self.node = None

    def cube(self, axes, values=None, broadcast=True, dtype=None):
        """Create a cube  object. 
        axes: list of axis of the cube
        values: optional, list of values of the cube. Can be other cubes for build a report.
        Ex.
            cp.cube([time])
            cp.cube([time,product])
            cp.cube([time,product],[10,20,30,40,50,60,70,80])
            cp.cube([time,product],cp.random)

            cp.cube([index_reports],[report_1,report_2])
        """
        return cpf.cube(axes, values, broadcast, dtype)

    def index(self, values):
        """Create a index object.
        values: list of values of the index.
        Ex.
            cp.index(["Item 1","Item 2","Item 3"])
            cp.index([2016,2017,2018])
        """
        return cpf.index(self.node.identifier, values)

    def find(self, param1, param2, compareType=1, caseSensitive=True):
        """
        param1: value or indexarray for compare
        param2: index compare to
        compareType: cp.exact=1, cp.start_with=2, cp.end_with=3, cp.contain=4  
        caseSensitive: able to differentiate between uppercase and lowercase (by default True)

        If param1 is a scalar (numeric or str) and param2 is an index:  return cube indexed by param2 with True on ocurrences of param2
            Ex. result = cp.apply("te", region, cp.end_with)
        If param1 is an index and param2 is an index too:  return cube indexed by param1 and param2 with True on ocurrences of param1 on param2
            Ex. result = cp.apply(subregion, region, cp.contain)

        """
        return cpf.find(param1, param2, compareType, caseSensitive)

    def selectText(self, data, first=None, last=None):
        """Returns a new cube with the text contained between the 'first' and 'last' characters of cube / index 'data'. Starts counting from 0.
                If 'first' character is ommited, it returns every character from the first character of 'data' to the 'last' character, inclusive.
                If 'last' character is ommited, it returns every character from "first" character of 'data', to the last character available for each cell.
        """
        return cpf.selectText(data, first, last)

    def apply(self, fn, param1, param2=None, start=None):
        """
        Apply functions to index and cubes. Multiple results can be obtained
        fn: function to apply
        param1: index or cube
        param2: index or cube
        start: scalar or cube
            Ex. 
                cp.apply(lambda x: x[:2] ,indexRegion): return new cube indexed by "indexRegion" and apply fn on each item
                cp.apply(lambda x: x*5 ,cubeSales): return new cube result of apply fn on all values of the cubeSales
                cp.apply( cp.addPeriods, start_proj , end_proj): Return new cube result of apply fn on "start_proj" with "end_proj"
                cp.apply(lambda x: x+1, indexYear, start=10) : Return new cube indexed by "indexYear", result of apply fn starting with scalar value "10"
                cp.apply(lambda x: x+1, indexYear, start=prices) : Return new cube indexed by "indexYear", result of apply fn starting with cube "prices"
        """
        return cpf.apply(fn, param1, param2, start)

    def max(self, cube1, cube2):
        """Return max value between two cubes
        """
        return cpf.max(cube1, cube2)

    def min(self, cube1, cube2):
        """Return min value between two cubes
        """
        return cpf.min(cube1, cube2)

    def sum(self, cube, axis=None, keep=None, group=None, sort_grp=True):
        """Sum of array elements over a given axis.
        :param axis: Axis or axes along which a sum is performed. The default (axis = None) is perform a sum
        over all the dimensions of the input array. axis may be negative, in which case it counts from the last
        to the first axis. If this is a tuple of ints, a sum is performed on multiple axes, instead of a single
        axis or all the axes as before.
        :return: new Cube instance or a scalar value
        """
        return cpf.sum(cube, axis, keep, group, sort_grp)

    def subscript(self, cube, index, value):
        """Filter cube1 using the index and the value. Return a new cube without the index1 dimension
            Ex.
                cp.subscript(nodo_ejemplo,index_para_ejemplo,"Item 1")
        """
        if isinstance(index, str):
            index = self.node.model.getNode(index)
        return cpf.subscript(cube, index, value)

    def slice(self, cube, index, value):
        """Filter cube1 using the index and the value. Return a new cube without the index1 dimension
            Ex.
                cp.slice(nodo_ejemplo,index_para_ejemplo,2)
        """
        return cpf.slice(cube, index, value)

    def shift(self, cube, axis, n=1, cval=0):
        """Returns a cube with the axis shifted.
            Ex.
                cp.shift(nodo_ejemplo,index_para_ejemplo,1)
        """
        return cpf.shift(cube, axis, n, cval)

    def subset(self, cube):
        """Returns a list of all the elements of the index for which cube is true. The function is used to create a new index that is a subset of an existing index.
            Ex. cp.subset(cantidades>0)
        """
        return cpf.subset(cube, self.currentNodeId)

    def aggregate(self, cube, mapCube, indexToRemove, targetIndex):
        """ Aggregates the values in Cube to generate the result indexed by  targetIndex.
            Map gives the value of targetIndex for each element of indexToRemove

            Example for aggregating time information into annual index the syntax is:
                cp.aggregate(cube, map, time, years )
        """
        return cpf.aggregate(cube, mapCube, indexToRemove, targetIndex)

    def cumulate(self, cube, index):
        """ TODO coment
        """
        return cpf.cumulate(cube, index)

    def cumProd(self, cube, index):
        """Return the cumulative product of elements along a given axis
            param cube: cube 
            param axis: axis name (str), index (int) or instance
            Ex:
                cp.cumProd(nodo,indice)
        """
        return cpf.cumProd(cube, index)

    def irr(self, flow, time_index):
        """Returns the Internal Rate of Return (IRR) of a series of periodic payments (negative values) and inflows (positive values). The IRR is the discount rate at which the Net Present Value (NPV) of the flows equals zero. 
            The variable flow must be indexed by time_index.

        If the cash flow never changes sign, cp.irr() has no solution and returns NAN (Not A Number).
        """

        return cpf.irr(flow, time_index)

    def npv(self, rate, flow, time_index, offset=1):
        """"Returns the Net Present Value (NPV) of a cash flow with equally spaced periods. The flow parameter must contain a series of periodic payments (negative values) and inflows (positive values), indexed by time_index.
            The optional offset parameter especifies the offset of the first value relative to the current time period. By default, offset is set to 1, indicating that the first value is discounted as if it is one step in the future
        """
        return cpf.npv(rate, flow, time_index, offset)

    # Esta es una nueva forma de hacer aggregate, pero falla en algunas ocasiones. ver con Lucas
    # def aggregate(self, cube, mapCube, indexToRemove, targetIndex,  ):

    #     _model = self.node.model
    #     _mapCube_list = []

    #     if type( mapCube ) is list:
    #         for _cube in mapCube:
    #             _mapCube_list.append( _cube )
    #     else:
    #         _mapCube_list = [ mapCube ]

    #     # Transforms set of cubes into a list.
    #     _indexToRemove_st = indexToRemove.name

    #     # Transforms set of indexes into a list.
    #     _targetIndex_st = []
    #     if type( targetIndex ) is list:
    #         for _ind in targetIndex:
    #             _targetIndex_st.append( _ind.name )
    #     else:
    #         _targetIndex_st = [ targetIndex.name ]

    #     # Creates pairs of ( mapCube, targetIndex ).
    #     _map_index_pairs = []
    #     for _pos in range( 0, len( _mapCube_list ) ):
    #         _pair = [ _mapCube_list[_pos], _targetIndex_st[_pos] ]
    #         _map_index_pairs.append( _pair )

    #     # Creates a dataframe with a indexToRemove-to-targetIndex allocation.
    #     _df_allocation = pd.DataFrame()
    #     for nn, pair in enumerate( _map_index_pairs ):
    #         #_allocation = self.pandasFromCube( _model.getNode(pair[0]).result , dataColumnName = pair[1], keepIndexOrder = False ).reset_index()
    #         _allocation = self.pandasFromCube( pair[0] , dataColumnName = pair[1], keepIndexOrder = False ).reset_index()

    #         if nn == 0:
    #             _df_allocation = _allocation
    #         else:
    #             _df_allocation = _df_allocation.merge( _allocation , on = _indexToRemove_st , how = "outer" )

    #     _df = self.pandasFromCube( cube , dataColumnName = 'value', keepIndexOrder = False ).reset_index()
    #     _df = _df[_df['value'] != 0]
    #     _df = _df.merge( _df_allocation , on = _indexToRemove_st , how = 'left')

    #     # Eliminates columns that will not be part of the cube's dimensions.
    #     _columns = list( _df.columns.values )
    #     _columns.remove( 'value' )
    #     _columns.remove( _indexToRemove_st )

    #     _df = _df.groupby( _columns ).agg({"value": sum})

    #     #remove duplicates
    #     _finalColumns = []
    #     for _tmpIndex  in _columns:
    #         if (_tmpIndex.endswith("_x") or _tmpIndex.endswith("_y")):
    #             _finalColumns.append(_tmpIndex[:-2])
    #         else:
    #             _finalColumns.append(_tmpIndex)
    #     _finalColumns = set(_finalColumns)
    #     _finalColumns = list(_finalColumns)

    #     _index = [ _model.getNode(idx).result for idx in _finalColumns]
    #     _cube = self.cubeFromPandas( _df, _index, "value" )

    #     return _cube

    def isNumber(self, value):
        """Return true if value is number
        """
        try:
            float(value)
            return True
        except ValueError:
            return False

    def splitText(self, text, separator=",", resultIndex=None):
        """Split text into a list of substrings by each occurrence of separator.
            text:  string or cp.index used for split
            separator: string for use as separator
            resultIndex: optional, for return cp.cube indexes by this index
            Ex:
                cp.splitText("Uno Dos Tres Cuatro Cinco Seis", separator=" ") 
                cp.splitText(indice_para_split, separator="-") 
                cp.splitText("Uno Dos Tres Cuatro Cinco Seis"," ",result_index)  
                cp.splitText(indice_para_split, "-", result_index)  

        """
        return cpf.splitText(text, separator, resultIndex, self.currentNodeId)

    def changeIndex(self, cube, oldIndex, newIndex, compareMode=1, default=None):
        """Returns a new Cube instance with the axes changed,looking newIndex on oldIndex by value o by position.
            param Comparemode: cp.byVal or cp.byPos
            Ex:
                cp.changeIndex(nodo_original,indice_original,indice_cambiado,cp.byVal)
                cp.changeIndex(nodo_original,indice_original,indice_cambiado,cp.byPos)
        """
        return cpf.changeIndex(cube, oldIndex, newIndex, compareMode, default)

    def copyIndex(self, cube):
        """Generate a cp.index with current unique values of the cube. 
        The cube must have only one dimension
        """
        return cpf.copyIndex(cube, self.currentNodeId)

    def cascadeVolume(self, demand, ranges, consumption_range_index=None):
        """TODO Comment
        Ex:
                cp.cascadeVolume(cantidades,limites_rango_consum)
                cp.cascadeVolume(cantidades,limites_rango_consum,"rangos_consumo")
                cp.cascadeVolume(cantidades,limites_rango_consum,rangos_consumo)
        """
        return cpf.cascadeVolume(demand, ranges, consumption_range_index)

    def bandAllocation(self, demand, ranges, consumption_range_index=None):
        """TODO Comment
            Ex:
                cp.bandAllocation(cantidades,limites_rango_consum)
                cp.bandAllocation(cantidades,limites_rango_consum,"rangos_consumo")
                cp.bandAllocation(cantidades,limites_rango_consum,rangos_consumo)
        """
        return cpf.bandAllocation(demand, ranges, consumption_range_index)

    def dispatch(self, contract_vol, contract_price, contract_index, demand):
        """TODO comment
            Ex:
                cp.dispatch(contract_volumes,prices,contracts,demand)
        """
        return cpf.dispatch(contract_vol, contract_price, contract_index, demand)

    def argsort(self, cube, axis):
        """Return new cube with the position of values sorted by axis
            ex.
                cp.argsort(nodo_1,index_a)
        """
        return cpf.argsort(cube, axis)

    def iif(self, condition, truePart, falsePart=None):
        """Inline if. Evaluate condition and return truePart or fasePart
            ex. 
                cp.iif( producto=="Producto A", cantidades*1000 , cantidades)
                cp.iif( cantidades > 10, cantidades , 0)
        """
        return cpf.iif(condition, truePart, falsePart)

    def mdtable(self, dataframe, cubeIndexes, valueColumns, indexColumnHeaders=None, replaceByIndex=None):
        """
        DEPRECATED: Use "cp.cubeFromPandas" instead
        """
        return self.cubeFromPandas(dataframe, cubeIndexes, valueColumns, indexColumnHeaders, replaceByIndex)

    def cubeFromPandas(self, dataframe, cubeIndexes, valueColumns, indexColumnHeaders=None, replaceByIndex=None):
        """Creat new cp.cube, converting pandas to multidimensional data, according to the parameters
            dataframe: pandas dataframe
            cubeIndexes: objects cp.index for perform change index
            valueColumns: string with column name of the dataframe where contain the values
                            cp.index with columns names for convert colums to index
            indexColumnHeaders: (optional) column names in pandas to parse with cubeIndexes. Used if header on dataframe is not equal to index identifiers.
            replaceByIndex: (optional) replace index used in valueColumns for this index. (using changeindex)
        """

        return cpf.cubeFromPandas(dataframe, cubeIndexes, valueColumns, indexColumnHeaders, replaceByIndex)

    def indexFromPandas(self, dataframe, columnName=None, removeEmpty=True):
        """ Return a cp.index from an columnf of a pandas dataframe.
        dataframe: pandas dataframe
        columnName: dataframe column name used for create cp.index. By default is created using the first column
        removeEmpty: True for remove empty rows
            Ex.
                cp.indexFromPandas(df)
                cp.indexFromPandas(df,"column10")
        """
        return cpf.indexFromPandas(dataframe, columnName, removeEmpty, self.currentNodeId)

    def pandasFromCube(self, cube, dataColumnName="value", keepIndexOrder=False):
        """
        Return indexed Dataframe created from cubePy Cube
        """
        return cpf.pandasFromCube(cube, dataColumnName, keepIndexOrder)

    def excel(self, filepath, useOpenpyxl=False, dataOnly=True, readOnly=True):
        """ Create excel object from filepath.
        filepath: absolute or relative path to excel file
        useOpenpyxl: True for use custom 
        dataOnly: True for view only the values, not formula
        readOnly: True for read only, False for write options
        Ex.
                cp.excel("\path\to\the\excelfile.xlsx")
        """
        fullFilename = filepath

        if not os.path.isfile(fullFilename):
            fullFilename = self.node.model.getNode(
                "current_path").result + filepath
        return cpf.excel(fullFilename, useOpenpyxl, dataOnly, readOnly)

    def pandasFromExcel(self, excel, sheetName=None, namedRange=None, cellRange=None, indexes=None, driver='Driver={Microsoft Excel Driver (*.xls, *.xlsx, *.xlsm, *.xlsb)};DBQ=%s;READONLY=TRUE'):
        """ return a pandas dataframe from excel.
        excel: path to excel file or cp.excel object
        sheetName: sheet name to be read
        namedRange: name of the range to be read
        cellRange: used with sheetname, for read from a simple range
        indexes: Listo of columns names for convert to index of dataframe
            Ex.
                cp.pandasFromExcel(excelNode,"Sheet 1")
                cp.pandasFromExcel(excelNode,namedRange="name_range")
                cp.pandasFromExcel(excelNode,"Sheet 1",cellRange="A1:H10")

        """
        if isinstance(excel, str):

            if not os.path.isfile(excel):
                excel = self.node.model.getNode("current_path").result + excel
        return cpf.pandasFromExcel(excel, sheetName, namedRange, cellRange, indexes, driver)

    def indexFromExcel(self, excel, sheetName=None, namedRange=None, cellRange=None, columnName=None, removeEmpty=True):
        """ Return a cp.index from an excel file.
        excel: cp.excel object
        sheetName: sheet name to be read
        namedRange: name of the range to be read
        cellRange: used with sheetname, for read from a simple range
        columnName: dataframe column name used for create cp.index. By default is created using the first column
        removeEmpty: True for remove empty rows
            Ex.
                cp.indexFromExcel(excelNode,"Sheet 1")
                cp.indexFromExcel(excelNode,namedRange="name_range")
                cp.indexFromExcel(excelNode,namedRange="name_range", columnName="indicadores")
        """
        return cpf.indexFromExcel(excel, sheetName, namedRange, cellRange, columnName, removeEmpty, self.currentNodeId)

    def cubeFromExcel(self, excel, sheetName=None, namedRange=None, cellRange=None, cubeIndexes=None, valueColumns=None, indexColumnHeaders=None, replaceByIndex=None):
        """ Return a cp.cube from excel file.
         excel: cp.excel object
        sheetName: sheet name to be read
        namedRange: name of the range to be read
        cellRange: used with sheetname, for read from a simple range
        cubeIndexes: objects cp.index for perform change index
        valueColumns: string with column name of the dataframe where contain the values
                        cp.index with columns names for convert colums to index
        indexColumnHeaders: (optional) column names in pandas to parse with cubeIndexes. Used if header on dataframe is not equal to index identifiers.
        replaceByIndex: (optional) replace index used in valueColumns for this index. (using changeindex)

            Ex.
                cp.cubeFromExcel(excelNode,"Sheet 1",cubeIndexes=[indicadores],valueColumns="descuentos")
                cp.cubeFromExcel(excelNode,namedRange="nombre_rango",cubeIndexes=[indicadores],valueColumns=time)
        """
        return cpf.cubeFromExcel(excel, sheetName, namedRange, cellRange, cubeIndexes, valueColumns, indexColumnHeaders, replaceByIndex)

    def sequence(self, initialNum, finalNum, stepSize=1, dtype=None):
        """
        Creates an index with a list of numbers increasing or decreasing from initial_num to final_num by increments (or decrements) of stepSize, which is optional and defaults to 1
        """
        return cpf.sequence(initialNum, finalNum, stepSize, dtype, self.currentNodeId)

    def lookup(self, cubeWithData, cubeWithMap, sharedIndex):
        """
        Returns the value of cubeWithData indexed by the index of cubeWithMap.
        cubeWithData must be indexed by sharedIndex and cubeWithData values must correspond to elements of sharedIndex.

        For example: Let's say you have a cube with an estimated inflation rate by Country ("inflation_rate" is the name of the cube; "country" is the name of the index) and you want to assign it to the corresponding Company depending on its location. On the other hand, there's a many-to-one map where each Company is allocated to a single Country ("country_to_company_allocation"). The sharedIndex, in this case, is Country ("country").
        As a result, 
            cp.lookup( inflation_rate , country_to_company_allocation , country )
        will return the estimated inflation rate by Company.
        """
        return cpf.lookup(cubeWithData, cubeWithMap, sharedIndex)

    def cubeFromNumpy(self, npArray):
        """ 
        Return a cube object from numpy Array. Generate temporal indexes
        """
        return cpf.cubeFromNumpy(npArray)

    def movingStats(self, cube, index, window=12, fn=np.mean):
        """
        Allows to calculate in a moving Window the selected statistics measure
        """
        return cpf.movingStats(cube, index, window, fn)

    # Cubepy Methods

    def plot(self, fig, **kwargs):
        """
        Generate HTML with plotly chart
        Params:
            fig: plotly fig
        """
        import plotly.io as pio
        return pio.to_html(fig, full_html=False, **kwargs)

    def concatIndex(self, *args):
        """
        Concatenates two or more indexes and/or atomic values into a single new index
        Return: new index
            Ex.
                cp.concatIndex(index1,index2,index3,value1,value2)
        """
        _list = []
        for arg in args:
            if isinstance(arg, cubepy.Index):
                values = (arg.values).tolist()
                _list.extend(values)
            else:
                _list.append(arg)

        seripandas = pd.Series(_list)
        return self.index(seripandas.unique())

    def yearsToTime(self, cube, yearsIndex, timeIndex, div=12):
        """ Convert cube indexed by anual index to a monthly index
        cube are the cp.cube with annual values to be converted
        yearIndex: is the year index of the original matrix
        timeIndex: is the monthly index of the result
        div: is an optional parameter used as divisor of the annual values (the tipical value is 12)
        """
        matrix = self.find(yearsIndex, timeIndex, compareType=4)
        final_cube = self.sum(cube * matrix, axis=[yearsIndex]) / div
        return final_cube

    def dynamic(self, cube, index, shift, initialValues=None):
        """
        Perform cyclic calculations betwwen nodes.
        cube: cp.cube to evaluate
        index: Index to shift 
        shift: amount of elemnts to shift. Can be positive or negative
        initialValues: (optional), initial values to apply to first "shift" elemnts
        """
        return self.shift(cube, index, shift, initialValues)

    def addPeriods(self, start, periods, freq='M', format='%Y.%m'):
        """Add periods to a date. Can set freq and output format 
            Ex.
                cp.addPeriods('2016.01',6)
                cp.apply( cp.addPeriods, inicio_de_proyectos , duracin_de_proyectos)
        """
        if "." in start:
            start = start.replace('.', '-')
        if periods < 0:
            return pd.period_range(end=start, periods=-periods+1, freq=freq).strftime(format)[0]
        else:
            return pd.period_range(start=start, periods=periods+1, freq=freq).strftime(format)[-1]

    def createTime(self, date_start, date_end, freq='M', format='%Y.%m'):
        """Create time index usign start and end dates and freq. The result is formated to format parameter
            Ex.
                cp.createTime('2016.01','2018.12')
                cp.createTime('2016.01','2016.12',freq='D',format='%d/%m/%Y')
        """
        if "." in date_start:
            date_start = date_start.replace('.', '-')
        if "." in date_end:
            date_end = date_end.replace('.', '-')
        return self.index(pd.period_range(start=date_start, end=date_end, freq=freq).strftime(format))

    def choice(self, index, selection, includeAll=False):
        """Return the element in the "selection" position of the index. 
        """
        if selection == 0 and includeAll == 1:
            return "All"
        else:
            values = None
            if isinstance(index, cubepy.Index):
                values = (index.values[:1000]).tolist()
            elif isinstance(index, np.ndarray):
                values = (index[:1000]).tolist()
            else:
                values = list(index)[:1000]
            if not values is None and len(values) >= selection:
                return values[selection-1]
        return ""

    def copyAsValues(self, source, targetId):
        """Copy values of cube "source" into cube with id 'targetId'. This function alter the thefinition of cube with 'targetId' identifier.
            source: cube/index from copy values
            targetId: identifier (string) of the target node 
        """

        if isinstance(source, str):
            if self.node.model.existNode(source):
                source = self.node.model.getNode(source)
            else:
                raise ValueError("Node '" + source + "' not found")

        if not isinstance(source, cubepy.Cube) and not isinstance(source, cubepy.Index):
            raise ValueError(
                "The 'source' parameter must be a cp.cube or cp.index object")

        if not isinstance(targetId, str):
            raise ValueError(
                "The 'targetId' parameter must be a string (identifier of node)")

        if not self.node.model.existNode(targetId):
            raise ValueError("Node '" + targetId + "' not found")

        self.node.model.getNode(
            targetId).definition = source.generateDefinition()
        return True

    def goalSeek(self, nodeIdX, nodeIdObjective, goal=0, startValue=1):
        """ Finds the value of nodeIdX that makes nodeIdObjective equal to goal.
        nodeIdX: String with id of node X
        nodeIdObjective: String with id of node X
        """
        from scipy.optimize import newton

        def _f(x):
            self.node.model.getNode(nodeIdX).definition = "result = " + str(x)
            value = self.node.model.getNode(nodeIdObjective).result
            return value - goal

        _res = newton(_f, x0=startValue)
        return _res

    def from_xindex(self, xindex):
        """Create a cubepy index from xarray index 
        """
        return cpf.index(self.node.identifier, xindex.values)

    def from_dataArray(self, axes, dataArray):
        """Create a cubepy cube from dataarray 
        """
        return self.cube(axes, values=dataArray.values)

    @staticmethod
    def getResultSize(result):
        res = getsizeof(0)
        res += getsizeof(result)
        return res

    @staticmethod
    def kindToString(kind):
        return cubepy.cube.kindToString(kind)
        """
        if kind in {'U', 'S'}:
            return "string"
        elif kind in {'b'}:
            return "boolean"
        elif kind in {'i','u','f','c'}:
            return "numeric"
        elif kind in {'m','M'}:
            return "date"
        elif kind in {'O'}:
            return "object"
        elif kind in {'V'}:
            return "void"
        """

    @staticmethod
    def describe(text, prefix, objectType=None):
        res = []

        _prefix = prefix + "."
        if text == _prefix:
            text = ""
            _prefix = ""

        _members = inspect.getmembers(objectType)
        for _member in _members:
            if not("__" in str(_member[0])) and (text is None or text in str(_member[0]).lower()):
                if inspect.isfunction(_member[1]):
                    _doc = inspect.getdoc(_member[1])
                    if not _doc is None:
                        _params = str(inspect.signature(_member[1]))
                        _params = _params.replace("self,", "")
                        res.append({
                            "identifier": _prefix + _member[0],
                            "nodeClass": "helper" if prefix == "cp" else "function",
                            "moduleId": "",
                            "title": _prefix + _member[0],
                            "description": _doc,
                            "params": _params
                        })
                elif inspect.isroutine(_member[1]):
                    _doc = inspect.getdoc(_member[1])
                    try:
                        _params = str(inspect.signature(_member[1]))
                        _params = _params.replace("self,", "")
                        res.append({
                            "identifier": _prefix + _member[0],
                            "nodeClass": "method",
                            "moduleId": "",
                            "title": _prefix + _member[0],
                            "description": _doc,
                            "params": _params
                        })
                    except:
                        # check if object is form numpy class
                        _dot = str(objectType).find('.')
                        if _dot != -1 and str(objectType)[_dot-5:_dot] == 'numpy':
                            info = numpydoc.docscrape.FunctionDoc(_member[1])
                            info["Signature"] = info["Signature"][info["Signature"].find(
                                "("):]
                            res.append({
                                "identifier": _prefix + _member[0],
                                "nodeClass": "method",
                                "moduleId": "",
                                "title": _prefix + _member[0],
                                "description": _doc,
                                "params":  info["Signature"]
                            })
                        else:
                            print(
                                "Error al intentar obtener la signature del tipo de dato")
                            e = exc_info()[0]
                            print("<p>Error: %s</p>" % e)
        return res

    @staticmethod
    def dfs_topsort(graph):
        """
        DFS algorithm for sort nodes
        """
        L = []
        color = {u: "white" for u in graph}
        found_cycle = [False]
        for u in graph:
            if color[u] == "white":
                Helpers.dfs_visit(graph, u, color, L, found_cycle)
            if found_cycle[0]:
                break

        if found_cycle[0]:           # if there is a cycle,
            L = []                   # then return an empty list

        L.reverse()                  # reverse the list
        return L                     # L contains the topological sort

    @staticmethod
    def dfs_visit(graph, u, color, L, found_cycle):
        """
        DFS algorithm for sort nodes
        """
        if found_cycle[0]:
            return
        color[u] = "gray"
        for v in graph[u]:
            if color[v] == "gray":
                found_cycle[0] = True
                return
            if color[v] == "white":
                Helpers.dfs_visit(graph, v, color, L, found_cycle)
        color[u] = "black"      # when we're done with u,
        L.append(u)             # add u to list (reverse it later!)
