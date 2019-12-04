from pyplan_engine.classes.wizards.BaseWizard import BaseWizard
import pandas as pd
import jsonpickle


class Wizard(BaseWizard):

    def __init__(self):
        self.code = "DataframeGroupby"

    def generateDefinition(self, model, params):
        nodeId = params["nodeId"]
        if model.existNode(nodeId):

            currentDef = model.getNode(nodeId).definition
            newDef = self.getLastDefinition(currentDef)
            newDef = newDef + "\n# Groupby"
            agg = params['agg']
            need_join = False

            group_by = ""
            if 'columns' in params and len(params['columns']) > 0:
                group_by = f".groupby({params['columns']})"
                # format aggregator
                for key in agg:
                    if len(agg[key]) == 1:
                        agg[key] = str(agg[key][0])
                    else:
                        need_join = True

            newDef = newDef + \
                f"\n_df = _df{group_by}.agg({jsonpickle.dumps(agg)})"
            if need_join:
                newDef = newDef + "\n# Format columns name"
                newDef = newDef + \
                    f"\n_df.columns = _df.columns.map('_'.join)"

            newDef = newDef + \
                f"\nresult = _df"

            model.getNode(nodeId).definition = self.formatDefinition(newDef)

            return "ok"

        return ""
