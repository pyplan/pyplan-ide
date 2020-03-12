import os
import sqlite3

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import exceptions

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.preference.models import Preference
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.usercompanies.models import UserCompany

from .models import InputTemplate


class InputTemplateService(BaseService):

    def _connect(self, entity):

        fileName = ""
        if entity.filepath:
            if self.checkModelOpen():
                basepath = os.path.dirname(self.client_session.modelInfo.uri)
                fileName = os.path.join(settings.MEDIA_ROOT, "models", basepath, entity.filepath)
            else:
                raise exceptions.NotAcceptable("you must have an open model")
        else:
            basepath = os.path.join(settings.MEDIA_ROOT, 'forms', entity.owner.company.code)
            fileName = os.path.join(basepath, "input_templates.db")

        if not os.path.isfile(fileName):
            # create file
            os.makedirs(os.path.dirname(fileName), exist_ok=True)

        conn = sqlite3.connect(fileName)
        conn.isolation_level = None
        return conn

    def drop_entity(self, entity):
        """Drop entity from database"""
        conn = self._connect(entity)
        try:
            cursor = conn.cursor()
            cursor.executescript(f"DROP TABLE [{entity.code}];")
        finally:
            conn.close()

    def generate_entity(self, entity):
        """Generate entity in dabatase"""
        conn = self._connect(entity)
        try:
            key = entity.code
            cursor = conn.cursor()

            if not self.exists(key, cursor=cursor):

                indexes = f"CREATE INDEX [{entity.code}_userId] ON [{entity.code}]([userId] ASC); "

                sql = f"CREATE TABLE {entity.code}( id INTEGER PRIMARY KEY AUTOINCREMENT "

                for col in entity.definition["columns"]:

                    if col["type"] == "numeric":
                        precision = "12,2"
                        if "columnLength" in col and col["columnLength"]:
                            precision = col["columnLength"]

                        sql += f", [{col['field']}] DECIMAL({precision})"
                    elif col["type"] == "text":
                        sql += f", [{col['field']}] TEXT"
                    elif col["type"] == "dateTime":
                        sql += f", [{col['field']}] DATETIME"
                    elif col["type"] == "dropdown" or col["type"] == "remoteDropdown":
                        sql += f", [{col['field']}] INTEGER"
                        indexes += f"CREATE INDEX [{entity.code}_{col['field']}] ON [{entity.code}]([{col['field']}]); "

                sql += ", userId INTEGER"
                sql += ", lastUpdate DATETIME"
                sql += ", [departments] TEXT "
                sql += ", [users] TEXT )"

                cursor.executescript(sql)
                cursor.executescript(indexes)

                return True
        finally:
            conn.close()

    def exists(self, table, cursor):
        """Return True if table exists in db"""
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        res = cursor.fetchone()
        return True if res else False

    def list(self):
        """Return list of Input Templates """
        res = []
        queryset = None
        if self.current_user.has_perm("pyplan.view_all_input_templates"):
            company_id = self.client_session.companyId
            res = InputTemplate.objects.filter(owner__company_id=company_id)
        elif self.current_user.has_perm("pyplan.view_my_input_templates"):
            usercompany_id = self.client_session.userCompanyId
            res = InputTemplate.objects.filter(owner__id=usercompany_id)

        # apply security on department list
        if len(res) > 0:
            my_departments = self.getMyDepartments().split(",")
            res = res.filter(Q(departments__pk__isnull=True) | Q(departments__pk__in=my_departments))

        return res

    def getMetadata(self, id=None, code=None):
        """Return input template metadata"""
        input_template = None
        if id:
            input_template = InputTemplate.objects.get(pk=id)
        else:
            input_template = InputTemplate.objects.get(code=code)
        
        self._checkInputTemplateSecurity(input_template)
        res = input_template.definition
        res["code"] = input_template.code
        res["name"] = input_template.name
        res["companyId"] = input_template.owner.company_id
        return res

    def getData(self, params):
        """Retun data of input tempalte"""

        input_template = None
        if "id" in params and params["id"]:
            input_template = InputTemplate.objects.get(pk=params["id"])
        else:
            input_template = InputTemplate.objects.get(code=params["code"])

        self._checkInputTemplateSecurity(input_template)
        self._fillSecurityInRelatedEntities(input_template)
        return self._getData(input_template, params)

    def setData(self, params):
        """Set data of input tempalte"""

        input_template = None
        if "id" in params and params["id"]:
            input_template = InputTemplate.objects.get(pk=params["id"])
        else:
            input_template = InputTemplate.objects.get(code=params["code"])

        self._checkInputTemplateSecurity(input_template)
        return self._setData(input_template, params)

    def _getData(self, entity, params):
        """ Interal method for return input template data"""

        res = []
        entity_code = entity.code
        conn = self._connect(entity)
        try:
            conn.create_function("INLIST", 2, self._inlist)

            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if not self.exists(entity_code, cursor):
                self.generate_entity(entity)

            my_departments = ""
            my_users = ""
            for column in entity.definition["columns"]:
                if "entityFilterByDepartment" in column or column["type"] == "departmentSelector":
                    my_departments = self.getMyDepartments()
                if "entityFilterByUser" in column or column["type"] == "userSelector":
                    my_users = self.getMyUsers()

            # Create columnames for each column in entity metadata. Adding too related fields
            columnNames = "A.id"
            leftJoin = ""
            letter = "B"
            thisEntityHaveDepartmentFilter = False
            thisEntityHaveUserFilter = False
            for column in entity.definition["columns"]:

                if column["type"] in ["numeric", "text"]:
                    columnNames += f", A.[{column['field']}]"

                elif column["type"] == "dateTime":
                    columnNames += f", strftime('%Y-%m-%d',{column['field']}) as [{column['field']}]"

                elif column["type"] in ["dropdown", "remoteDropdown"]:
                    columnNames += f", A.[{column['field']}]"
                    columnNames += f", {letter}.[{column['entityLabel']}] as {letter}_label"
                    leftJoin += f" LEFT JOIN [{column['entity']}] as {letter} ON {letter}.id = A.{column['field']} "

                    if "entityFilterByDepartment" in column:
                        leftJoin += f' AND ( {letter}.departments is null or INLIST({letter}.departments,"{my_departments}") = 1 ) '
                    if "entityFilterByUser" in column:
                        leftJoin += f' AND ( {letter}.users is null or INLIST({letter}.users,"{my_users}") = 1 ) '

                    letter = self.getNextLetter(letter)

                elif column["type"] == "departmentSelector":
                    columnNames += f", A.[departments]"
                    thisEntityHaveDepartmentFilter = True

                elif column["type"] == "userSelector":
                    columnNames += f", A.[users]"
                    thisEntityHaveUserFilter = True

                elif column["type"] == "relatedEntity":
                    columnNames += f", {letter}.[{column['entityLabel']}] as {column.field}"
                    if "relatedColumnRelation" in column and column["relatedColumnRelation"]:
                        left_on = str(column['relatedColumnRelation']).replace(
                            "#entity#", "A").replace("#relatedEntity#", letter)
                        leftJoin += f" LEFT JOIN [{column['entity']}] as {letter} ON {left_on} "
                    else:
                        leftJoin += f" LEFT JOIN [{column['entity']}] as {letter} ON {letter}.id = A.{column['relatedForeignKey']} "
                    letter = self.getNextLetter(letter)

            sortBy = "A.ID"
            if "sortBy" in params and params["sortBy"]:
                sortBy = f'A.{params["sortBy"]}'
            elif "sortBy" in entity.definition and entity.definition["sortBy"]:
                sortBy = f'A.{entity.definition["sortBy"]}'
            where = ""
            letter = "B"

            if thisEntityHaveDepartmentFilter:
                where = f' WHERE ( A.departments is null or INLIST(A.departments,"{my_departments}") = 1 ) '
            if thisEntityHaveUserFilter:
                where = f' WHERE ( A.users is null or INLIST(A.users,"{my_users}") = 1 ) '

            # Add filter for group in related entities
            for column in entity.definition["columns"]:
                if column["type"] in ["dropdown", "remoteDropdown"] and ("entityFilterByDepartment" in column or "entityFilterByUser" in column):
                    where += " AND " if where else " WHERE "
                    where += f'A.{column["field"]} is null or A.{column["field"]} is not null and {letter}.id is not null '
                letter = self.getNextLetter(letter)

            param_list = tuple()
            if "filters" in params and params["filters"] and len(params["filters"]) > 0:
                for filter_item in params["filters"]:
                    if "values" in filter_item and filter_item["values"] and len(filter_item["values"]) > 0:
                        if where == "":
                            where = " WHERE "
                        else:
                            where += " AND "

                        if "." in str(filter_item["field"]):
                            mm_entity = "MM" + str(filter_item["field"]).split(".")[0]
                            mm_field = str(filter_item["field"]).split(".")[1]
                            if len(filter_item["values"]) == 1:
                                where += f" {mm_entity}.[{mm_field}] = ?"
                                param_list += (append(filter_item["values"][0]),)
                            else:
                                where += f" {mm_entity}.[{mm_field}] IN ({','.join( filter_item['values'])})"

                            leftJoin += f" INNER JOIN [{filter_item['field'].split('.')[0]}] as {mm_entity} ON {mm_entity}.{filter_item['relatedManyToManyKey']} = A.id "
                        else:
                            if len(filter_item["values"]) == 1:
                                if filter_item["useLike"]:
                                    where += f" A.[{filter_item['field']}] LIKE ?"
                                    param_list += (f"%{filter_item['values'][0]}%",)
                                else:
                                    where += f" A.[{filter_item['field']}] = ?"
                                    param_list += (filter_item["values"][0],)
                            else:
                                if filter_item["useLike"]:
                                    where += " ( 1=2 "
                                    for filter_value in filter_item["values"]:
                                        if filter_value:
                                            where += f" OR A.[{filter_item['field']}] LIKE ?"
                                            param_list += (f"%{filter_value}%",)
                                    where += " ) "
                                else:
                                    where += f" A.[{filter_item['field']}] IN ({','.join( filter_item['values'])})"

            # Add fixed condition
            if "condition" in entity.definition and entity.definition["condition"]:
                if where == "":
                    where = " WHERE "
                else:
                    where += " AND  "
                where += entity.definition["condition"]

            sql = f"SELECT {columnNames} FROM {entity_code} as A {leftJoin}"
            if where != "":
                sql += where

            sql += f" ORDER BY {sortBy}"

            if "fromReg" in params and params["fromReg"] > 0 and "toReg" in params and params["toReg"] > 0:
                sql += F" LIMIT {params['fromReg']-1}, {params['toReg']-params['fromReg']+1} "

            cursor.execute(sql, param_list)
            for row in cursor:
                dic = {"id": row["id"]}
                letter = "B"

                for column in entity.definition["columns"]:

                    if column["type"] in ["numeric", "text", "dateTime", "date"]:
                        dic[column["field"]] = row[column["field"]]
                    elif column["type"] in ["dropdown", "remoteDropdown"]:
                        dic[column["field"]] = f"{row[column['field']]}|-|{row[f'{letter}_label']}"
                        letter = self.getNextLetter(letter)
                    elif column["type"] == "departmentSelector":
                        dic["departments"] = row["departments"]
                    elif column["type"] == "userSelector":
                        dic["users"] = row["users"]
                    elif column["type"] == "relatedEntity":
                        dic[column["field"]] = row[column["field"]]
                        letter = self.getNextLetter(letter)

                res.append(dic)

        finally:
            conn.close()

        return res

    def _setData(self, entity, params):
        """ Interal method for setting input template data"""
        res = []
        entity_code = entity.code
        conn = self._connect(entity)
        try:
            cursor = conn.cursor()
            if not self.exists(entity_code, cursor):
                self.generate_entity(entity)

            usercompany_id = self.client_session.userCompanyId

            for row in params["rows"]:

                sqlBuild = []
                paramList = tuple()

                if row["id"] > 0:  # UPDATE

                    sqlBuild.append(f" UPDATE {entity_code} SET ")
                    sqlBuild.append(" userId = ?, lastUpdate=datetime('now') ")
                    paramList = paramList + (usercompany_id,)

                    for change in row["changes"]:
                        sqlBuild.append(f", [{change['field']}] = ?")
                        if "value" in change and change["value"]:
                            paramList = paramList + (change["value"],)
                        else:
                            paramList = paramList + (None,)

                    sqlBuild.append(f" WHERE id = {row['id']};")
                    res.append({"id": row["id"], "newId": row["id"], "rowIndex": row["rowIndex"]})

                    try:
                        res_update = cursor.execute(" ".join(sqlBuild), paramList)
                        if res_update is None or res_update.rowcount <= 0:
                            res[len(res) - 1]["err"] = "Error"
                    except Exception as ex:
                        res[len(res) - 1]["err"] = str(ex)

                else:  # INSERT
                    sqlBuild.append(f" INSERT INTO {entity_code} (userId,lastUpdate ")
                    for change in row["changes"]:
                        sqlBuild.append(f", [{change['field']}]")
                    sqlBuild.append(f") VALUES ({usercompany_id}, datetime('now') ")
                    
                    for change in row["changes"]:
                        sqlBuild.append(f", '{change['value']}'")

                    sqlBuild.append(");")
                    
                    res.append({"id": row["id"], "newId": row["id"],
                                "rowIndex": row["rowIndex"] if "rowIndex" in row else -1})

                    try:
                        execute_result = cursor.execute(" ".join(sqlBuild), paramList)
                        if not execute_result is None:
                            cursor.execute(" select last_insert_rowid() as newid ")
                            last_inserted = cursor.fetchone()
                            if last_inserted is None:
                                res[len(res) - 1]["err"] = "Error"
                            else:
                                res[len(res) - 1]["newId"] = last_inserted[0]

                        else:
                            raise ValueError("Error in insert command")
                    except Exception as ex:
                        res[len(res) - 1]["err"] = str(ex)

            if "toDelete" in params and len(params["toDelete"]) > 0:
                for id_to_delete in params["toDelete"]:
                    res.append({"id": id_to_delete, "newId": id_to_delete, "rowIndex": -1})
                    try:
                        cursor.executescript(f"DELETE FROM [{entity.code}] WHERE id = {id_to_delete};")
                    except Exception as ex:
                        res[len(res) - 1]["err"] = str(ex)

            self._saveUser(cursor)

        finally:
            conn.close()

        return res

    def getNextLetter(self, letter):
        """ return next letter """
        res = ""
        aux = letter[-1:]  # Right(letter, 1)
        if aux == "Z":
            res = letter + "A"
        else:
            next_letter = chr(ord(aux)+1)
            if len(letter) == 1:
                res = next_letter
            else:
                res = letter[:-1] + next_letter
        return res
    
    def getMyDepartments(self):
        """ return list of my departments """
        my_departments = None
        if self.current_user.is_superuser or self.current_user.has_perm("manage_input_templates"):
            my_departments = Department.objects.filter(
                company__pk=self.client_session.companyId).all()
        else:
            my_departments = Department.objects.filter(
                usercompanies__pk=self.client_session.userCompanyId).all()

        ids = []
        if my_departments.count() > 0:
            ids = [str(d.id) for d in my_departments]
        return ",".join(ids)

    def getMyUsers(self):
        """ return my user id or list of all users """
        my_users = None
        if self.current_user.is_superuser or self.current_user.has_perm("manage_input_templates"):
            my_users = UserCompany.objects.filter(
                company__pk=self.client_session.companyId).all()
        else:
            my_users = UserCompany.objects.filter(pk=self.client_session.userCompanyId).all()

        ids = []
        if my_users.count() > 0:
            ids = [str(d.id) for d in my_users]
        return ",".join(ids)

    def _inlist(self, source, target):
        """ function for sqlite for compare two arrays in string format """
        source = "" if not source else source
        target = "" if not target else target
        source_list = source.split(",")
        target_list = target.split(",")
        return 1 if len([value for value in source_list if value in target_list]) > 0 else 0

    def _fillSecurityInRelatedEntities(self, input_template):
        """ fill security info for related entities """

        if not input_template.definition is None and "columns" in input_template.definition:
            for column in input_template.definition["columns"]:
                if column["type"] in ["dropdown", "remoteDropdown"]:
                    related_input_template = InputTemplate.objects.get(code=column["entity"])
                    for related_column in related_input_template.definition["columns"]:
                        if related_column["type"] == "departmentSelector":
                            column["entityFilterByDepartment"] = True
                            break

    def _checkInputTemplateSecurity(self, input_template):
        """ check if current user can view the input template """
        if input_template.departments.count() > 0:
            ids = [str(d.id) for d in input_template.departments.all()]
            my_departments = self.getMyDepartments()
            if not self._inlist(",".join(ids), my_departments):
                raise exceptions.PermissionDenied()

    def _saveUser(self, cursor):
        """ add usercompany data to _users_ table """
        user_tablename = "_users_"
        if not self.exists(user_tablename, cursor):
            sql = f"CREATE TABLE {user_tablename}(id INTEGER PRIMARY KEY, user_code TEXT, firstname TEXT, lastname TEXT)"
            cursor.executescript(sql)
        sql = f"  INSERT INTO {user_tablename}(id,user_code,firstname,lastname)"
        sql += f" SELECT {self.client_session.userCompanyId},?,?,? "
        sql += f" WHERE NOT EXISTS( SELECT 1 FROM {user_tablename} WHERE id = {self.client_session.userCompanyId} )"
        params = (self.current_user.username, self.client_session.userFirstName,
                  self.client_session.userLastName)
        cursor.execute(sql, params)

