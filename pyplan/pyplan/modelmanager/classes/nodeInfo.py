class NodeInfo(object):
    def __init__(self, **kargs):
        self.fill = kargs["fill"] if "fill" in kargs else None
        self.showBorder = kargs["showBorder"] if "showBorder" in kargs else None
        self.showInputs = kargs["showInputs"] if "showInputs" in kargs else None
        self.showLabel = kargs["showLabel"] if "showLabel" in kargs else None
        self.showOutputs = kargs["showOutputs"] if "showOutputs" in kargs else None
        self.useNodeFont = kargs["useNodeFont"] if "useNodeFont" in kargs else None
        self.formWidth = kargs["formWidth"] if "formWidth" in kargs else None
        self.showBevel = kargs["showBevel"] if "showBevel" in kargs else None
        self.showFormIcon = kargs["showFormIcon"] if "showFormIcon" in kargs else None
        self.version = kargs["version"] if "version" in kargs else None
