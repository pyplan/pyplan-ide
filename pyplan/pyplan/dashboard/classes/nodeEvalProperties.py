class NodeEvalProperties(object):
    def __init__(self):
        self.node = ""
        self.properties = list()
        self.forceThisNode = False

class NodeEvalProperty(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
