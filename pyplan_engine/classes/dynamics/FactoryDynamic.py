from pyplan_engine.classes.dynamics.CubepyDynamic import CubepyDynamic
from pyplan_engine.classes.dynamics.XArrayDynamic import XArrayDynamic
from pyplan_engine.classes.dynamics.PureXArrayDynamic import PureXArrayDynamic

class FactoryDynamic(object):

    @staticmethod
    def createInstance(circularNodes, node):
        if not node is None:
            DynamicClass = FactoryDynamic.findDynamicClass(circularNodes, node)
            return DynamicClass()

    @staticmethod
    def findDynamicClass(circularNodes, node):
        for nodeId in circularNodes:
            if node.model.existNode(nodeId):
                _def = node.model.getNode(nodeId).definition
                if "cp.dynamic(" in _def:
                    return CubepyDynamic
                elif "pp.dynamic(" in _def:
                    return XArrayDynamic
                elif "dynamic(" in _def:
                    return PureXArrayDynamic

        return PureXArrayDynamic
