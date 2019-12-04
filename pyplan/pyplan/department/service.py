from django.db.models import Q

from pyplan.pyplan.common.baseService import BaseService

from .models import Department
from pyplan.pyplan.companies.models import Company
import json


class DepartmentService(BaseService):

    def list(self):
        res = []
        departments = None

        # filter super
        if self.current_user.is_superuser:
            departments = Department.objects.all()
        else:
            company = Company.objects.get(id=self.client_session.companyId)
            departments = Department.objects.filter(company=company)

        if departments:
            for department in departments:
                res.append(department)

        return res

    def create(self, data):
        res = None
        company = None

        # filter super
        if self.current_user.is_superuser:
            company = Company.objects.get(id=data['company_id'])
        else:
            company = Company.objects.get(id=self.client_session.companyId)

        if company:
            department = Department.objects.create(
                code=data['code'],
                name=data['name'],
                engine_definitions=json.loads(data['engine_definitions']),
                login_action=json.loads(data['login_action']),
                denied_items=json.loads(data['denied_items']),
                company=company
            )
            res = department

        return res

    def partial_update(self, department_id, data):
        res = None
        department = Department.objects.get(id=department_id)
        if department.id is not None:
            if data['name']:
                department.name = data['name']
            if data['engine_definitions']:
                department.engine_definitions = json.loads(data['engine_definitions'])
            if data['login_action']:
                department.login_action = json.loads(data['login_action'])
            if data['denied_items']:
                department.denied_items = json.loads(data['denied_items'])
            if data['company_id']:
                department.company = Company.objects.get(id=data['company_id'])
            department.save()
            res = department
        return res

    def byCurrentCompany(self):
        return Department.objects.filter(company_id=self.client_session.companyId).all()

    def deniedByItem(self, data):
        if 'folder' in data:
            return Department.objects.filter(
                company_id=self.client_session.companyId,
                denied_items__folders__contains=data['folder'],
            ).all()
        elif 'module' in data:
            current_model_id = self.client_session.modelInfo.modelId
            return Department.objects.filter(
                Q(company_id=self.client_session.companyId) &
                Q(denied_items__modules__isnull=False) &
                Q(denied_items__modules__0__model_id=current_model_id) &
                Q(denied_items__modules__0__modules_ids__contains=data['module']),
            ).all()
        return []

    def denyItems(self, data):
        departments = Department.objects.filter(
            company_id=self.client_session.companyId,
            pk__in=data['departments'],
        ).all()
        # { "folders": ["folder_a"], "modules": [{ "model_id": "model_a", "modules_ids": ["id_of_module"] }] }
        if 'folder' in data:
            # Remove folder from departments that where not selected
            departments_to_unset = Department.objects.filter(
                company_id=self.client_session.companyId,
                denied_items__folders__contains=data['folder'],
            ).exclude(
                pk__in=data['departments'],
            ).all()
            for department in departments_to_unset:
                department.denied_items['folders'].remove(data['folder'])
            Department.objects.bulk_update(departments_to_unset, ['denied_items'])

            # Add folder to selected departments
            for department in departments:
                if not department.denied_items:
                    department.denied_items = {'folders': [], 'modules': []}
                if not 'folders' in department.denied_items:
                    department.denied_items['folders'] = []
                if not data['folder'] in department.denied_items['folders']:
                    department.denied_items['folders'].append(data['folder'])

            Department.objects.bulk_update(departments, ['denied_items'])
        elif 'module' in data:
            current_model_id = self.client_session.modelInfo.modelId
            # Remove module from departments that where not selected
            departments_to_unset = Department.objects.filter(
                Q(company_id=self.client_session.companyId) &
                Q(denied_items__modules__isnull=False) &
                Q(denied_items__modules__0__model_id=current_model_id) &
                Q(denied_items__modules__0__modules_ids__contains=data['module']),
            ).exclude(
                pk__in=data['departments'],
            ).all()
            for department in departments_to_unset:
                for denied_module in department.denied_items['modules']:
                    denied_module['modules_ids'].remove(data['module'])
            Department.objects.bulk_update(departments_to_unset, ['denied_items'])

            # Add module to selected departments
            for department in departments:
                if not department.denied_items:
                    department.denied_items = {'folders': [], 'modules': [
                        {'model_id': current_model_id, 'modules_ids': [data['module']]}]}
                elif not 'modules' in department.denied_items:
                    department.denied_items['modules'] = [
                        {'model_id': current_model_id, 'modules_ids': [data['module']]}]
                else:
                    curr_model_den_mod = list(
                        filter(lambda item: item['model_id'] == current_model_id, department.denied_items['modules']))
                    # If it exists, update the list
                    if curr_model_den_mod and curr_model_den_mod[0]:
                        if not data['module'] in curr_model_den_mod[0]['modules_ids']:
                            curr_model_den_mod[0]['modules_ids'].append(data['module'])
                    else:
                        # If it does not exist, append it
                        department.denied_items['modules'].append(
                            {'model_id': current_model_id, 'modules_ids': [data['module']]})
            Department.objects.bulk_update(departments, ['denied_items'])
        return departments
