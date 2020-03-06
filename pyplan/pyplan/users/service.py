from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import User


class UserService(BaseService):

    def list(self):
        users = None
        # check superuser
        if self.current_user.is_superuser:
            users = User.objects.all()
        else:
            users = User.objects.filter(
                company__pk=self.client_session.companyId).exclude(username='super')
        return users or []

    def retrieve(self, user_id):
        user = User.objects.get(pk=user_id)
        return user

    def partial_update(self, user_id, data):
        # only used in ide for now
        user = User.objects.get(pk=user_id)
        if user:
            user.my_uuid = data['my_uuid'] if data['my_uuid'] else user.my_uuid
            user.my_username = data['my_username'] if data['my_username'] else user.my_username
            user.first_name = data['first_name'] if data['first_name'] else user.first_name
            user.last_name = data['last_name'] if data['last_name'] else user.last_name
        user.save()

        # update session
        if self.client_session:
            self.client_session.my_uuid = user.my_uuid
            self.client_session.my_username = user.my_username
            self.client_session.userFirstName = user.first_name
            self.client_session.userLastName = user.last_name
            self.client_session.userFullName = f'{user.first_name} {user.last_name}'
            self.saveSession()

        return user
