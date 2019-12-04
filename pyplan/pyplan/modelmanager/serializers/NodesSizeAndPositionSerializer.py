from rest_framework import serializers

from pyplan.pyplan.modelmanager.serializers.NodeSizeSerializer import NodeSizeSerializer

class NodesSizeAndPositionSerializer(serializers.Serializer):
    values = NodeSizeSerializer(many=True)
