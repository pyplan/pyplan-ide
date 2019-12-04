from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
import json
from io import BytesIO
import base64
from matplotlib.figure import Figure as MatplotlibFigure
import inspect
import matplotlib.pyplot as plt


class MatplotlibEvaluator(BaseEvaluator):

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        fig = result
        _img = ""
        if not isinstance(fig, MatplotlibFigure):
            fig = plt

        figfile = BytesIO()
        fig.savefig(figfile, format='png')
        figfile.seek(0)  # rewind to beginning of file
        figdata_png = base64.b64encode(figfile.getvalue()).decode('utf8')
        _img = f"<img class='pyplan-autosize' src='data:image/png;base64,{figdata_png}'\>"
        nodeDic[nodeId]._result = _img
        plt.figure()

        res = dict()
        res["result"] = _img
        return json.dumps(res)
