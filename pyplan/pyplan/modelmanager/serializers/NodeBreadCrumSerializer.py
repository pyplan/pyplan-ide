from rest_framework import serializers

class NodeBreadcrumSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, allow_blank=False, max_length=200, source="identifier")
    title = serializers.CharField(required=True, allow_blank=False, max_length=200)
