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
