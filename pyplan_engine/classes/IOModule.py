import jsonpickle


class IOModule(object):

    def __init__(self, model):
        self.model = model

    def exportModule(self, moduleId, filename):
        res = False
        if self.model.existNode(moduleId):
            toSave = {
                "modelProp": self.model.modelProp,
                "nodeList": []
            }

            # add module
            mainModule = self.model.getNode(moduleId).toObj()
            toSave["nodeList"].append(mainModule)

            # add model
            mainModel = self.model.getNode(mainModule["moduleId"])
            modelObj = mainModel.toObj()
            modelObj["nodeClass"] = "model"
            modelObj["moduleId"] = "_model_"
            toSave["nodeList"].append(modelObj)

            def iterateNodes(subModuleId, toSave):
                for node in self.model.findNodes("moduleId", subModuleId):
                    if(not node.system):
                        toSave["nodeList"].append(node.toObj())
                        if node.nodeClass == "module":
                            iterateNodes(node.identifier, toSave)

            iterateNodes(moduleId, toSave)
            # add childrens

            with open(filename, 'w') as f:
                f.write(jsonpickle.encode(toSave))
                f.close()

            toSave = None
            res = True
        return res

    def importModule(self, moduleId, filename, importType):
        if importType == "0":  # merge
            return self.mergeModule(moduleId, filename)
        elif importType == "2":  # switch
            return self.switchModule(moduleId, filename)
        else:
            return False

    def mergeModule(self, moduleId, filename):
        res = False
        if self.model.existNode(moduleId):
            opened = {}
            with open(filename, 'r') as f:
                opened = jsonpickle.decode(f.read())
                f.close()
            pass
            self.model._isLoadingModel = True

            try:
                for nn, obj in enumerate(opened["nodeList"]):

                    if obj["nodeClass"] != "model":

                        if self.model.existNode(obj["identifier"]):
                            node = self.model.getNode(obj["identifier"])
                            node.definition = obj["definition"]
                            node.title = obj["title"]
                            node.description = obj["description"]
                            node.units = obj["units"]
                            node.color = obj["color"]
                            node.x = obj["x"]
                            node.y = obj["y"]
                            node.w = obj["w"]
                            node.h = obj["h"]
                            node = None
                        else:
                            if nn == 0:
                                obj["moduleId"] = moduleId
                            node = self.model.createNode(
                                obj["identifier"], moduleId=obj["moduleId"])
                            node.fromObj(obj)
                            node = None

                # generate io's
                [self.model.nodeDic[nod].generateIO()
                 for nod in self.model.nodeDic]
            finally:
                self.model._isLoadingModel = False

            res = True

        else:
            raise ValueError('Module base not found')

        return res

    def switchModule(self, moduleId, filename):
        res = False
        if self.model.existNode(moduleId):
            opened = {}
            with open(filename, 'r') as f:
                opened = jsonpickle.decode(f.read())
                f.close()
            pass

            if len(opened["nodeList"]) > 0:
                mainModule = opened["nodeList"][0]
                mainId = mainModule["identifier"]
                self.model.deleteNodes([mainId], removeAliasIfNotIn=mainId)

            self.model._isLoadingModel = True

            try:
                for nn, obj in enumerate(opened["nodeList"]):
                    if nn == 0:
                        obj["moduleId"] = moduleId

                    if obj["nodeClass"] != "model":

                        if self.model.existNode(obj["identifier"]):
                            node = self.model.getNode(obj["identifier"])
                            node.identifier = node.identifier + "_copy"

                        node = self.model.createNode(
                            obj["identifier"], moduleId=obj["moduleId"])
                        node.fromObj(obj)
                        node = None

                # generate io's
                for nodeId in self.model.nodeDic:
                    self.model.nodeDic[nodeId].generateIO()
            finally:
                self.model._isLoadingModel = False

            res = True

        else:
            raise ValueError('Module base not found')

        return res
