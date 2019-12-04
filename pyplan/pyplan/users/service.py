from pyplan.pyplan.common.baseService import BaseService
from .models import User
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany
from pyplan.pyplan.companies.models import Company


class UserService(BaseService):

    def list(self):
        res = []
        users = None

        # check superuser
        if self.current_user.is_superuser:
            users = User.objects.all()
        else:
            company = Company.objects.get(id=self.client_session.companyId)
            users = User.objects.filter(company=company)

        if users:
            for user in users:
                res.append(user)

        return res

    def retrieve(self, user_id):

        user = User.objects.get(id=user_id)
        assigned = []
        for company in user.companies.values():
            comp = {}
            comp['id'] = company['id']
            comp['code'] = company['code']
            comp['name'] = company['name']
            comp['system'] = company['system']
            comp['active'] = company['active']
            comp['licence'] = company['licence']

            assigned_groups = []
            for group in user.groups.values():
                if group['company_id'] == company['id']:
                    assigned_groups.append(group)

            comp['groups'] = assigned_groups

            user_company = UserCompany.objects.get(
                company__id=company['id'], user=user)

            assigned_departments = []
            for department in user_company.departments.values():
                assigned_departments.append(department)

            comp['departments'] = assigned_departments

            assigned.append(comp)
            user.assigned = assigned

        return user
