
class IOEngine(object):

    def __init__(self, node):
        self.node = node
        self.inputs = []
        self.outputs = []

    def release(self):
        self.inputs = None
        self.outputs = None
        self.node = None

    def updateInputs(self, names):
        # remove prior outputs
        for inputNode in self.inputs:
            if not inputNode in names:
                if self.node.model.existNode(inputNode):
                    self.node.model.getNode(inputNode).ioEngine.removeOutput(
                        self.node.identifier)

        newInputs = []
        for nodeId in names:
            if self.node.model.existNode(nodeId):
                newInputs.append(nodeId)
                if not nodeId in self.inputs:
                    self.node.model.getNode(nodeId).ioEngine.addOutput(
                        self.node.identifier)

        self.inputs = newInputs

    def removeOutput(self, nodeId):
        if nodeId in self.outputs:
            self.outputs.remove(nodeId)

    def removeInput(self, nodeId):
        if nodeId in self.inputs:
            self.inputs.remove(nodeId)

    def addOutput(self, nodeId):
        self.outputs.append(nodeId)

    def updateNodeId(self, oldId, newId):
        for inputNode in self.inputs:
            if self.node.model.existNode(inputNode):
                self.node.model.getNode(
                    inputNode).ioEngine.updateOutputId(oldId, newId)

        for outputNode in self.outputs:
            if self.node.model.existNode(outputNode):
                self.node.model.getNode(
                    outputNode).ioEngine.updateInputId(oldId, newId)

    def updateOnDeleteNode(self):
        for inputNode in self.inputs:
            if self.node.model.existNode(inputNode):
                self.node.model.getNode(inputNode).ioEngine.removeOutput(
                    self.node.identifier)

        for outputNode in self.outputs:
            if self.node.model.existNode(outputNode):
                self.node.model.getNode(outputNode).ioEngine.removeInput(
                    self.node.identifier)

    def updateOutputId(self, oldId, newId):
        if oldId in self.outputs:
            self.outputs.remove(oldId)
        self.outputs.append(newId)

    def updateInputId(self, oldId, newId):
        if oldId in self.inputs:
            self.inputs.remove(oldId)
        self.inputs.append(newId)

        self.node.updateDefinitionForChangeId(oldId, newId)
