import os
import sqlite3

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.companies.models import Company
from pyplan.pyplan.preference.models import Preference

from .models import InputTemplate


class InputTemplateService(BaseService):
    pass

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

            if "enableHistoryChanges" in entity.definition:
                # TODO: create table for changes
                pass

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
                sql += ", [departments] TEXT )"

                cursor.executescript(sql)
                cursor.executescript(indexes)

                if "enableHistoryChanges" in entity.definition and entity.definition["enableHistoryChanges"]:
                    pass
                    # TODO: implement trigger

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

        return res

    def getMetadata(self, id=None, code=None):
        """Return input template metadata"""
        input_template = None
        if id:
            input_template = InputTemplate.objects.get(pk=id)
        else:
            input_template = InputTemplate.objects.get(code=code)
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

        # TODO: check security
        # TODO: check if related entity has filter by group

        return self._getData(input_template, params)

    def setData(self, params):
        """Set data of input tempalte"""

        input_template = None
        if "id" in params and params["id"]:
            input_template = InputTemplate.objects.get(pk=params["id"])
        else:
            input_template = InputTemplate.objects.get(code=params["code"])

        # TODO: check security
        # TODO: check if related entity has filter by group

        return self._setData(input_template, params)

    def _getData(self, entity, params):
        """ Interal method for return input template data"""

        res = []
        entity_code = entity.code
        conn = self._connect(entity)
        try:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if not self.exists(entity_code, cursor):
                self.generate_entity(entity)

            # TODO: view departments
            # Dim myGroups As String = ""
            # '' iterate all columns for determinate if is necesary get user groups
            # For Each column As TemplateColumnVO In entity.columns
            #     If column.entityFilterByGroup Or column.type = eTemplateColumnType.groupSelector Then
            #         'get myGroups
            #         myGroups = Me.getMyGroups()
            #         Exit For
            #     End If
            # Next

            # Create columnames for each column in entity metadata. Adding too related fields
            columnNames = "A.id"
            leftJoin = ""
            letter = "B"
            thisEntityHaveGroupFilter = False
            for column in entity.definition["columns"]:

                if column["type"] == "numeric" or column["type"] == "text":

                    columnNames += f", A.[{column['field']}]"

                elif column["type"] == "dateTime":
                    # TODO:  view format
                    # formatCode As String
                    # If column.dateFormat = "YYYY/MM/DD" Then
                    #     formatCode = 111
                    # End If
                    columnNames += f", strftime('%Y-%m-%d',{column['field']}) as [{column['field']}]"

                elif column["type"] == "dropdown" or column["type"] == "remoteDropdown":
                    columnNames += f", A.[{column['field']}]"
                    columnNames += f", {letter}.[{column['entityLabel']}] as {letter}_label"
                    leftJoin += f" LEFT JOIN [{column['entity']}] as {letter} ON {letter}.id = A.{column['field']} "

                    # TODO: filter by group
                    #     If column.entityFilterByGroup Then
                    #         leftJoin &= " AND ( " & letter & ".groups is null or  [dbo].[checkInList](" & letter & ".groups,'" & myGroups & "') = 1 ) "
                    #     End If

                    letter = self.getNextLetter(letter)

                elif column["type"] == "departmentSelector":
                    columnNames += f", A.[departments]"
                    thisEntityHaveGroupFilter = True

                    # Case eTemplateColumnType.groupSelector
                    #     columnNames &= ", A.[groups] "
                    #     thisEntityHaveGroupFilter = True

                    # Case eTemplateColumnType.relatedEntity
                    #     columnNames &= ", " & letter & ".[" & column.entityLabel & "] as " & column.field
                    #     If Not String.IsNullOrEmpty(column.relatedColumnRelation) Then
                    #         leftJoin &= " LEFT JOIN [" & getKey(column.entity, entity.companyId) & "] as " & letter & " ON " & column.relatedColumnRelation.Replace("#entity#", "A").Replace("#relatedEntity#", letter) & " "
                    #     Else
                    #         leftJoin &= " LEFT JOIN [" & getKey(column.entity, entity.companyId) & "] as " & letter & " ON " & letter & ".id = " & "A." & column.relatedForeignKey & " "
                    #     End If

                    #     letter = getNextLetter(letter)

                    #     End Select
                    # Next

            # TODO: includeHistory
            # If params.includeHistory Then
            #     columnNames &= ", ZZ.historyColumns "
            #     leftJoin &= " LEFT JOIN (SELECT entityId,STUFF((SELECT ',' + [ColumnName] FROM ( SELECT DISTINCT entityId, [ColumnName] FROM [" & key & "_log] ) KK  WHERE (entityId = Results.entityId)  FOR XML PATH(''),TYPE).value('(./text())[1]','VARCHAR(MAX)'),1,1,'') AS historyColumns FROM [" & key & "_log] Results GROUP BY entityId) ZZ on A.id = ZZ.entityId "
            # End If

            sortBy = "A.ID"
            if "sortBy" in params and params["sortBy"]:
                sortBy = "A." + params["sortBy"]
            elif "sortBy" in entity.definition and entity.definition["sortBy"]:
                sortBy = "A." + entity.definition["sortBy"]

            where = ""
            letter = "B"

            # TODO: grop filters
            # if thisEntityHaveGroupFilter:
            #     where = " WHERE  ( A.groups is null or [dbo].[checkInList](A.groups,'" + myGroups & "') = 1 ) "

            # TODO: 'Add filter for group in related entities
            # For Each column As TemplateColumnVO In entity.columns
            #     Select Case column.type
            #         Case eTemplateColumnType.dropdown, eTemplateColumnType.remoteDropdown
            #             If column.entityFilterByGroup Then
            #                 If where = "" Then
            #                     where = " WHERE "
            #                 Else
            #                     where &= " AND "
            #                 End If
            #                 where &= " A.[" & column.field & "] is null or  A.[" & column.field & "] is not null and " & letter & ".id is not null "
            #             End If
            #             letter = getNextLetter(letter)
            #     End Select
            # Next

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
            #row = cursor.fetchone()
            for row in cursor:
                dic = {"id": row["id"]}
                letter = "B"

                for column in entity.definition["columns"]:

                    if column["type"] in ["numeric", "text", "dateTime", "date"]:
                        dic[column["field"]] = row[column["field"]]

                    if column["type"] in ["dropdown", "remoteDropdown"]:

                        dic[column["field"]] = f"{row[column['field']]}|-|{row[f'{letter}_label']}"

                        letter = self.getNextLetter(letter)

                    # Case eTemplateColumnType.relatedEntity
                    #     row.Add(column.field, dr(column.field))
                    #     letter = getNextLetter(letter)

                    # Case eTemplateColumnType.groupSelector
                    #     row.Add("groups", dr("groups"))

                res.append(dic)
                #row = cursor.fetchone()

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

            usercompany_id = self.client_session.companyId

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

                    except:
                        res[len(res) - 1]["err"] = "Error"

                else:  # INSERT
                    sqlBuild.append(f" INSERT INTO {entity_code} (userId,lastUpdate ")
                    for change in row["changes"]:
                        sqlBuild.append(f", [{change['field']}]")
                    sqlBuild.append(f") VALUES ({usercompany_id}, datetime('now') ")
                    for change in row["changes"]:
                        sqlBuild.append(f", '{change['value']}'")

                    sqlBuild.append(");")
                    res.append({"id": row["id"], "newId": row["id"], "rowIndex": row["rowIndex"]})

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
            if len(next_letter) == 1:
                res = next_letter
            else:
                res = letter[:-1] + next_letter
        return res
