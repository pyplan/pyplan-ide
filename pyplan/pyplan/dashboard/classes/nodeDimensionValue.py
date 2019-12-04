class NodeDimensionValue(object):
    def __init__(self, **kargs):
        self.type = kargs["type"] if "type" in kargs else None
        self.value = kargs["value"] if "value" in kargs else None
        self.selected = kargs["selected"] if "selected" in kargs else False
        self.geoDef = kargs["geoDef"] if "geoDef" in kargs else None
