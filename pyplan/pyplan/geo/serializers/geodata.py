from rest_framework import serializers


class GeoDataPointSerializer(serializers.Serializer):
    lat = serializers.CharField(allow_blank=True)
    lng = serializers.CharField(allow_blank=True)
    geoDef = serializers.CharField(allow_blank=True)
    labelRes = serializers.CharField(allow_blank=True)
    sizeRes = serializers.CharField(allow_blank=True)
    colorRes = serializers.CharField(allow_blank=True)
    iconRes = serializers.CharField(allow_blank=True)
    id = serializers.CharField(allow_blank=True)


class GeoDataSerializer(serializers.Serializer):
    minSize = serializers.FloatField(required=False)
    maxSize = serializers.FloatField(required=False)
    minColor = serializers.FloatField(required=False)
    maxColor = serializers.FloatField(required=False)
    minIcon = serializers.CharField(allow_blank=True, required=False)
    maxIcon = serializers.CharField(allow_blank=True, required=False)
    zoomLevel = serializers.IntegerField(required=False)
    points = serializers.ListField(child=GeoDataPointSerializer())
