from django.urls import path
from rest_framework.routers import DefaultRouter, url

from pyplan.pyplan.activity.views import ActivityViewSet
from pyplan.pyplan.companies.views import CompanyViewSet
from pyplan.pyplan.company_preference.views import CompanyPreferenceViewSet
from pyplan.pyplan.permissions.views import PermissionViewSet
from pyplan.pyplan.dashboard.views import DashboardView
from pyplan.pyplan.dashboard_comment.views import DashboardCommentViewSet
from pyplan.pyplan.dashboardstyle.views import DashboardStyleViewSet
from pyplan.pyplan.department.views import DepartmentViewSet
from pyplan.pyplan.diagram_shortcut.views import DiagramShortcutViewSet
from pyplan.pyplan.external_link.dashboard.views import \
    DashboardExternalLinkViewSet
from pyplan.pyplan.external_link.node.views import NodeExternalLinkViewSet
from pyplan.pyplan.external_link.report.views import ReportExternalLinkViewSet
from pyplan.pyplan.external_link.views import ExternalLinkViewSet
from pyplan.pyplan.filemanager.views import FileManagerView
from pyplan.pyplan.geo.views import GeoView
from pyplan.pyplan.healthcheck.views import HealthcheckView
from pyplan.pyplan.inputtemplate.views import InputTemplateView
from pyplan.pyplan.modelmanager.views import ModelManagerView
from pyplan.pyplan.preference.views import PreferenceViewSet
from pyplan.pyplan.preference_module.views import PreferenceModuleViewSet
from pyplan.pyplan.report.views import ReportView
from pyplan.pyplan.security.views import SecurityView
from pyplan.pyplan.user_company_preference.views import \
    UserCompanyPreferenceViewSet
from pyplan.pyplan.usercompanies.views import UserCompanyViewSet
from pyplan.pyplan.users.views import UserViewSet
from pyplan.pyplan.notification.views import NotificationViewSet

router = DefaultRouter()

# Activity
router.register(r'activities', ActivityViewSet)

# Users
router.register(r'users', UserViewSet)

# Companies
router.register(r'companies', CompanyViewSet)
router.register(r'usercompanies', UserCompanyViewSet)

# Permission
router.register(r'permissions', PermissionViewSet, base_name='permissions')

# Departments
router.register(r'departments', DepartmentViewSet)

# Dashboard
router.register(r'dashboardComments', DashboardCommentViewSet)
router.register(r'dashboardStyles', DashboardStyleViewSet,
                base_name='dashboardStyles')

# Diagram
router.register(r'diagramShortcut', DiagramShortcutViewSet)

# Preference
router.register(r'preferenceModules', PreferenceModuleViewSet)
router.register(r'preferences', PreferenceViewSet)
router.register(r'userCompanyPreferences', UserCompanyPreferenceViewSet)
router.register(r'companyPreferences', CompanyPreferenceViewSet)

# ExternalLink
router.register(r'externalLink', ExternalLinkViewSet)
router.register(r'reportExternalLink', ReportExternalLinkViewSet,
                base_name='reportExternalLink')
router.register(r'dashboardExternalLink',
                DashboardExternalLinkViewSet, base_name='dashboardExternalLink')

# Notification
router.register(r'notification',
                NotificationViewSet, base_name='notification')

urlpatterns = []
urlpatterns += SecurityView.register()
urlpatterns += ModelManagerView.register()
urlpatterns += FileManagerView.register()
urlpatterns += ReportView.register()
urlpatterns += DashboardView.register()
urlpatterns += HealthcheckView.register()
urlpatterns += GeoView.register()
urlpatterns += InputTemplateView.register()
urlpatterns += [
    path(
        'result/', NodeExternalLinkViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('result/by_node_id/<str:node_id>/',
         NodeExternalLinkViewSet.as_view({'get': 'by_node_id'})),
    path('result/<uuid:pk>/', NodeExternalLinkViewSet.as_view(
        {'post': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'},)
    ),
]

urlpatterns += router.urls
