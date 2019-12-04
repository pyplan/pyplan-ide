from rest_framework import serializers

from pyplan.pyplan.modelmanager.classes.node import Node
from pyplan.pyplan.modelmanager.serializers.NodeInfoSerializer import NodeInfoSerializer

class NodeSerializer(serializers.Serializer):
    # from NodeDiagramVO (same as NodeDiagramSerializer)
    id = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    nodeClass = serializers.CharField(required=False)
    originalId = serializers.CharField(required=False)
    originalClass = serializers.CharField(required=False)
    x = serializers.IntegerField(required=False)
    y = serializers.IntegerField(required=False)
    z = serializers.IntegerField(required=False)
    w = serializers.IntegerField(required=False)
    h = serializers.IntegerField(required=False)
    color = serializers.CharField(required=False, allow_blank=True, max_length=200, default="#6699FF")
    formNodeType = serializers.IntegerField(required=False)
    formNodeValue = serializers.CharField(required=False)
    formNodeLabel = serializers.CharField(required=False)
    formNodeList = serializers.ListField(child=serializers.CharField(required=False), required=False)
    formNodeExtraValue = serializers.CharField(required=False)
    formNodeFormat = serializers.CharField(required=False)
    nodeInfo = NodeInfoSerializer(required=False)
    units = serializers.CharField(required=False)
    nodeFont = serializers.CharField(required=False)
    hasPicture = serializers.BooleanField(required=False)
    errorInDef = serializers.BooleanField(required=False, default=False)
    # from NodeVO
    identifier = serializers.CharField(required=False)
    moduleId = serializers.CharField(required=False)
    toObj = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Node(**validated_data)
