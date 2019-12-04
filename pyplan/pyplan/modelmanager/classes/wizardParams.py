class WizardParams(object):
    def __init__(self, **kargs):
        self.encoding = kargs["encoding"] if "encoding" in kargs else None
        self.filename = kargs["filename"] if "filename" in kargs else None
        self.nodeId = kargs["nodeId"] if "nodeId" in kargs else None
        self.indexes = kargs["indexes"] if "indexes" in kargs else None
        self.rows = kargs["rows"] if "rows" in kargs else None
        self.sep = kargs["sep"] if "sep" in kargs else None
