from pyplan.pyplan.dashboard.classes.nodeQueryResult import NodeQueryResult

class ExportNode(object):
    def __init__(self, **kargs):
        self.nodeId = kargs["nodeId"] if "nodeId" in kargs else None
        self.fileFormat = kargs["fileFormat"] if "fileFormat" in kargs else None
        self.numberFormat = kargs["numberFormat"] if "numberFormat" in kargs else None
        self.columnFormat = kargs["columnFormat"] if "columnFormat" in kargs else None
        self.compressed = kargs["compressed"] if "compressed" in kargs else None
        self.nodeQuery = NodeQueryResult(**kargs["nodeQuery"]) if "nodeQuery" in kargs else None
