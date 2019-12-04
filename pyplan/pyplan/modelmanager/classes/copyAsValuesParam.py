class CopyAsValuesParam(object):
    def __init__(self, **kargs):
        self.nodeId = kargs["nodeId"] if "nodeId" in kargs else None
        self.asNewNode = kargs["asNewNode"] if "asNewNode" in kargs else False
