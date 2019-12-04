import json
import autopep8


class BaseWizard(object):

    def getLastDefinition(self, definition):
        newDef = definition.replace(
            "result=", "_df =").replace("result =", "_df =")
        return newDef

    def getColumnList(self, model, params):
        res = []
        nodeId = params["nodeId"]
        if model.existNode(nodeId):
            nodeResult = model.getNode(nodeId).result

            # append indexes
            for nn, idx in enumerate(nodeResult.index.names):
                if not idx is None:
                    res.append(dict(field=idx, type="index", dtype=self.kindToString(
                        nodeResult.index.levels[nn].values.dtype.kind)))

            # append columns
            for nn, cols in enumerate(list(nodeResult.columns)):
                if not cols is None:
                    res.append(dict(field=cols, type="column",  dtype=self.kindToString(
                        nodeResult.dtypes[nn].kind)))

        return res

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

    def formatDefinition(self, definition):
        return autopep8.fix_code(definition)
