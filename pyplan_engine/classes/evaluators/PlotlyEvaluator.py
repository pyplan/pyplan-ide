import json
from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
import plotly.io as pio
from plotly.graph_objs._figure import Figure


class PlotlyEvaluator(BaseEvaluator):

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        fig = result
        if not "layout" in fig or not "margin" in fig["layout"] or fig["layout"]["margin"]["b"] is None:
            fig.update_layout(margin=dict(b=10))
        if not "layout" in fig or not "margin" in fig["layout"] or fig["layout"]["margin"]["t"] is None:
            fig.update_layout(margin=dict(t=10))
        if not "layout" in fig or not "margin" in fig["layout"] or fig["layout"]["margin"]["l"] is None:
            fig.update_layout(margin=dict(l=10))

        res = dict()
        res["result"] = pio.to_html(
            fig, full_html=False, include_plotlyjs=False)
        return json.dumps(res)
