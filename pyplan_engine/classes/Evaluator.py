import numpy as np
import pandas as pd
import xarray as xr
import cubepy
from pyplan_engine.classes.evaluators.BaseEvaluator import BaseEvaluator
from pyplan_engine.classes.evaluators.CubepyEvaluator import CubepyEvaluator
from pyplan_engine.classes.evaluators.IPythonEvaluator import IPythonEvaluator
from pyplan_engine.classes.evaluators.NumpyEvaluator import NumpyEvaluator
from pyplan_engine.classes.evaluators.PandasEvaluator import PandasEvaluator
from pyplan_engine.classes.evaluators.XArrayEvaluator import XArrayEvaluator
from pyplan_engine.classes.evaluators.BokehEvaluator import BokehEvaluator
from pyplan_engine.classes.evaluators.PlotlyEvaluator import PlotlyEvaluator
from pyplan_engine.classes.evaluators.MatplotlibEvaluator import MatplotlibEvaluator
from pyplan_engine.classes.XHelpers import XIndex
from bokeh.plotting import Figure
from bokeh.layouts import LayoutDOM
from plotly.graph_objs._figure import Figure as PlotlyFigue
import inspect
from matplotlib.artist import Artist as MatplotlibArtist


class Evaluator(object):
    ipytonMethods = ["_repr_html_", "_repr_json_",
                     "_repr_jpeg_", "_repr_png_", "_repr_pretty_"]

    @staticmethod
    def createInstance(result):
        if result is None:
            return BaseEvaluator()
        else:
            if isinstance(result, pd.DataFrame) or isinstance(result, pd.Series) or isinstance(result, pd.Index):
                return PandasEvaluator()
            elif isinstance(result, xr.DataArray) or isinstance(result, XIndex):
                return XArrayEvaluator()
            elif isinstance(result, MatplotlibArtist) or inspect.ismodule(result) and "matplotlib.pyplot" in str(result) or isinstance(result, np.ndarray) and result.ndim > 0 and len(result) > 0 and isinstance(result.item(0), MatplotlibArtist):
                return MatplotlibEvaluator()
            elif isinstance(result, np.ndarray):
                return NumpyEvaluator()
            elif isinstance(result, Figure) or isinstance(result, LayoutDOM):
                return BokehEvaluator()
            elif isinstance(result, PlotlyFigue):
                return PlotlyEvaluator()
            elif isinstance(result, cubepy.Cube) or isinstance(result, cubepy.Index):
                return CubepyEvaluator()
            else:
                _dir = dir(result)
                if len(list(set(_dir) & set(Evaluator.ipytonMethods))) > 0:
                    return IPythonEvaluator()
                else:
                    return BaseEvaluator()
