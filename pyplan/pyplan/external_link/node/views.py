from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from pyplan.pyplan.modelmanager.service import ModelManagerService
from pyplan.pyplan.security.service import SecurityService

from .models import NodeExternalLink
from .permissions import NodeExternalLinkPermissions
from .serializers import NodeExternalLinkSerializer
from .service import NodeExternalLinkService


class NodeExternalLinkViewSet(viewsets.ModelViewSet):
    """
    Updates and retrieves node external links relations
    """
    queryset = NodeExternalLink.objects.all()
    serializer_class = NodeExternalLinkSerializer
    permission_classes = (NodeExternalLinkPermissions,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance:
            security_service = SecurityService()
            session, token = security_service.getSessionFromExternalLink(instance)
            modelmanager_service = ModelManagerService(session=session)
            res = None
            try:
                res = modelmanager_service.callFunction(instance.node_id, request.data)
            except Exception as ex:
                return Response(str(ex), status=status.HTTP_406_NOT_ACCEPTABLE)
            finally:
                if not instance.common_instance:
                    modelmanager_service.closeModel()
            return Response(res)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def by_node_id(self, request, *args, **kwargs):
        """
        Retrieves NodeExternalLink by node_id
        """
        node_id = kwargs['node_id']
        if node_id:
            external_link = NodeExternalLinkService(request).getOrCreateNodeExternalLink(node_id)
            if external_link:
                return Response(NodeExternalLinkSerializer(external_link).data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
