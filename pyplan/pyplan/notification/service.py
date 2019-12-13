import json

import requests

from pyplan.pyplan.common.baseService import BaseService


class NotificationService(BaseService):
    def retrieveMessages(self):
        try:
            if self.client_session and self.client_session.userId:
                msg_url = f'https://ping.pyplan.com/msg/{self.client_session.userId}'
                response = requests.get(url=msg_url)
                messages = json.loads(response.content)['content']
                return messages
        except Exception as ex:
            print(ex)

    def updateMessage(self, id):
        try:
            msg_url = f'https://ping.pyplan.com/msg/{id}'
            requests.patch(url=msg_url)
        except Exception as ex:
            print(ex)
