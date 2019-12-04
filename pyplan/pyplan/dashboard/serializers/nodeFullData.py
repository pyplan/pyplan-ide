from rest_framework import serializers

from .nodeDimension import NodeDimensionSerializer
from .nodeProperties import NodePropertiesSerializer
from .nodeResult import NodeResultSerializer


class NodeFullDataSerializer(serializers.Serializer):
    nodeId = serializers.CharField()
    nodeName = serializers.CharField(default="")
    dims = NodeDimensionSerializer(many=True)
    rows = NodeDimensionSerializer(many=True)
    columns = NodeDimensionSerializer(many=True)
    itemProperties = NodePropertiesSerializer()
    itemType = serializers.CharField(default=None)
    objectType = serializers.CharField(default=None)
    nodeResult = NodeResultSerializer()
