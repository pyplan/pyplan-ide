from pyplan.pyplan.common.baseService import BaseService
from django.contrib.auth.hashers import make_password

from .models import UserCompany
from pyplan.pyplan.users.models import User
from pyplan.pyplan.companies.models import Company
from django.contrib.auth.models import Permission
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.preference.models import Preference


class UserCompanyService(BaseService):

    def list(self):

        res = []
        usercompanies = None

        # check superuser
        if self.current_user.is_superuser:
            usercompanies = UserCompany.objects.all()
        else:
            company = Company.objects.get(id=self.client_session.companyId)
            usercompanies = UserCompany.objects.filter(company=company)

        if usercompanies:
            for usercompanie in usercompanies:
                res.append(usercompanie)

        return res

    def create(self, data):
        """creates a user and it's userscompanies"""
        res = []

        # creates the user
        user = User.objects.create(
            username=data['user']['username'],
            first_name=data['user']['first_name'],
            last_name=data['user']['last_name'],
            email=data['user']['email'],
            password=make_password(data['user']['password']),
            active=data['user']['active'],
            imageURL=data['user']['imageURL'] if 'imageURL' in data['user'].keys(
            ) else None,
            langCode=data['user']['langCode'] if 'langCode' in data['user'].keys(
            ) else None,
        )

        if user.id is None:
            return res

        # add permissions to the user
        for permission_id in data['permissions']:
            user.user_permissions.add(Permission.objects.get(id=permission_id))
            user.save()

        # try to retrieve companies
        for comp_object in data['companies']:

            if not comp_object['delete']:

                company = Company.objects.get(id=comp_object['company_id'])

                # add company to the user (this creates the usercompany)
                user.companies.add(company)
                user.save()

                # get the usercompany
                user_company, created = UserCompany.objects.get_or_create(
                    user=user,
                    company=company
                )

                # get the departments
                if 'departments' in comp_object.keys():
                    for department_id in comp_object['departments']:
                        user_company.departments.add(
                            Department.objects.get(company=company, id=department_id))
                        user_company.save()

                # get the preferences
                if 'preferences' in comp_object.keys():
                    for preference_id in comp_object['preferences']:
                        user_companies.preferences.add(
                            Preference.objects.get(id=preference_id))
                        user_company.save()

                res.append(user_company)

        return res

    def partial_update(self, user_id, data):
        """partially updates a user and it's userscompanies"""
        res = []

        # gets the user
        user = User.objects.get(id=user_id)

        if user.id is None:
            return None

        # updates user data
        if 'user' in data.keys():
            if 'username' in data['user'].keys():
                user.username = data['user']['username']
            if 'first_name' in data['user'].keys():
                user.first_name = data['user']['first_name']
            if 'last_name' in data['user'].keys():
                user.last_name = data['user']['last_name']
            if 'email' in data['user'].keys():
                user.email = data['user']['email']
            if 'password' in data['user'].keys():
                user.password = make_password(data['user']['password'])
            if 'active' in data['user'].keys():
                user.active = data['user']['active']
            if 'imageURL' in data['user'].keys():
                user.imageURL = data['user']['imageURL']
            if 'langCode' in data['user'].keys():
                user.langCode = data['user']['langCode']

            user.save()

        # add permissions to the user
        if 'permissions' in data.keys():
            user.user_permissions.clear()
            for permission_id in data['permissions']:
                user.user_permissions.add(
                    Permission.objects.get(id=permission_id))
                user.save()

        # try to retrieve companies
        if len(data['companies']) > 0:
            for comp_object in data['companies']:

                company = Company.objects.get(id=comp_object['company_id'])

                # check if company should be removed from user
                if comp_object['delete']:
                    # remove company from user (this deletes the usercompany)
                    if User.objects.filter(id=user.id, company__id=company.id).exists():
                        user.companies.remove(company)
                else:
                    # add company to the user
                    if not User.objects.filter(id=user_id, company__id=company.id).exists():
                        # if company does not exist in user add it
                        user.companies.add(company)
                        user.save()

                    # create the usercompany
                    user_company, created = UserCompany.objects.get_or_create(
                        user=user,
                        company=company
                    )

                    # get the departments
                    if 'departments' in comp_object.keys():
                        user_company.departments.clear()
                        for department_id in comp_object['departments']:
                            user_company.departments.add(
                                Department.objects.get(company=company, id=department_id))
                            user_company.save()

                    # get the preferences
                    if 'preferences' in comp_object.keys():
                        user_company.preferences.clear()
                        for preference_id in comp_object['preferences']:
                            user_companies.preferences.add(
                                Preference.objects.get(id=preference_id))
                            user_company.save()

                    res.append(user_company)
        else:

            user_companies = UserCompany.objects.filter(user=user)
            for user_company in user_companies:
                res.append(user_company)

        return res

    def listByCompanyId(self):
        """Returns usercompanies by company id"""
        res = []
        company_id = self.client_session.companyId
        if company_id:
            company = Company.objects.get(id=company_id)
            users_companies = UserCompany.objects.filter(company=company)
            for uc in users_companies.values():
                user = User.objects.get(id=uc['user_id'])
                user.user_company_id = uc['id']
                res.append(user)

        return res
