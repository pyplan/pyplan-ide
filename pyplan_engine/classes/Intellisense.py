import inspect
import os
from sys import exc_info

import numpy as np
import numpydoc
import pandas as pd

import cubepy
from pyplan_engine.classes.BaseNode import BaseNode
from pyplan_engine.classes.Evaluator import Evaluator
from pyplan_engine.classes.XHelpers import XHelpers
from pyplan_engine.common.classes.indexValuesReq import IndexValuesReq


class Intellisense(object):
    """
    Class to manage intellisense on node definition. Also used for search node in entire model
    """

    def __init__(self):
        self._operatorsDic = {
            '.': self.searchDot,
            '[': self.searchBrackeys,
            '==': self.searchOperators,
            '>=': self.searchOperators,
            '<=': self.searchOperators,
            '!=': self.searchOperators,
            '>': self.searchOperators,
            '<': self.searchOperators
        }
        self._finalIndex = -1
        self._preIndex = -1
        self._operator = None
        self._prefix = None
        self._searchText = ""
        self._extraText = ""

    # Props
    @property
    def operatorsDic(self):
        return self._operatorsDic

    # Methods
    def clearValues(self):
        self._finalIndex = -1
        self._preIndex = -1
        self._operator = None
        self._prefix = None
        self._searchText = ""
        self._extraText = ""

    def search(self, model, filterOptions):
        res = []
        self.clearValues()
        if not filterOptions is None:
            onlyClass = None
            if not filterOptions["nodeClass"] is None and str(filterOptions["nodeClass"]).lower() != "all":
                onlyClass = []
                onlyClass.append(str(filterOptions["nodeClass"]).lower())
            if "extraClasses" in filterOptions and isinstance(filterOptions["extraClasses"], list) and len(filterOptions["extraClasses"]) > 0:
                if onlyClass is None:
                    onlyClass = []
                onlyClass.extend(str(extraClass).lower()
                                 for extraClass in filterOptions["extraClasses"])

            moduleId = None
            if not filterOptions["moduleId"] is None:
                moduleId = str(filterOptions["moduleId"]).lower()

            searchText = None
            index = None
            if not filterOptions["text"] is None and filterOptions["text"] != "":
                searchText = str(filterOptions["text"]).lower()

                for operator in self._operatorsDic:
                    index = searchText.rfind(operator)
                    if (index > self._finalIndex):
                        self._operator = operator
                        self._finalIndex = index

                if (self._finalIndex != -1):
                    self._prefix = searchText[:self._finalIndex]
                    index = -1
                    for operator in self._operatorsDic:
                        index = searchText[:self._finalIndex].rfind(operator)
                        if index > self._preIndex:
                            self._preIndex = index
                            if self._preIndex != -1:
                                if len(operator) == 1:
                                    self._prefix = searchText[self._preIndex +
                                                              1:self._finalIndex]
                                    self._extraText = searchText[:self._preIndex+1]
                                else:
                                    self._prefix = searchText[self._preIndex +
                                                              2:self._finalIndex]
                                    self._extraText = searchText[:self._preIndex+2]

                        if (len(filterOptions["text"]) > self._finalIndex+1 and len(self._operator) == 1):
                            self._searchText = str(
                                filterOptions["text"][self._finalIndex+1:]).lower()
                        elif (len(filterOptions["text"]) > self._finalIndex+2 and len(self._operator) == 2):
                            self._searchText = str(
                                filterOptions["text"][self._finalIndex+2:]).lower()

                    res = self._operatorsDic[self._operator](
                        model, filterOptions, onlyClass, moduleId, self._searchText, self._prefix, self._extraText, self._operator)

                else:
                    self._searchText = str(filterOptions["text"]).lower()
                    res = self.searchDefault(
                        model, filterOptions, onlyClass, moduleId, self._searchText, self._prefix, self._extraText)

        return res

    # search if no operator was found
    def searchDefault(self, model, filterOptions, onlyClass, moduleId, searchText, prefix, extraText):
        res = []
        for k, node in model.nodeDic.items():
            if not searchText is None and not node is None:
                if (
                    node.identifier.lower().find(searchText) >= 0 or
                    ((not node.title is None)
                     and node.title.lower().find(searchText) >= 0)
                ):

                    if onlyClass is None or node.nodeClass in onlyClass:
                        if moduleId is None or node.moduleId == moduleId:
                            if not node.system:
                                toAppend = node.toObj(
                                    properties=["identifier", "nodeClass", "moduleId", "title", "description"])
                                toAppend["completeText"] = extraText + \
                                    node.identifier
                                if filterOptions["fillDetail"] and node.nodeClass == "function":
                                    try:
                                        _fn = node.result
                                        toAppend["params"] = str(
                                            inspect.signature(_fn))
                                        toAppend["description"] = str(
                                            inspect.getdoc(_fn))
                                    except Exception as ex:
                                        params = node.definition[node.definition.find(
                                            "(")+1:node.definition.find(")")]
                                        toAppend["params"] = params

                                res.append(toAppend)

        return res

    # search if operator is .
    def searchDot(self, model, filterOptions, onlyClass, moduleId, searchText, prefix, extraText, operator):
        res = []
        node = None
        if model.existNode(prefix):
            node = model.getNode(prefix)
            if node.isCalc:
                if filterOptions["fillDetail"]:
                    res = self.describe(searchText, prefix,
                                        extraText, operator, type(node.result))
        else:
            localRes = localRes = {
                "pp": XHelpers,
            }
            customImports = model.getCustomImports()
            if customImports:
                for keyParam in customImports:
                    localRes[keyParam] = customImports[keyParam]

            toExec = "result =" + prefix
            try:
                exec(compile(toExec, '<string>', 'exec'), globals(), localRes)
                if filterOptions["fillDetail"]:
                    res = self.describe(
                        searchText, prefix, extraText, operator, localRes["result"])
            except:
                print("Error al intentar compilar el prefijo " +
                      prefix + " antes del .")
                e = exc_info()[0]
                print("<p>Error: %s</p>" % e)

        return res

    # search if operator is [
    def searchBrackeys(self, model, filterOptions, onlyClass, moduleId, searchText, prefix, extraText, operator):
        res = []
        if (prefix is not None and prefix != ""):
            # check if node
            node = None
            indexes = None
            if model.existNode(prefix):
                node = model.getNode(prefix)
                if node.isCalc:
                    # check if cube
                    if isinstance(node.result, cubepy.Cube):
                        if filterOptions["fillDetail"]:
                            indexes = model.getIndexes(node.identifier)
                            if indexes:
                                for index in indexes:
                                    res.append({
                                        "identifier": index,
                                        "nodeClass": "cube axis",
                                        "moduleId": "",
                                        "title": index,
                                        "description": "se ha buscado un cubo",
                                        "params": index,
                                        "completeText": extraText + prefix + operator
                                    })
                    elif isinstance(node.result, pd.DataFrame):
                        if filterOptions["fillDetail"]:
                            for column in list(node.result.columns):
                                res.append({
                                    "identifier": column,
                                    "nodeClass": "dataframe column",
                                    "moduleId": "",
                                    "title": column,
                                    "description": "dataframe column",
                                    "params": "\""+column+"\"",
                                    "completeText": extraText + prefix + operator
                                })

        return res

     # search if operator is == or >= or <= or != or > or <
    def searchOperators(self, model, filterOptions, onlyClass, moduleId, searchText, prefix, extraText, operator):
        res = []
        if (prefix is not None and prefix != ""):
            # check if node
            node = None
            indexValues = None
            if model.existNode(prefix):
                node = model.getNode(prefix)
                if node.isCalc:
                    # check if index
                    if node.nodeClass == "index":
                        if filterOptions["fillDetail"]:
                            indexValues = model.getIndexValues(
                                None, IndexValuesReq({'node_id': node.identifier}))
                            if indexValues:
                                for value in indexValues:
                                    finalValue = str(value)
                                    finalParam = value
                                    if isinstance(value, str):
                                        finalValue = "'" + value + "'"
                                        finalParam = finalValue
                                    res.append({
                                        "identifier": finalValue,
                                        "nodeClass": "index value",
                                        "moduleId": "",
                                        "title": finalValue,
                                        "description": "se ha buscado un indice",
                                        "params": finalParam,
                                        "completeText": extraText + prefix + operator
                                    })

        return res

    # describes a class or object by type
    @staticmethod
    def describe(text, prefix, extraText, operator, objectType=None):
        res = []

        _prefix = prefix + operator
        if text == _prefix:
            text = ""
            _prefix = ""

        _members = inspect.getmembers(objectType)
        for _member in _members:
            if not("__" in str(_member[0])) and (text is None or text in str(_member[0]).lower()):
                if inspect.isfunction(_member[1]) or inspect.isclass(_member[1]):
                    _doc = inspect.getdoc(_member[1])
                    if not _doc is None:
                        _params = ""
                        try:
                            _params = str(inspect.signature(_member[1]))
                            _params = _params.replace("self,", "")
                        except:
                            _params = ""
                        res.append({
                            "identifier": _prefix + _member[0],
                            "nodeClass": "helper" if prefix == "cp" else "function" if inspect.isfunction(_member[1]) else "class",
                            "moduleId": "",
                            "title": _prefix + _member[0],
                            "description": _doc,
                            "params": _params,
                            "completeText": extraText + _prefix + _member[0]
                        })
                elif inspect.isroutine(_member[1]):
                    _doc = inspect.getdoc(_member[1])
                    try:
                        _params = ""
                        try:
                            _params = str(inspect.signature(_member[1]))
                            _params = _params.replace("self,", "")
                        except:
                            _params = ""
                        res.append({
                            "identifier": _prefix + _member[0],
                            "nodeClass": "method",
                            "moduleId": "",
                            "title": _prefix + _member[0],
                            "description": _doc,
                            "params": _params,
                            "completeText": extraText + _prefix + _member[0]
                        })
                    except:
                        # check if object is from numpy class
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
                                "params":  info["Signature"],
                                "completeText": extraText + _prefix + _member[0]
                            })
                        else:
                            print(
                                "Error al intentar obtener la signature del tipo de dato")
                            e = exc_info()[0]
                            print("<p>Error: %s</p>" % e)
                else:
                    _doc = inspect.getdoc(_member[1])
                    try:
                        res.append({
                            "identifier": _prefix + _member[0],
                            "nodeClass": "other",
                            "moduleId": "",
                            "title": _prefix + _member[0],
                            "description": _doc,
                            "params": "",
                            "completeText": extraText + _prefix + _member[0]
                        })
                    except:
                        pass

        return res
