from pyplan_engine.classes.wizards.BaseWizard import BaseWizard
import pandas as pd
import jsonpickle


class Wizard(BaseWizard):

    def __init__(self):
        self.code = "SelectColumns"

    def generateDefinition(self, model, params):
        nodeId = params["nodeId"]
        if model.existNode(nodeId):
            currentDef = model.getNode(nodeId).definition
            newDef = self.getLastDefinition(currentDef)
            newDef = newDef + "\n# Selected columns"
            newDef = newDef + "\nresult = _df[" + str(params["columns"]) + "]"
            model.getNode(nodeId).definition = self.formatDefinition(newDef)
            return "ok"
        return ""
