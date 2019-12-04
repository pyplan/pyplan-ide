from pyplan_engine.classes.wizards.BaseWizard import BaseWizard
import pandas as pd
import jsonpickle


class Wizard(BaseWizard):

    def __init__(self):
        self.code = "SelectRows"

    def getValues(self, model, params):
        field = params["field"]
        nodeId = params["nodeId"]
        if model.existNode(nodeId):
            nodeResult = model.getNode(nodeId).result
            if field["type"] == "index":
                pos = nodeResult.index.names.index(field["field"])
                return list(nodeResult.index.levels[pos].values)[:500]
            else:
                return list(nodeResult[field["field"]].unique())[:500]

    def generateDefinition(self, model, params):
        nodeId = params["nodeId"]
        if model.existNode(nodeId):
            nodeResult = model.getNode(nodeId).result
            currentDef = model.getNode(nodeId).definition
            newDef = currentDef
            conditions = ""
            for filterItem in params["filters"]:
                conditions = conditions + \
                    self.generateFilter(nodeResult, filterItem) + " & "
            if conditions != "":
                conditions = conditions[:-3]

            if conditions != "":
                newDef = self.getLastDefinition(currentDef)
                newDef = newDef + "\n" + "# applied filters"
                newDef = newDef + "\n" + "_conditions = " + conditions
                newDef = newDef + "\n" + "result = _df[_conditions]"

            model.getNode(nodeId).definition = self.formatDefinition(newDef)
            return "ok"
        return ""

    def generateFilter(self, nodeResult, filterItem):

        res = ""
        field = filterItem["field"]
        values = filterItem["values"]
        operator = filterItem["operator"]

        selector = ""
        if filterItem["type"] == "column":
            selector = "_df['" + field.replace("'", "\\'") + "']"
        else:
            selector = "_df.index.get_level_values('" + \
                field.replace("'", "\\'") + "')"

        if filterItem["dtype"] == "numeric":
            if operator == "between":
                res = "(" + selector + " > " + str(values[0]) + ")"
                res = res + " & (" + selector + " < " + str(values[1]) + ")"
            elif operator == "outside":
                res = "(" + selector + " < " + str(values[0]) + ")"
                res = res + " & (" + selector + " > " + str(values[1]) + ")"
            elif operator == "defined":
                res = "(~" + selector + ".isnull())"
            elif operator == "undefined":
                res = "(" + selector + ".isnull())"
            else:
                res = "(" + selector + " " + operator + \
                    " " + str(values[0]) + ")"
        else:
            if operator == "contains":
                res = "(" + selector + ".str.contains('" + \
                    str(values[0]).replace("'", "\\'") + "'))"
            elif operator == "notcontains":
                res = "(~" + selector + ".str.contains('" + \
                    str(values[0]).replace("'", "\\'") + "'))"
            else:
                res = "(" + selector + " " + operator + " '" + \
                    str(values[0]).replace("'", "\\'") + "')"
            pass

        return res
