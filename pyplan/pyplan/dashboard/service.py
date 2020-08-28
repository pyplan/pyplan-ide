import uuid
from types import SimpleNamespace
import re
import json

from django.db.models import Q
from rest_framework import exceptions

from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.common.calcEngine import CalcEngine
from pyplan.pyplan.common.classes.eNodeProperty import eNodeProperty
from pyplan.pyplan.common.engineManager import EngineManager
from pyplan.pyplan.dashboardstyle.models import DashboardStyle
from pyplan.pyplan.department.models import Department
from pyplan.pyplan.report.models import Report
from pyplan.pyplan.usercompanies.models import UserCompany

from .classes.nodeDimension import NodeDimension
from .classes.nodeDimensionValue import NodeDimensionValue
from .classes.nodeEvalProperties import NodeEvalProperties, NodeEvalProperty
from .classes.nodeFullData import NodeFullData
from .classes.nodeProperties import NodeProperties
from .classes.nodeQueryResult import NodeQueryResult
from .classes.nodeResult import (NodeResult, NodeResultColumns,
                                 NodeResultPageInfo, NodeResultSerie)
from .classes.pivot import PivotQuery
from .models import Dashboard
from .serializers.nodeDimension import NodeDimensionSerializer
from .serializers.pivot import (PivotNodeValueChangesSerializer,
                                PivotQuerySerializer)


