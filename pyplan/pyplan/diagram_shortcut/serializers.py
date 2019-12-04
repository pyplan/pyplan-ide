from rest_framework import serializers

from .models import DiagramShortcut


class DiagramShortcutSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiagramShortcut
        fields = '__all__'

class DiagramShortcutCreateSerializer(serializers.Serializer):
    node_id = serializers.CharField()
