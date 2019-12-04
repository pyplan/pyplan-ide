from rest_framework import serializers

class NodeIdSerializer(serializers.Serializer):
    nodeId = serializers.CharField(required=True, allow_blank=False)
