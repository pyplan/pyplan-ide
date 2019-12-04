import json


class NodeInfo(dict):

    def __init__(self, showInputs, showOutputs, showLabel, showBorder, fill, useNodeFont):
        """
        self.showInputs = showInputs
        self.showOutputs = showOutputs
        self.showLabel = showLabel
        self.showBorder = showBorder
        self.fill = fill
        self.useNodeFont = useNodeFont
        """

        dict.__init__(self, showInputs=showInputs, showOutputs=showOutputs,
                      showLabel=showLabel, showBorder=showBorder, fill=fill, useNodeFont=useNodeFont)

    def __setattr__(self, name, value):
        if name == "fullset":
            arr = value.split(",")
            if (len(arr) > 6):
                self["showInputs"] = 1 if arr[1] == "1" else 0
                self["showOutputs"] = 1 if arr[2] == "1" else 0
                self["showLabel"] = 1 if arr[3] == "1" else 0
                self["showBorder"] = 1 if arr[4] == "1" else 0
                self["fill"] = 1 if arr[5] == "1" else 0
                self["useNodeFont"] = 1 if arr[6] == "1" else 0
        else:
            self[name] = value

    def __del__(self):
        self.release()

    def __repr__(self):
        return json.dumps(self.__dict__)

    def release(self):
        pass

    @property
    def showInputs(self):
        return self["showInputs"] == 1

    @property
    def showOutputs(self):
        return self["showOutputs"] == 1

    @property
    def showLabel(self):
        return self["showLabel"] == 1

    @property
    def showBorder(self):
        return self["showBorder"] == 1

    @property
    def fill(self):
        return self["fill"] == 1

    @property
    def useNodeFont(self):
        return self["useNodeFont"] == 1
