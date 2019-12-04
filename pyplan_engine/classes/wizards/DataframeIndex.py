from pyplan_engine.classes.wizards.BaseWizard import BaseWizard
import pandas as pd
import jsonpickle


class Wizard(BaseWizard):

    def __init__(self):
        self.code = "DataframeIndex"

    def generateDefinition(self, model, params):
        nodeId = params["nodeId"]
        if model.existNode(nodeId):
            currentDef = model.getNode(nodeId).definition
            newDef = self.getLastDefinition(currentDef)
            newDef = newDef + "\n# Set index"
            reset_index = ""
            if not isinstance(model.getNode(nodeId).result.index, pd.RangeIndex):
                reset_index = ".reset_index()"

            if not params is None and "columns" in params and len(params["columns"]) > 0:
                newDef = newDef + \
                    f"\nresult = _df{reset_index}.set_index({params['columns']})"
            else:
                newDef = newDef + f"\nresult = _df{reset_index}"

            model.getNode(nodeId).definition = self.formatDefinition(newDef)
            return "ok"
        return ""
