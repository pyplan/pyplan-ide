from pyplan.pyplan.common.baseService import BaseService

from .models import NodeExternalLink


class NodeExternalLinkService(BaseService):

    def getOrCreateNodeExternalLink(self, node_id: str, common_instance: bool = True):
        """
        Get or Create NodeExternalLink by node_id
        """
        node_external_link, created = NodeExternalLink.objects.get_or_create(
            node_id=node_id,
            model_path=self.client_session.modelInfo.uri,
            owner_id=self.client_session.userCompanyId,
        )
        if created:
            node_external_link.common_instance = common_instance
            node_external_link.save()

        return node_external_link
