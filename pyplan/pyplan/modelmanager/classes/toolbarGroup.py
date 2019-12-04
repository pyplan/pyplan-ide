class ToolbarGroup(object):
    def __init__(self, **kargs):
        self.label = kargs["label"] if "label" in kargs else None
        self.active = kargs["active"] if "active" in kargs else None
        self.items = kargs["items"] if "items" in kargs else None
