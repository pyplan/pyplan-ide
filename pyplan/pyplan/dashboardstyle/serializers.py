from rest_framework import serializers

from .models import DashboardStyle


class DashboardStyleSerializer(serializers.ModelSerializer):
    definition = serializers.JSONField()

    class Meta:
        model = DashboardStyle
        fields = '__all__'


class DashboardStyleImportSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    definition = serializers.JSONField()
    style_type = serializers.IntegerField()
