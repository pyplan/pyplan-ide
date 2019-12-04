from pyplan_engine.classes.wizards.BaseWizard import BaseWizard
import pandas as pd
import jsonpickle
import re


class Wizard(BaseWizard):

    def __init__(self):
        self.code = "CalculatedField"

    def generateDefinition(self, model, params):
        nodeId = params["nodeId"]
        formula = params["formula"]
        name = params["name"]
        if model.existNode(nodeId):
            currentDef = model.getNode(nodeId).definition
            newDef = self.getLastDefinition(currentDef)
            newDef = newDef + "\n# Generated new column"

            # find fields on formula
            regex = r"#(.+?)#"
            matches = re.finditer(regex, formula)
            formulaFields = []
            for matchNum, match in enumerate(matches):
                formulaFields.append(str(match.group(1)))

            # find df fields
            dfFields = self.getColumnList(model, params)

            # replace def
            for field in formulaFields:
                dfField = [f for f in dfFields if f["field"] == field]
                if not dfField is None and len(dfField) == 1:
                    fieldDef = ""
                    if dfField[0]["type"] == "column":
                        fieldDef = "_df['" + field.replace("'", "\\'") + "']"
                    else:
                        fieldDef = "_df.index.get_level_values('" + field.replace(
                            "'", "\\'") + "')"

                    key = "#"+field+"#"
                    formula = formula.replace(key, fieldDef)

            newDef = newDef + "\n_df['" + \
                name.replace("'", "") + "'] = " + formula
            newDef = newDef + "\nresult = _df"

            model.getNode(nodeId).definition = self.formatDefinition(newDef)
            return "ok"
        return ""
