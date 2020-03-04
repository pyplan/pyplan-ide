from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.calcEngine import CalcEngine
from pyplan.pyplan.common.classes.eNodeProperty import eNodeProperty

from .models import DiagramShortcut


class DiagramShortcutService(BaseService):

    def list(self):
        """ List DiagramShortcut
        only for the requesting user and company
        """
        return DiagramShortcut.objects.filter(
            model=self.client_session.modelInfo.modelId,
            usercompany_id=self.client_session.userCompanyId
        )

    def create(self, data):
        """ Creates DiagramShortcut
        using model and usercompany_id from client_session
        """
        calcEngine = CalcEngine.factory(self.client_session)
        usercompany_id = self.client_session.userCompanyId
        model = self.client_session.modelInfo.modelId

        name = data['node_id']
        if calcEngine.existNode(data['node_id']):
            node_title = calcEngine.getNodeProperty(data['node_id'], eNodeProperty.TITLE.value)
            if node_title:
                name = node_title

        return DiagramShortcut.objects.create(
            model=model,
            usercompany_id=usercompany_id,
            node_id=data['node_id'],
            name=name,
        )
