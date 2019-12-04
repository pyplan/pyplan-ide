class ImportModuleMap(object):
    def __init__(self, **kargs):
        self.currentId = kargs["currentId"] if "currentId" in kargs else None
        self.currentIdChanged = kargs["currentIdChanged"] if "currentIdChanged" in kargs else None
        self.newId = kargs["newId"] if "newId" in kargs else None
        self.newIdChanged = kargs["newIdChanged"] if "newIdChanged" in kargs else None
        self.currentName = kargs["currentName"] if "currentName" in kargs else None
        self.newName = kargs["newName"] if "newName" in kargs else None
