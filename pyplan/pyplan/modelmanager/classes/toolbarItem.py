class ToolbarItem(object):
    def __init__(self, **kargs):
        self.nodeClass = kargs["nodeClass"] if "nodeClass" in kargs else None
        self.baseClass = kargs["baseClass"] if "baseClass" in kargs else None
        self.icon = kargs["icon"] if "icon" in kargs else None
        self.label = kargs["label"] if "label" in kargs else None
        self.wizard = kargs["wizard"] if "wizard" in kargs else None
