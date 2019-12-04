class ExportModuleToFile(object):
    def __init__(self, **kargs):
        self.moduleId = kargs["moduleId"] if "moduleId" in kargs else None
        self.exportType = kargs["exportType"] if "exportType" in kargs else None
