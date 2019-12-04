class NodeResult(object):
    def __init__(self, **kargs):
        self.columns = NodeResultColumns()
        self.series = list()
        self.indexValues = list()
        self.nodeProperties = dict()
        self.newDims = list()
        self.indexOnRow = ""
        self.indexOnColumn = ""
        self.pageInfo = NodeResultPageInfo() if "pageInfo" in kargs else None

class NodeResultColumns(object):
    def __init__(self):
        self.name = ""
        self.categories = list()

class NodeResultPageInfo(object):
    def __init__(self, **kargs):
        self.fromRow = kargs["fromRow"] if "fromRow" in kargs else None
        self.toRow = kargs["toRow"] if "toRow" in kargs else None
        self.totalRows = kargs["totalRows"] if "totalRows" in kargs else None

class NodeResultSerie(object):
    def __init__(self):
        self.name = object
        self.data = list()
