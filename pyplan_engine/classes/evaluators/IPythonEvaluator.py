import json

from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator


class IPythonEvaluator(BaseEvaluator):
    """ IPython Evaluator. 
    Display an IPython component using _repr_*_ methods
    """

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        return self.toHTML(result)

    def previewNode(self, nodeDic, nodeId):
        res = {
            "resultType": str(type(nodeDic[nodeId].result)),
            "dims": [],
            "columns": [],
            "console": nodeDic[nodeId].lastEvaluationConsole,
            "preview": self.toHTML(nodeDic[nodeId].result)
        }
        return json.dumps(res)

    def toHTML(self, result):
        _dir = dir(result)
        if "_repr_html_" in _dir:
            return result._repr_html_()
        elif "_repr_pretty_" in _dir:
            return result._repr_pretty_()
        elif "_repr_png_" in _dir:
            return result._repr_png_()
        elif "_repr_jpeg_" in _dir:
            return result._repr_jpeg_()
        elif "_repr_json_" in _dir:
            return result._repr_json_()
