from rest_framework import serializers

class NodeSearchResultSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, allow_blank=False, max_length=200, source="identifier")
    name = serializers.SerializerMethodField()
    completeText = serializers.CharField(allow_blank=True)
    params = serializers.CharField(required=False, default="")
    description = serializers.CharField(allow_blank=True)
    moduleId = serializers.CharField(allow_blank=False)
    nodeClass = serializers.CharField(allow_blank=False)
    title = serializers.CharField(allow_blank=True)

    def get_name(self, obj):
        return obj["title"] if obj["title"] else obj["identifier"]
