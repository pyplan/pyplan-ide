from rest_framework import serializers
from pyplan.pyplan.common.serializers.ObjectField import ObjectField


class NodePropertyAxisSerializer(serializers.Serializer):
    min = serializers.IntegerField(default=None)
    max = serializers.IntegerField(default=None)
    showTitle = serializers.BooleanField(default=True)
    isSumList = serializers.ListSerializer(child=serializers.CharField())
    title = serializers.DictField(child=serializers.CharField())
    labels = serializers.DictField(child=serializers.CharField())

class NodePropertyAxesSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=True)
    xAxis = NodePropertyAxisSerializer()
    yAxis = NodePropertyAxisSerializer()

class NodePropertyLegendSerializer(serializers.Serializer):
    enabled = serializers.BooleanField(default=True)
    layout = serializers.CharField(default="vertical")
    align = serializers.CharField(default="right")
    verticalAlign = serializers.CharField(default="middle")
    borderWidth = serializers.IntegerField(default=0)
    y = serializers.IntegerField(default=0)
    title = serializers.DictField(child=serializers.CharField())

class NodePropertyStyleSerializer(serializers.Serializer):
    text = serializers.CharField(default="#000000")
    fontWeight = serializers.CharField(default="normal")

class NodePropertyTimeChartSerializer(serializers.Serializer):
    active = serializers.BooleanField(default=False)
    possible = serializers.BooleanField(default=False)

class NodePropertySubtitleSerializer(serializers.Serializer):
    text = serializers.CharField(default="")
    verticalAlign = serializers.CharField(default="top")
    enabled = serializers.BooleanField(default=True)
    style = NodePropertyStyleSerializer()

class NodePropertyTitleSerializer(serializers.Serializer):
    text = serializers.CharField(default="")
    isCustom = serializers.BooleanField(default=False)
    align = serializers.CharField(default="center")
    margin = serializers.CharField(default="")
    verticalAlign = serializers.CharField(default="top")
    enabled = serializers.BooleanField(default=True)
    style = NodePropertyStyleSerializer()

class NodePropertyTooltipSerializer(serializers.Serializer):
    valueSuffix = serializers.CharField(default="")
    valueDecimals = serializers.IntegerField(default=2)

class NodePropertiesSerializer(serializers.Serializer):
    tooltip = NodePropertyTooltipSerializer()
    unit = serializers.CharField(default="")
    originalId = serializers.CharField(default=None)
    title = NodePropertyTitleSerializer()
    subtitle = NodePropertySubtitleSerializer()
    legend = NodePropertyLegendSerializer()
    timeChart = NodePropertyTimeChartSerializer()
    axes = NodePropertyAxesSerializer()
    drilldown = serializers.BooleanField(default=True)
    detail = serializers.BooleanField(default=True)
    zoom = serializers.BooleanField(default=True)
    cubeOptions = serializers.DictField(child=ObjectField(), default=None)
