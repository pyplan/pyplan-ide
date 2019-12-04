from rest_framework import serializers

from .models import ExternalLink


class ExternalLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalLink
        fields = '__all__'
