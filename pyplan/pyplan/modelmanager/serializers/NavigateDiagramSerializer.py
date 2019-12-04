from rest_framework import serializers

from pyplan.pyplan.modelmanager.serializers.NodeDiagramSerializer import NodeDiagramSerializer
from pyplan.pyplan.modelmanager.serializers.NodeBreadCrumSerializer import NodeBreadcrumSerializer
from pyplan.pyplan.modelmanager.serializers.ArrowSerializer import ArrowsSerializer

class NavigateDiagramSerializer(serializers.Serializer):
    moduleId = serializers.CharField(required=False, allow_blank=True, max_length=200)
    nodes = NodeDiagramSerializer(many=True, read_only=True)
    breadcrumb = NodeBreadcrumSerializer(many=True, read_only=True)
    arrows = ArrowsSerializer(many=True, read_only=True)
