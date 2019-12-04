from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.exportNode import ExportNode
from pyplan.pyplan.dashboard.serializers.nodeQueryResult import NodeQueryResultSerializer

class ExportNodeSerializer(serializers.Serializer):
    nodeId = serializers.CharField(required=True, allow_blank=False)
    fileFormat = serializers.CharField(required=True, allow_blank=False)
    numberFormat = serializers.CharField(required=True, allow_blank=False)
    columnFormat = serializers.CharField(allow_blank=True)
    compressed = serializers.CharField(allow_blank=True)
    nodeQuery = NodeQueryResultSerializer(required=False)

    def create(self, validated_data):
        return ExportNode(**validated_data)
