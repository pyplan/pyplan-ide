from pyplan.pyplan.modelmanager.classes.eFormNodeType import eFormNodeType
from pyplan.pyplan.modelmanager.classes.nodeInfo import NodeInfo

class Node(object):
    def __init__(self, **kargs):
        # from NodeDiagramVO
        self.id = kargs["id"] if "id" in kargs else None
        self.title = kargs["title"] if "title" in kargs else None
        self.description = kargs["description"] if "description" in kargs else None
        self.nodeClass = kargs["nodeClass"] if "nodeClass" in kargs else None
        self.originalId = kargs["originalId"] if "originalId" in kargs else None
        self.originalClass = kargs["originalClass"] if "originalClass" in kargs else None
        self.x = kargs["x"] if "x" in kargs else None
        self.y = kargs["y"] if "y" in kargs else None
        self.z = kargs["z"] if "z" in kargs else None
        self.w = kargs["w"] if "w" in kargs else None
        self.h = kargs["h"] if "h" in kargs else None
        self.color = kargs["color"] if "color" in kargs else None
        self.formNodeType = eFormNodeType(kargs["formNodeType"]) if "formNodeType" in kargs else None
        self.formNodeValue = kargs["formNodeValue"] if "formNodeValue" in kargs else None
        self.formNodeLabel = kargs["formNodeLabel"] if "formNodeLabel" in kargs else None
        self.formNodeList = kargs["formNodeList"] if "formNodeList" in kargs else None
        self.formNodeExtraValue = kargs["formNodeExtraValue"] if "formNodeExtraValue" in kargs else None
        self.formNodeFormat = kargs["formNodeExtraValue"] if "formNodeFormat" in kargs else None
        self.nodeInfo = NodeInfo(**kargs["nodeInfo"]) if "nodeInfo" in kargs else None
        self.units = kargs["color"] if "color" in kargs else None
        self.nodeFont = kargs["nodeFont"] if "nodeFont" in kargs else None
        self.hasPicture = kargs["hasPicture"] if "hasPicture" in kargs else None
        self.errorInDef = kargs["errorInDef"] if "errorInDef" in kargs else None
        # From NodeVO
        self.identifier = kargs["identifier"] if "identifier" in kargs else None
        self.moduleId = kargs["moduleId"] if "moduleId" in kargs else None
        self.toObj = kargs["toObj"] if "toObj" in kargs else False
        self.originalId = kargs["originalId"] if "originalId" in kargs else None
