from rest_framework import serializers

from pyplan.pyplan.modelmanager.serializers.NodeInfoSerializer import NodeInfoSerializer

class NodeDiagramSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, allow_blank=False, max_length=200, source="identifier")
    title = serializers.CharField(required=False, allow_blank=True, max_length=200)
    description = serializers.CharField(required=False, allow_blank=True, max_length=200)
    nodeClass = serializers.CharField(required=True, allow_blank=False, max_length=200)
    originalId = serializers.CharField(required=False, allow_blank=True, max_length=200)
    originalClass = serializers.CharField(required=False, allow_blank=True, max_length=200)
    x = serializers.IntegerField(required=False)
    y = serializers.IntegerField(required=False)
    z = serializers.IntegerField(required=True)
    w = serializers.IntegerField(required=False)
    h = serializers.IntegerField(required=False)
    color = serializers.CharField(required=False, allow_blank=True, max_length=200, default="#6699FF")
    nodeInfo = NodeInfoSerializer(read_only=True)
    formNodeType = serializers.IntegerField(required=False)
    formNodeValue = serializers.CharField(required=False)
    formNodeLabel = serializers.CharField(required=False)
    formNodeList = serializers.ListField(child=serializers.CharField(required=False), required=False)
    formNodeExtraValue = serializers.CharField(required=False)
    formNodeFormat = serializers.CharField(required=False)
    units = serializers.CharField(required=False)
    nodeFont = serializers.CharField(required=False)
    hasPicture = serializers.BooleanField(required=False)
    errorInDef = serializers.BooleanField(required=False, default=False)
    picture = serializers.CharField(required=False)
