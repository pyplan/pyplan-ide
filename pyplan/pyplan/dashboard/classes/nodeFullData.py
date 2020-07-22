from .nodeResult import NodeResult

class NodeFullData(object):
    def __init__(self):
        self.nodeId = ""
        self.nodeName = ""
        self.dims = list()
        self.rows = list()
        self.columns = list()
        self.itemType = ""
        self.objectType = ""
        self.itemProperties = object
        self.nodeResult = NodeResult()
        self.definition = None
