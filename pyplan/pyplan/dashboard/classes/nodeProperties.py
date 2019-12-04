class NodeProperties(object):
    def __init__(self):
        self.tooltip = NodePropertyTooltip()
        self.unit = ""
        self.originalId = None
        self.title = NodePropertyTitle()
        self.subtitle = NodePropertySubtitle()
        self.legend = NodePropertyLegend()
        self.timeChart = NodePropertyTimeChart()
        self.axes = NodePropertyAxes()
        self.drilldown = True
        self.detail = True
        self.zoom = True

class NodePropertyTooltip(object):
    def __init__(self):
        self.valueSuffix = ""
        self.valueDecimals = 2

class NodePropertyTitle(object):
    def __init__(self):
        self.text = ""
        self.isCustom = False
        self.align = "center"
        self.margin = ""
        self.verticalAlign = "top"
        self.enabled = True
        self.style = NodePropertyStyle()

class NodePropertySubtitle(object):
    def __init__(self):
        self.text = ""
        self.verticalAlign = "top"
        self.enabled = True
        self.style = NodePropertyStyle()

class NodePropertyStyle(object):
    def __init__(self):
        self.color = "#000000"
        self.fontWeight = "normal"

class NodePropertyLegend(object):
    def __init__(self):
        self.enabled = True
        self.layout = "vertical"
        self.align = "right"
        self.verticalAlign = "middle"
        self.borderWidth = 0
        self.y = 0
        self.margin = 2
        self.title = {"text": ""}

class NodePropertyTimeChart(object):
    def __init__(self):
        self.active = False
        self.possible = False

class NodePropertyAxes(object):
    def __init__(self):
        self.enabled = True
        self.xAxis = NodePropertyAxis()
        self.yAxis = NodePropertyAxis()

class NodePropertyAxis(object):
    def __init__(self):
        self.min = None
        self.max = None
        self.showTitle = True
        self.isSumList = list()
        self.title = {"text": ""}
        self.labels = {"enabled": True, "rotation": None, "align": None}
