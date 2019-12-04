from rest_framework import serializers

from pyplan.pyplan.common.serializers.ObjectField import ObjectField

from .nodeDimension import NodeDimensionSerializer
from .nodeDimensionValue import NodeDimensionValueSerializer


class NodeResultPageInfoSerializer(serializers.Serializer):
    fromRow = serializers.IntegerField(default=None)
    toRow = serializers.IntegerField(default=None)
    totalRows = serializers.IntegerField(default=None)

class NodeResultSerieSerializer(serializers.Serializer):
    name = serializers.CharField()
    data = serializers.ListSerializer(child=ObjectField())

class NodeResultColumnsSerializer(serializers.Serializer):
    name = serializers.CharField()
    categories = serializers.ListSerializer(child=ObjectField())

class NodeResultSerializer(serializers.Serializer):
    columns = NodeResultColumnsSerializer()
    series = NodeResultSerieSerializer(many=True, default=[])
    indexValues = NodeDimensionValueSerializer(many=True, default=None)
    nodeProperties = serializers.DictField(child=serializers.CharField())
    newDims = NodeDimensionSerializer(many=True, default=[])
    indexOnRow = serializers.CharField(default="")
    indexOnColumn = serializers.CharField(default="")
    pageInfo = NodeResultPageInfoSerializer(default=None)
