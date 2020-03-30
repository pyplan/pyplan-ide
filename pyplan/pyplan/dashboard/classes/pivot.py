from .nodeDimension import NodeDimension


class PivotQueryFilter(object):
    def __init__(self, **kargs):
        self.field = kargs["field"]
        self.values = kargs["values"]
        self.level = kargs["level"]

class PivotQueryPosition(object):
    def __init__(self, **kargs):
        self.field = kargs["field"]
        self.values = kargs["values"]

class PivotQuery(object):
    def __init__(self, **kargs):
        self.cube = kargs["cube"] if "cube" in kargs else None
        self.columns = kargs["columns"] if "columns" in kargs else None
        self.hierarchicalColumns = kargs["hierarchicalColumns"] if "hierarchicalColumns" in kargs else None
        self.filters = list(map(lambda item: PivotQueryFilter(**item),
                                kargs["filters"])) if "filters" in kargs else None
        self.positionFilters = list(map(lambda item: PivotQueryPosition(**item),
                                        kargs["positionFilters"])) if "positionFilters" in kargs else None
        self.aggregator = kargs["aggregator"] if "aggregator" in kargs else None
        self.measure = kargs["measure"] if "measure" in kargs else None
        self.measures = kargs["measures"] if "measures" in kargs else None
        self.limit = kargs["limit"] if "limit" in kargs else None
        self.mode = kargs["mode"] if "mode" in kargs else None
        self.validationNode = kargs["validationNode"] if "validationNode" in kargs else None
        self.excludeEmptyValues = kargs["excludeEmptyValues"] if "excludeEmptyValues" in kargs else True
        self.text = kargs["text"] if "text" in kargs else None
        self.resultType = kargs["resultType"] if "resultType" in kargs else ""

class PivotNodeChanges(object):
    def __init__(self, **kargs):
        self.definition = kargs["definition"] if "definition" in kargs else None
        self.filterList = list(map(lambda item: dict(**item),
                                   kargs["filterList"])) if "filterList" in kargs else None

class PivotNodeValueChanges(object):
    def __init__(self, **kargs):
        self.node = kargs["node"] if "node" in kargs else None
        self.changes = list(map(lambda item: PivotNodeChanges(**item),
                                kargs["changes"])) if "changes" in kargs else None