class DashboardManagerService(BaseService):

    def getDashboard(self, dashboard_id):
        return Dashboard.objects.get(pk=int(dashboard_id)) if dashboard_id.isnumeric() else Dashboard.objects.get(uuid=dashboard_id)

    def getDashboardByNodeID(self, node_id: str):
        return Dashboard.objects.filter(
            node=node_id,
            model=self.client_session.modelInfo.modelId,
            owner_id=self.client_session.userCompanyId,
        ).first()

    def companyDashboards(self):
        company_id = self.client_session.companyId
        model_id = self.client_session.modelInfo.modelId

        dashboards = Dashboard.objects.filter(
            model=model_id,
            node__isnull=True,
            owner__company__pk=company_id
        )
        return dashboards.order_by('name').distinct()

    def myDashboards(self, report_id=None, favs=None):
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        dashboards = Dashboard.objects.filter(
            model=model_id,
        )

        if type(favs) is bool and favs:
            dashboards = dashboards.filter(
                owner_id=usercompany_id,
                is_fav=True,
            )
        else:
            dashboards = dashboards.filter(
                node__isnull=True,
            )

            if report_id and report_id.isnumeric():
                dashboards = dashboards.filter(
                    report__pk=int(report_id),
                )
            else:
                dashboards = dashboards.filter(
                    owner_id=usercompany_id,
                    report__pk__isnull=True,
                )

        return dashboards.order_by('order', 'pk').distinct()

    def sharedWithMe(self, report_id):
        company_id = self.client_session.companyId
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        dashboards = Dashboard.objects.filter(
            # shared to specific users, me included
            Q(usercompanies__pk=usercompany_id) |
            # shared to departments where I belong
            Q(departments__usercompanies__pk=usercompany_id) |
            # public but not mine
            (Q(is_public=True) & ~Q(owner_id=usercompany_id)),
            # from the same company
            owner__company__pk=company_id,
            model=model_id,
        )

        if report_id and isinstance(report_id, int):
            dashboards = dashboards.filter(
                report__pk=int(report_id),
            )
        else:
            # exclude dashboards that are inside a shared report
            reports = Report.objects.filter(
                # shared to specific users, me included
                Q(usercompanies__pk=usercompany_id) |
                # shared to departments where I belong
                Q(departments__usercompanies__pk=usercompany_id) |
                # public but not mine
                (Q(is_public=True) & ~Q(owner_id=usercompany_id)),
                # from the same company
                owner__company__pk=company_id,
                model=model_id,
            )
            dashboards = dashboards.exclude(report__in=reports)
        return dashboards.order_by('order').distinct()

    def allMyDashboards(self):
        company_id = self.client_session.companyId
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId

        dashboards = Dashboard.objects.filter(
            Q(
                # shared to specific users, me included
                Q(usercompanies__pk=usercompany_id) |
                # shared to departments where I belong
                Q(departments__usercompanies__pk=usercompany_id) |
                # public but not mine
                (Q(is_public=True) & ~Q(owner_id=usercompany_id)),
                # from the same company
                owner__company__pk=company_id,
                model=model_id
            ) |
            # my dashboards
            Q(model=model_id,
              node__isnull=True,
              owner__id=usercompany_id)
        )

        # include dashboards that are inside a shared report
        reports = Report.objects.filter(
            # shared to specific users, me included
            Q(usercompanies__pk=usercompany_id) |
            # shared to departments where I belong
            Q(departments__usercompanies__pk=usercompany_id) |
            # public but not mine
            (Q(is_public=True) & ~Q(owner_id=usercompany_id)),
            # from the same company
            owner__company__pk=company_id,
            model=model_id,
        )
        dashboards_from_shared_reports = Dashboard.objects.filter(
            report__in=reports)
        dashboards_response = dashboards | dashboards_from_shared_reports

        return dashboards_response.order_by('name').distinct()

    def mySharedDashboards(self, report_id):
        dashboards = Dashboard.objects.filter(
            Q(departments__isnull=False) | Q(usercompanies__isnull=False) | Q(is_public=True),
            owner__pk=self.client_session.userCompanyId,
            model=self.client_session.modelInfo.modelId
        )
        return dashboards.order_by('order').distinct()

    def getNodeFullData(self, nodeQuery: NodeQueryResult):
        calcEngine = CalcEngine.factory(self.client_session)

        result = NodeFullData()
        result.itemType = "linechart"

        item_properties = NodeProperties()
        value_suffix = calcEngine.getNodeProperty(
            nodeQuery.node, eNodeProperty.UNITS.value)

        if value_suffix:
            value_suffix = f" {value_suffix}"
            item_properties.unit = f"({value_suffix})"

        item_properties.tooltip.valueSuffix = value_suffix

        # Main
        original_id = calcEngine.getNodeProperty(
            nodeQuery.node, eNodeProperty.ORIGINAL_ID.value)
        if not original_id is None:
            node_id = original_id
        else:
            node_id = nodeQuery.node

        node_title = calcEngine.getNodeProperty(
            nodeQuery.node, eNodeProperty.TITLE.value)
        node_class = calcEngine.getNodeProperty(
            node_id, eNodeProperty.CLASS.value)
        alias_class = calcEngine.getNodeProperty(
            nodeQuery.node, eNodeProperty.CLASS.value)

        item_properties.title.text = node_title

        item_type = None
        object_type = None
        node_result = None
        edit_mode = False

        if node_class == "module":
            item_type = "objectItem"
            object_type = "diagramviewer"
        elif node_class == "decision" and (calcEngine.isChoice(node_id) or calcEngine.isSelector(node_id)):
            item_type = "selector"
            node_result = self._evaluateNode(
                node_id, result.dims, result.rows, result.columns, hide_empty=nodeQuery.hideEmpty)
        elif alias_class == "formnode":
            item_type = "formnode"
            node_result = self._evaluateNode(
                nodeQuery.node, result.dims, result.rows, result.columns, hide_empty=nodeQuery.hideEmpty)
            if calcEngine.isTable(node_id):
                item_type = "nodetable"
                edit_mode = True
        elif node_class == "button":
            item_type = "button"
            item_properties.title.enabled = False
            item_properties.title.text = ""
            node_result = self._evaluateNode(
                node_id, result.dims, result.rows, result.columns, hide_empty=nodeQuery.hideEmpty)
        elif calcEngine.isIndex(node_id):
            item_type = "indexlist"
            if calcEngine.isTime(node_id):
                item_properties.index = type("obj", (object,), {"ui": "range"})
        else:
            # get dimensions
            result.dims = self.getNodeIndexes(nodeQuery.node)

            dim_list = list(result.dims).copy()

            for dim in dim_list:
                if calcEngine.isTime(dim.name) or calcEngine.isTime(dim.field):
                    dim.isTime = True
                if len(result.columns) is 0 and (dim.isTime or str(dim.field).startswith("Measures")):
                    result.dims.remove(dim)
                    result.columns.append(dim)
                    continue
                if len(result.rows) is 0:
                    result.dims.remove(dim)
                    result.rows.append(dim)
                if len(result.columns) > 0 and len(result.rows) > 0:
                    break

            # ' evaluate node
            node_result = self._evaluateNode(
                node_id,
                result.dims,
                result.rows,
                result.columns,
                "sum",
                nodeQuery.fromRow,
                nodeQuery.toRow,
                nodeQuery.hideEmpty
            )

            # Retrieves node dashboard
            dashboard = self.getDashboardByNodeID(node_id)
            if dashboard:
                if nodeQuery.resetView:
                    if nodeQuery.isView:
                        dashboard.definition = None
                        dashboard.save()
                elif dashboard.definition:
                    result.definition = dashboard.definition

            if calcEngine.isTable(node_id):
                if not result.columns is None and len(result.columns) == 0 and not result.dims is None and len(result.dims) > 0:
                    dim = result.dims[0]
                    result.dims.remove(dim)
                    result.columns.append(dim)
                item_type = "nodetable"
                item_properties.cubeOptions = dict(editMode=True)
                if result.rows and len(result.rows) > 0:
                    item_properties.cubeOptions["rows"] = [
                        str(xx.field).split(".")[0] for xx in result.rows]
                if result.columns and len(result.columns) > 0:
                    item_properties.cubeOptions["cols"] = [
                        str(xx.field).split(".")[0] for xx in result.columns]
            else:
                item_type = "indicator"
                if len(result.dims) > 0 or len(result.columns) > 0 or len(result.rows) > 0 or (not node_result is None and not node_result.series is None and len(node_result.series) > 1):
                    item_type = "table"

        result.nodeId = nodeQuery.node
        result.nodeName = node_title
        result.itemProperties = item_properties
        result.itemType = item_type
        result.objectType = object_type
        result.nodeResult = node_result

        return result

    def updateNodeViewAndRetrieveNodeDashboards(self, old_id, new_id):
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        _regex = re.compile(rf'(?<=\"nodeId\": \")({old_id})(?=\")', re.M)

        node_views = Dashboard.objects.filter(
            node=old_id,
            model=model_id,
            owner_id=usercompany_id
        )

        for view in node_views:
            view.node = new_id
            if view.definition:
                _def = json.dumps(view.definition)
                view.definition = json.loads(re.sub(_regex, new_id, _def))
            view.save()

        node_dashboards = Dashboard.objects.filter(
            node__isnull=True,
            definition__isnull=False,
            model=model_id,
            owner_id=usercompany_id
        )

        for dashboard in node_dashboards:
            _matches = re.search(_regex, json.dumps(dashboard.definition))
            if not _matches:
                node_dashboards = node_dashboards.exclude(pk=dashboard.pk)

        node_views.order_by('order', 'pk').distinct()
        node_dashboards.order_by('order', 'pk').distinct()

        return {'node_views': node_views, 'node_dashboards': node_dashboards}

    def updateNodeDashboards(self, old_id, new_id):
        usercompany_id = self.client_session.userCompanyId
        model_id = self.client_session.modelInfo.modelId
        _regex = re.compile(rf'(?<=\"nodeId\": \")({old_id})(?=\")', re.M)

        node_dashboards = Dashboard.objects.filter(
            node__isnull=True,
            definition__isnull=False,
            model=model_id,
            owner_id=usercompany_id
        )

        for dashboard in node_dashboards:
            _matches = re.search(_regex, json.dumps(dashboard.definition))
            if _matches:
                _def = json.dumps(dashboard.definition)
                dashboard.definition = json.loads(re.sub(_regex, new_id, _def))
                dashboard.save()
            else:
                node_dashboards = node_dashboards.exclude(pk=dashboard.pk)

        return node_dashboards.order_by('order', 'pk').distinct()

    def existNode(self, nodeId):
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.existNode(nodeId)

    def evaluateNode(self, nodeQuery):
        calcEngine = CalcEngine.factory(self.client_session)

        return self._evaluateNode(
            nodeQuery.node, nodeQuery.dims, nodeQuery.rows,
            nodeQuery.columns, nodeQuery.summaryBy,
            nodeQuery.fromRow, nodeQuery.toRow, nodeQuery.bottomTotal, nodeQuery.rightTotal, nodeQuery.hideEmpty)

    def getOrCreate(self, node_id):
        """
        - If the user has a dashboard for this model and node, return it.
        - Otherwise, create it and return it.
        """
        # Retrieve user dashboards for that node
        user_company_id = self.client_session.userCompanyId
        dashboard = Dashboard.objects.filter(
            node=node_id,
            model=self.client_session.modelInfo.modelId,
            owner_id=user_company_id,
        )
        if dashboard:
            return dashboard[0]
        else:
            # Create
            calcEngine = CalcEngine.factory(self.client_session)
            node_name = calcEngine.getNodeProperty(
                node_id, eNodeProperty.TITLE.value)
            return Dashboard.objects.create(
                model=self.client_session.modelInfo.modelId,
                name=node_name,
                node=node_id,
                owner_id=user_company_id,
            )

    def createDashboard(self, data):
        user_company = UserCompany(id=self.client_session.userCompanyId)
        report = None
        if "reportId" in data and not data["reportId"] is None:
            report = Report(id=data["reportId"])

        return Dashboard.objects.create(
            model=self.client_session.modelInfo.modelId,
            name=data["name"],
            node=data["node"] if "node" in data else None,
            owner=user_company,
            report=report,
        )

    def updateDashboard(self, dashboard, data):
        if "name" in data:
            dashboard.name = data["name"]
        if "definition" in data:
            dashboard.definition = data["definition"]
        if "report_id" in data:
            dashboard.report = Report(id=data["report_id"])
        if "styles" in data:
            dashboard.styles.set(
                DashboardStyle.objects.filter(pk__in=data['styles']))
        return dashboard.save()

    def bulkDelete(self, ids):
        return Dashboard.objects.filter(pk__in=ids).delete()

    def changeOrder(self, ids):
        for index, val in enumerate(ids):
            if val.isnumeric():
                dash = Dashboard.objects.get(pk=int(val))
                dash.order = index + 1
                dash.save()

    def getIndexValues(self, data):
        calcEngine = CalcEngine.factory(self.client_session)
        index_type = calcEngine.getIndexType(data['id'])
        response = calcEngine.getIndexValues(data)
        newResponse = {}

        index_values = []
        if response:
            for index_value in response:
                index_values.append(NodeDimensionValue(
                    type=index_type, value=index_value))
        newResponse['results'] = index_values
        return newResponse

    def isResultComputed(self, nodes):
        calcEngine = CalcEngine.factory(self.client_session)
        is_result = calcEngine.isResultComputed(nodes)
        res = []
        if len(is_result) == len(nodes):
            for nn, node in enumerate(nodes):
                if not is_result[nn]:
                    res.append(node)
        return res

    def getShares(self, dashboard_id):
        dashboard = Dashboard.objects.get(pk=dashboard_id)
        is_shared = dashboard.usercompanies.count() > 0 or dashboard.departments.count() > 0
        return {
            "departments": Department.objects.filter(company_id=self.client_session.companyId).all(),
            "usercompanies_shares": dashboard.usercompanies,
            "departments_shares": dashboard.departments,
            "sharedToEveryone": dashboard.is_public,
            "sharedTo": is_shared,
            "noShared": not is_shared,
        }

    def setShares(self, dashboard_id, data):
        dashboard = Dashboard.objects.get(pk=dashboard_id)

        dashboard.is_public = data["sharedToEveryone"]

        dashboard.usercompanies.clear()
        dashboard.departments.clear()

        if not data["noShared"]:
            for usercompany_id in data["usercompanies_ids"]:
                usercompany = UserCompany.objects.get(pk=usercompany_id)
                dashboard.usercompanies.add(usercompany)
            for department_id in data["departments_ids"]:
                department = Department.objects.get(pk=department_id)
                dashboard.departments.add(department)
        dashboard.save()
        return {
            "departments": Department.objects.filter(company_id=self.client_session.companyId).all(),
            "usercompanies_shares": dashboard.usercompanies,
            "departments_shares": dashboard.departments,
            "sharedToEveryone": dashboard.is_public,
            "sharedTo": dashboard.usercompanies.count() > 0 or dashboard.departments.count() > 0,
        }

    def copy(self, dashboard_id, name=None):
        dashboard = Dashboard.objects.get(pk=dashboard_id)
        if name:
            dashboard.name = name
        dashboard.pk = None
        dashboard.uuid = uuid.uuid4()
        if dashboard.owner_id != self.client_session.userCompanyId:
            dashboard.report = None
        dashboard.owner_id = self.client_session.userCompanyId
        dashboard.is_public = False
        dashboard.save()
        return dashboard.pk

    # Pivot
    def getCubeMetadata(self, query):
        calcEngine = CalcEngine.factory(self.client_session)
        result = calcEngine.getCubeMetadata(PivotQuerySerializer(query).data)
        original = calcEngine.getNodeProperty(
            query.cube, eNodeProperty.IDENTIFIER.value)

        # if not res is None and not res.nodeProperties is None:
        #     Dim srvWiki As New KnowledgeBaseService(token)
        #     res.nodeProperties.hasDescription = srvWiki.hasDescription(original)
        #     Dim srvWorkflow As New Workflow(token)
        #     res.nodeProperties.hasWorkflowTask = srvWorkflow.hasTask(original)
        return result

    def getCubeValues(self, pivotQuery: PivotQuery):
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.getCubeValues(PivotQuerySerializer(pivotQuery).data)

    def setCubeChanges(self, changes):
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.setNodeValueChanges(PivotNodeValueChangesSerializer(changes).data)

    def getCubeDimensionValues(self, query):
        calcEngine = CalcEngine.factory(self.client_session)
        return calcEngine.getCubeDimensionValues(PivotQuerySerializer(query).data)

    # Private Methods

    def _evaluateNode(
            self, node: str, dims: list, rows: list, columns: list, summary_by: str = "sum",
            from_row: int = 0, to_row: int = 0, bottom_total: bool = False, right_total: bool = False, hide_empty: str = None):

        calcEngine = CalcEngine.factory(self.client_session)
        node_result = NodeResult()

        props_to_get = [{"name": "numberFormat", "value": ""},
                        {"name": eNodeProperty.CLASS.value, "value": ""}]
        node_properties = calcEngine.getNodeProperties(node, props_to_get)
        node_class = None
        for prop in node_properties['properties']:
            if prop['name'] == "numberFormat" and prop['value']:
                node_result.nodeProperties["numberFormat"] = str(prop['value'])
            elif prop['name'] == eNodeProperty.CLASS.value:
                node_class = str(prop['value'])
            elif prop['name'] == eNodeProperty.TITLE.value and prop['value']:
                node_result.nodeProperties.update({'title': str(prop['value'])})
            elif prop['name'] == eNodeProperty.DESCRIPTION.value and prop['value']:
                node_result.nodeProperties.update({'description': str(prop['value'])})

        if calcEngine.isIndex(node):
            node_result.indexValues = self.getIndexValues({'id': node})[
                'results']

        elif node_class == "formnode":
            original_id = calcEngine.getNodeProperty(
                node, eNodeProperty.ORIGINAL_ID.value)
            if original_id:
                node_result = self._evaluateNode(
                    original_id, dims, rows, columns, hide_empty=hide_empty)

                props_to_get = [
                    {"name": "numberFormat", "value": ""},
                    {"name": "formNodeExtraValue", "value": ""}
                ]
                node_properties = calcEngine.getNodeProperties(
                    node, props_to_get)

                if node_properties and node_properties['properties'] and len(node_properties['properties']) > 0:
                    node_result.nodeProperties['originalId'] = node
                    for prop in node_properties['properties']:
                        if prop['name'] == "formNodeExtraValue":
                            node_result.nodeProperties['definition'] = str(
                                prop['value'])
        elif node_class == "button":
            node_result.nodeProperties['title'] = calcEngine.getNodeProperty(
                node, eNodeProperty.TITLE.value)
        elif node_class == "decision" and (calcEngine.isChoice(node) or calcEngine.isSelector(node)):
            node_result.nodeProperties["originalId"] = node

            node_result.nodeProperties["definition"] = calcEngine.getNodeProperty(
                node, eNodeProperty.DEFINITION.value)

            if calcEngine.isChoice(node):
                inputs = calcEngine.getNodeInputs(node)
                if inputs and len(inputs) > 0:
                    index = ""
                    for inputNode in inputs:
                        if inputNode["nodeClass"] == "index":
                            index = inputNode["id"]
                            break
                    node_result.indexValues = self.getIndexValues({'id': index})[
                        'results']
                    definition = node_result.nodeProperties["definition"]
                    start = definition.find("cp.choice(")
                    len_choice = 10
                    if start == -1:
                        start = definition.find("pp.choice(")
                    if start == -1:
                        start = definition.find("choice(")
                        len_choice = 7
                    end = definition.find(")")
                    characters = definition[start +
                                            len_choice:end].replace("(", "").replace(")", "")
                    arr = characters.split(",")
                    if len(arr) == 3 and "True" in arr[2]:
                        values = node_result.indexValues
                        values.append(NodeDimensionValue(
                            type="S", value="All"))

                current_result = calcEngine.getNodeProperty(
                    node, eNodeProperty.RESULT.value)
                if current_result:
                    for item in node_result.indexValues:
                        if item.value == current_result:
                            item.selected = True
                            exit
            elif calcEngine.isSelector(node):
                selectorData = calcEngine.getSelector(node)
                if selectorData:
                    node_result.nodeProperties["isSelector"] = "1"
                    node_result.nodeProperties["multiselect"] = "1" if selectorData["multiselect"] else "0"

                    node_result.indexValues = []
                    for nn, itemValue in enumerate(selectorData["options"]):
                        nodeValue = NodeDimensionValue(
                            type="S", value=itemValue)
                        if selectorData["multiselect"]:
                            if nn in selectorData["selected"]:
                                nodeValue.selected = True
                        else:
                            if nn == selectorData["selected"]:
                                nodeValue.selected = True
                        node_result.indexValues.append(nodeValue)

        else:
            filter_list = list()
            for dim in dims + rows + columns:
                filter_list.append(dim)

            eval_result_json = calcEngine.evaluateNode(
                node,
                NodeDimensionSerializer(dims, many=True).data,
                NodeDimensionSerializer(rows, many=True).data,
                NodeDimensionSerializer(columns, many=True).data,
                summary_by,
                from_row,
                to_row,
                bottom_total,
                right_total,
                hide_empty
            )

            result = eval_result_json["result"]

            node_result.columns = NodeResultColumns()
            node_result.columns.name = "Total"

            if isinstance(result, dict):
                if "columns" in result and len(result["columns"]) > 0:
                    for col in result["columns"]:
                        if isinstance(col, list):
                            if len(col) > 1:
                                node_result.columns.categories.append(col[1])
                            else:
                                node_result.columns.categories.append(col[0])
                        else:
                            node_result.columns.categories.append(col)
                else:
                    node_result.columns.categories.append("-")

                if "data" in result and len(result["data"]) > 0:
                    for index, data in enumerate(result["data"]):
                        serie = NodeResultSerie()
                        serie.name = result["index"][index]
                        for item in data:
                            serie.data.append(item)
                        node_result.series.append(serie)
            else:  # atomic value
                node_result.columns.categories.append("-")
                serie = NodeResultSerie()
                serie.name = "Total"
                serie.data.append(result)
                node_result.series.append(serie)

            if "onRow" in eval_result_json:
                if eval_result_json["onRow"]:
                    node_result.indexOnRow = eval_result_json["onRow"]
            if "onColumn" in eval_result_json:
                if eval_result_json["onColumn"]:
                    node_result.indexOnColumn = eval_result_json["onColumn"]

            # nodeProperties as dynamic dictionary
            node_result.nodeProperties.update({"nodeId": node})

            if "scenario" in eval_result_json:
                node_result.nodeProperties.update({"scenario": True})

            if "pageInfo" in eval_result_json:
                node_result.pageInfo = NodeResultPageInfo(
                    **eval_result_json["pageInfo"])

            if "numberFormat" in eval_result_json:
                node_result.nodeProperties.update(
                    {"numberFormat": eval_result_json["numberFormat"]})

            # get dimensions
            node_result.newDims = self.getNodeIndexes(node)

            for newDim in node_result.newDims:
                dim_in_filter = list(
                    filter(lambda item: newDim.field == item.field, filter_list))
                if len(dim_in_filter) > 0:
                    if hasattr(dim_in_filter[0], "currentLevel"):
                        newDim.currentLevel = dim_in_filter[0].currentLevel
                        for level in newDim.levels:
                            if level.field == dim_in_filter[0].currentLevel:
                                newDim.name = level.name
                                exit
                    for nodeDimVal in dim_in_filter[0].values:
                        if nodeDimVal.selected:
                            newDim.values.append(nodeDimVal)
        return node_result

    def getNodeIndexes(self, node, include_values=False):
        calcEngine = CalcEngine.factory(self.client_session)
        node_indexes = calcEngine.getNodeIndexes(node)
        result = []
        for index_item in node_indexes:
            serializer = NodeDimensionSerializer(index_item)
            node_dimension = serializer.create(serializer.data)
            if include_values:
                node_dimension.values = self.getIndexValues(
                    {'id': node_dimension.field})['results']
            result.append(node_dimension)
        return result
