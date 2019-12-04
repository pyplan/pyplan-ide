from rest_framework import serializers

class UploadFilesSerializer(serializers.Serializer):
    action = serializers.CharField(required=True, allow_blank=False)
    folder_path = serializers.CharField(required=False, allow_blank=True, max_length=200)
    name = serializers.CharField(required=True, max_length=200)
    chunk = serializers.IntegerField(required=False)
    chunks = serializers.IntegerField(required=False)
