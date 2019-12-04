from rest_framework import serializers

from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    info = serializers.JSONField(required=False)

    class Meta:
        model = Activity
        fields = '__all__'
