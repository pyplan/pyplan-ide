from pyplan.pyplan.modelmanager.classes.importModuleMap import ImportModuleMap
from pyplan.pyplan.modelmanager.classes.eImportType import eImportType

class ImportModuleData(object):
    def __init__(self, **kargs):
        self.parentModelId = kargs["parentModelId"] if "parentModelId" in kargs else None
        self.importType = eImportType(kargs["importType"]) if "importType" in kargs else None
        self.moduleFile = kargs["moduleFile"] if "moduleFile" in kargs else None
        self.mapData = list(map(lambda item: ImportModuleMap(**item),
                                kargs["mapData"])) if "mapData" in kargs else None
        self.fromTemp = kargs["fromTemp"] if "fromTemp" in kargs else None
        self.currentModel = kargs["currentModel"] if "currentModel" in kargs else None
