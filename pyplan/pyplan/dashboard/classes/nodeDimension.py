from ..classes.nodeDimensionValue import NodeDimensionValue


class NodeDimension(object):
    def __init__(self, **kargs):
        self.field = kargs["field"]
        self.name = kargs["name"]
        self.description = kargs["description"] if "description" in kargs else None
        self.values = list(map(lambda item: NodeDimensionValue(**item),
                               kargs["values"])) if "values" in kargs else None
        self.isTime = kargs["isTime"]
        self.isGeo = kargs["isGeo"]
        self.numberFormat = kargs["numberFormat"]
        self.levels = list(map(lambda item: NodeDimension(**item),
                               kargs["levels"])) if "levels" in kargs else None
        self.currentLevel = kargs["currentLevel"]
