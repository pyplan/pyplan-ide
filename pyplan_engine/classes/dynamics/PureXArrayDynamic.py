from pyplan_engine.classes.dynamics.BaseDynamic import BaseDynamic
from pyplan_engine.classes.Helpers import Helpers
import numpy as np
import datetime as dt
import re
import xarray as xr


class PureXArrayDynamic(BaseDynamic):

    def circularEval(self, node, params):
        """
        Used for execute nodes with circular reference (pp.dynamic)
        """

        dynamicVars = params["dynamicVars"]
        dynamicIndex = params["dynamicIndex"]
        nodesInCyclic = params["nodesInCyclic"]
        initialValues = params["initialValues"]
        shift = params["shift"]

        evaluate = node.model.evaluate

        # create nodes array
        cyclicNodes = []

        try:
            node.model.inCyclicEvaluate = True
            for nodeId in nodesInCyclic:
                _nodeObj = node.model.getNode(nodeId)
                cyclicNodes.append({
                    "node": _nodeObj,
                    "initialize": self.generateInitDef(node, _nodeObj.bypassCircularEvaluator().result, dynamicIndex),
                    "loopDefinition": self.generateLoopDef(node, _nodeObj.definition, nodesInCyclic),
                    "calcTime": 0.
                })
        except Exception as e:
            raise e
        finally:
            node.model.inCyclicEvaluate = False

        cyclicDic = {}

        # initialice var dictionary
        for _node in cyclicNodes:
            _id = _node["node"].identifier
            cyclicDic[_id] = evaluate(_node["initialize"])
            if not initialValues is None and _id in initialValues:
                cyclicDic[_id] = cyclicDic[_id] + evaluate(initialValues[_id])

        # initialice vars in t-1
        for _var in dynamicVars:
            _key = "__" + _var + "_t"
            cyclicDic[_key] = cyclicDic[_var].sum(dynamicIndex.name) * 0

        # loop over index
        cyclicParams = None
        # for item in dynamicIndex:

        theRange = range(0, len(dynamicIndex.values))
        initialCount = shift*-1
        reverseMode = False
        if shift > 0:
            theRange = range(len(dynamicIndex.values)-1, -1, -1)
            initialCount = len(dynamicIndex.values)-1-shift
            reverseMode = True

        for nn in theRange:
            item = dynamicIndex.values[nn]

            # load params
            cyclicParams = {
                "item": item,
                "cyclicDic": cyclicDic,
                "dynamicIndex": dynamicIndex,
                "self": self
            }

            __initialValues = None
            # loop over variables
            for _node in cyclicNodes:

                startTime = dt.datetime.now()

                _id = _node["node"].identifier
                node.model.currentProcessingNode(_id)
                cyclicParams["cyclicDic"] = cyclicDic

                # execute vars
                if (_id in initialValues) and ((nn < initialCount and (not reverseMode)) or (nn > initialCount and reverseMode)):
                    # use initial values
                    __resultNode = evaluate(
                        _node["loopDefinition"], cyclicParams)
                    __initialValues = evaluate(initialValues[_id])

                    if isinstance(__initialValues, xr.DataArray):
                        __finalNode = self._tryFilter(
                            __initialValues, dynamicIndex, item) + self._tryFilter(__resultNode, dynamicIndex, item)
                    else:
                        __finalNode = self._tryFilter(
                            __resultNode, dynamicIndex, item) + __initialValues

                    try:
                        cyclicDic[_id].loc[{dynamicIndex.name: slice(
                            item, item)}] = __finalNode.values
                    except Exception as ex:
                        _cubeShape = cyclicDic[_id].loc[{
                            dynamicIndex.name: slice(item, item)}].shape
                        cyclicDic[_id].loc[{dynamicIndex.name: slice(
                            item, item)}] = __finalNode.values.reshape(_cubeShape)

                else:
                    # dont use use initial values
                    __resultNode = evaluate(
                        _node["loopDefinition"], cyclicParams)
                    _values = self._tryFilter(
                        __resultNode, dynamicIndex, item).values
                    try:
                        cyclicDic[_id].loc[{
                            dynamicIndex.name: slice(item, item)}] = _values
                    except Exception as ex:
                        _cubeShape = cyclicDic[_id].loc[{
                            dynamicIndex.name: slice(item, item)}].shape
                        cyclicDic[_id].loc[{dynamicIndex.name: slice(
                            item, item)}] = _values.reshape(_cubeShape)

                endTime = dt.datetime.now()
                _node["calcTime"] = _node["calcTime"] + \
                    (endTime - startTime).total_seconds()

            # set dynamicVar
            if (not reverseMode and (nn+1) < initialCount) or (reverseMode and (nn-1) > initialCount):
                # do not update t- vars
                pass
            else:
                for _var in dynamicVars:
                    _key = "__" + _var + "_t"
                    if reverseMode:
                        cyclicDic[_key] = self._tryFilter(
                            cyclicDic[_var], dynamicIndex, dynamicIndex.values[nn+shift-1])
                    else:
                        cyclicDic[_key] = self._tryFilter(
                            cyclicDic[_var], dynamicIndex, dynamicIndex.values[nn-initialCount+1])

        # set result
        for _node in cyclicNodes:
            _id = _node["node"].identifier
            _node["node"]._result = cyclicDic[_id]
            _node["node"].__resultMemory = Helpers.getResultSize(
                _node["node"]._result)
            _node["node"]._isCalc = True
            _node["node"].lastEvaluationTime = _node["calcTime"]
            _node["node"].evaluationVersion = node.model.evaluationVersion

        evaluate = None
        model = None
        cyclicDic = None
        cyclicParams = None

        return "ok"

    def generateLoopDef(self, node, nodeDefinition, cyclicVariables):
        """
        Return definition used for circular evaluator
        """
        _def = self.clearCircularDependency(
            nodeDefinition, "cyclicDic['__##node##_t']")
        finalDef = _def
        tmpCode = compile(_def, '<string>', 'exec')
        names = node.parseNames(tmpCode)
        rx = r"('[^'\\]*(?:\\.[^'\\]*)*'|\"[^\"\\]*(?:\\.[^\"\\]*)*\")|\b{0}\b"
        for nodeId in names:
            if node._model.existNode(node._model.clearId(nodeId)):
                if nodeId in cyclicVariables:
                    finalDef = re.sub(rx.format(nodeId), lambda m:
                                      (
                        m.group(1)
                        if m.group(1)
                        else
                        (
                            "cyclicDic['"+nodeId+"']"
                            if (m.endpos > m.regs[0][1]+5) and ((m.string[m.regs[0][1]:m.regs[0][1]+5] == '.node') or (m.string[m.regs[0][1]:m.regs[0][1]+8] == '.timeit('))
                            else
                            (nodeId
                             if (m.string[m.regs[0][0]-1:m.regs[0][0]+len(nodeId)] == ('.'+nodeId))
                             else "self._tryFilter( cyclicDic['"+nodeId+"'],dynamicIndex,item) "
                             )
                        )
                    ), finalDef, 0, re.IGNORECASE)

        return finalDef

    def generateInitDef(self, node, nodeCube, dynamicIndex):
        """
        Return definition used for initialice vars in circular evaluator
        """
        if isinstance(nodeCube, xr.DataArray):
            _list = list(nodeCube.dims[:])
            if not dynamicIndex.name in _list:
                _list.append(dynamicIndex.name)
            _dims = ','.join(_list)
            _def = f"result = create_dataarray(0.,[{_dims}])"

            """
            _data = np.full(nodeCube.shape, 0. )
            np.set_printoptions(threshold = np.prod(_data.shape))
            _data = np.array2string(_data, separator=",", precision=20 , formatter={'float_kind':lambda x: repr(x)}).replace('\n','')

            _def = f"result = xr.DataArray({_data},{_dims})"
            """
            return _def
        else:
            return f"result = create_dataarray(0.,[{dynamicIndex.name}])"
            """
            _data = np.full(dynamicIndex.shape, 0. )
            np.set_printoptions(threshold = np.prod(_data.shape))
            _data = np.array2string(_data, separator=",", precision=20 , formatter={'float_kind':lambda x: repr(x)}).replace('\n','')
            return f"result = xr.DataArray({_data}, [{dynamicIndex.name}])"
            """

    def generateCircularParameters(self, node, nodeList):
        """
        Generate paremters for call to circularEval
        """
        dynamicVars = []
        dynamicIndex = None
        nodesInCyclic = []  # nodeList TODO: Determinar orden de nodos
        initialValues = {}
        shift = -1

        for _nodeId in nodeList:
            if node.model.existNode(_nodeId):
                _def = node.model.getNode(_nodeId).definition
                if "dynamic(" in _def:
                    _startPos = _def.find("dynamic(") + 8
                    _endPos = _def.find(")", _startPos)

                    # dynamicVars = _def[_startPos:_endPos] # cc,time,-1
                    _arr = str(_def[_startPos:_endPos]).split(",")
                    _vart_1 = _arr[0].strip()
                    if not _vart_1 in dynamicVars:
                        dynamicVars.append(_vart_1)
                    dynamicIndex = node.model.getNode(_arr[1].strip()).result
                    shift = int(_arr[2])
                    if len(_arr) > 3:
                        initialValues[_nodeId] = "result = " + _arr[3].strip()

        #nodesInCyclic =  sort

        _graph = {}

        for _nodeId in nodeList:
            if node.model.existNode(_nodeId):
                _graph[_nodeId] = []
                for _outputId in node.model.getNode(_nodeId).ioEngine.outputs:
                    if _outputId in nodeList:
                        if 'dynamic('+_nodeId+',' not in str(node.model.getNode(_outputId).definition).replace(" ", ""):
                            _graph[_nodeId].append(_outputId)

        nodesInCyclic = Helpers.dfs_topsort(_graph)

        return {
            "dynamicVars": dynamicVars,
            "dynamicIndex": dynamicIndex,
            "nodesInCyclic": nodesInCyclic,
            "initialValues": initialValues,
            "shift": shift
        }

    def clearCircularDependency(self, stringDef, replaceWith="0"):
        """ Replaces pp.dynamic(x,y,z) for the desired replaceWith param
        """
        response = stringDef
        initialIndex = -1
        startIndex = -1
        finalIndex = -1
        toReplace = ''
        initialIndex = stringDef.find('dynamic(')
        if initialIndex != -1:
            startIndex = initialIndex
            initialIndex = initialIndex + len('dynamic(')
            if len(stringDef) > initialIndex:
                finalIndex = stringDef[initialIndex+1:].find(')')

        if initialIndex != -1 and finalIndex != -1:
            toReplace = stringDef[startIndex:initialIndex + finalIndex + 2]
            if "cyclicDic" in replaceWith:
                nodeInT1 = toReplace.split(",")[0]
                nodeInT1 = nodeInT1[(nodeInT1.find("(")+1):]
                replaceWith = replaceWith.replace("##node##", nodeInT1.strip())
            response = stringDef.replace(toReplace, replaceWith)

        return response

    def _tryFilter(self, array, dim, value):
        try:
            _dic = {
                dim.name: value
            }
            return array.sel(_dic, drop=True)
        except Exception as ex:
            return array
