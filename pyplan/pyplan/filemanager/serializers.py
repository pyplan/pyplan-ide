from rest_framework import serializers

from pyplan.pyplan.department.models import Department


class GetFoldersAndFilesSerializer(serializers.Serializer):
    folder = serializers.CharField(
        required=True, allow_blank=True, max_length=200)


class CreateFolderSerializer(serializers.Serializer):
    folder_path = serializers.CharField(
        required=True, allow_blank=True, max_length=200)
    folder_name = serializers.CharField(
        required=True, allow_blank=False, max_length=200)


class CopyFileOrFolderSerializer(serializers.Serializer):
    source = serializers.CharField(
        required=True, allow_blank=True, max_length=200)
    destination = serializers.CharField(
        required=True, allow_blank=False, max_length=200)


class DeleteFilesSerializer(serializers.Serializer):
    sources = serializers.ListField(child=serializers.CharField(
        allow_blank=False, max_length=200), min_length=1, max_length=200)


class FileEntryDataSerializer(serializers.Serializer):
    fullPath = serializers.CharField()
    fileSize = serializers.FloatField()
    extension = serializers.CharField()
    specialFolderType = serializers.IntegerField()
    specialFileType = serializers.IntegerField()
    isShared = serializers.BooleanField()
    sharedBy = serializers.CharField()
    lastUpdateTime = serializers.DateTimeField()
    hasDenied = serializers.SerializerMethodField()

    def get_hasDenied(self, obj):
        return False


class FileEntrySerializer(serializers.Serializer):
    show = serializers.BooleanField(default=True)
    text = serializers.CharField()
    type = serializers.IntegerField()
    data = FileEntryDataSerializer()


class UploadFilesSerializer(serializers.Serializer):
    folder_path = serializers.CharField(
        required=True, allow_blank=True, max_length=200)
    name = serializers.CharField(required=True, max_length=200)
    chunk = serializers.IntegerField(required=False)
    chunks = serializers.IntegerField(required=False)


class UnzipFileSerializer(serializers.Serializer):
    source = serializers.CharField(required=True, max_length=200)
    targetFolder = serializers.CharField(
        required=True, allow_blank=True, max_length=200)


class SourcesListSerializer(serializers.Serializer):
    sources = serializers.ListField(
        required=True, child=serializers.CharField(required=True, max_length=200))
