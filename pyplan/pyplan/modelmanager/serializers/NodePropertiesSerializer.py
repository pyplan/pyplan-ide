from rest_framework import serializers
from pyplan.pyplan.modelmanager.serializers.NodePropertySerializer import NodePropertySerializer

class NodePropertiesSerializer(serializers.Serializer):
    node = serializers.CharField(required=True, allow_blank=False, max_length=200)
    properties = NodePropertySerializer(many=True)
