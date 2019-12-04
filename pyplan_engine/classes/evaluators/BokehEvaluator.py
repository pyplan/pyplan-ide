import json

from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from bokeh.embed import json_item
from bokeh.plotting import Figure
from bokeh.layouts import LayoutDOM, layout
from bokeh.models import Widget


class BokehEvaluator(BaseEvaluator):

    def evaluateNode(self, result, nodeDic, nodeId, dims=None, rows=None, columns=None, summaryBy="sum", bottomTotal=False, rightTotal=False, fromRow=0, toRow=0):
        _result = result

        if isinstance(_result, Figure):  # create layout
            _result.sizing_mode = 'stretch_both'
        elif isinstance(result, Widget):
            pass
        elif isinstance(_result, LayoutDOM):  # update layout for all childrens
            _result.sizing_mode = 'stretch_both'
            for item in _result.children:
                if isinstance(item, LayoutDOM) and not isinstance(item, Widget):
                    if item.sizing_mode is None and item.width_policy == "auto" and item.height_policy == "auto":
                        item.sizing_mode = 'stretch_both'

        res = dict()
        res["result"] = "BOKEH:" + json.dumps(json_item(_result, "#bokeh-id#"))
        return json.dumps(res)
