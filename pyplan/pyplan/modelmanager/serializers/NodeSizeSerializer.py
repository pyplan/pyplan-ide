from rest_framework import serializers

class NodeSizeSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=200)
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)
    w = serializers.IntegerField(required=True)
    h = serializers.IntegerField(required=True)
