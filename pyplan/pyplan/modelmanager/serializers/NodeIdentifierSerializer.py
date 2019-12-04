from rest_framework import serializers

class NodeIdentifierSerializer(serializers.Serializer):
    values = serializers.ListField(child=serializers.CharField(required=True))
