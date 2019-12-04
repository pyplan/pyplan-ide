from rest_framework import serializers

from pyplan.pyplan.modelmanager.serializers.NodeSerializer import NodeSerializer

class NodesSerializer(serializers.Serializer):
    NodeSerializer(many=True)
