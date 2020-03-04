from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.companies.models import Company


class CompaniesService(BaseService):

    def list(self):
        if self.current_user.is_superuser:
            return Company.objects.all()
        # return all the  companies that the user has assigned
        return Company.objects.filter(users__id=self.client_session.userId)
