from rest_framework import serializers

from pyplan.pyplan.external_link.serializers import ExternalLinkSerializer

from .models import NodeExternalLink


class NodeExternalLinkSerializer(ExternalLinkSerializer):

    class Meta:
        model = NodeExternalLink
        fields = '__all__'
