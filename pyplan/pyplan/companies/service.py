from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.department.models import Department


class CompaniesService(BaseService):

    def list_with_groups_and_depts(self):
        res = []
        companies = None

        # check for superuser
        if self.current_user.is_superuser:
            companies = Company.objects.all()
        else:
            companies = Company.objects.filter(
                id=self.client_session.companyId)

        if companies:
            for company in companies:
                comp = {}
                comp['company'] = company
                departments = Department.objects.filter(company=company)
                comp['departments'] = departments.values()
                res.append(comp)

        return res
