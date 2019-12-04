from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.usercompanies.models import UserCompany
from .models import Activity, ActivityType
from django.conf import settings
import os


class ActivityService(BaseService):

    def registerOpenModel(self, file):
        self.client_session.userCompanyId
        activity = Activity.objects.update_or_create(
            type=ActivityType.MODEL,
            usercompany_id=self.client_session.userCompanyId,
            model_path=file,
            model_name=file[file.rfind('/')+1:],
        )
        # Delete entry 6 and beyond
        objects_to_remove = Activity.objects.filter(
            type=ActivityType.MODEL,
            usercompany_id=self.client_session.userCompanyId,
        ).order_by('-updated_at')[5:]
        Activity.objects.filter(pk__in=objects_to_remove).delete()

        return activity

    def registerOpenDashboard(self, dashboard):
        self.client_session.userCompanyId
        activity = Activity.objects.update_or_create(
            type=ActivityType.DASHBOARD,
            usercompany_id=self.client_session.userCompanyId,
            model_path=self.client_session.modelInfo.uri,
            model_name=self.client_session.modelInfo.name,
            info={"dashboardId": dashboard.pk, "dashboardName": dashboard.name}
        )
        # Delete entry 6 and beyond
        objects_to_remove = Activity.objects.filter(
            type=ActivityType.DASHBOARD,
            usercompany_id=self.client_session.userCompanyId,
        ).order_by('-updated_at')[5:]
        Activity.objects.filter(pk__in=objects_to_remove).delete()

        return activity

    def lastModels(self):
        model_list = Activity.objects.filter(
            type=ActivityType.MODEL,
            usercompany_id=self.client_session.userCompanyId
        ).order_by('-updated_at')[:5]
        return [model for model in model_list if os.path.isfile(os.path.join(settings.MEDIA_ROOT, "models", model.model_path))]

    def lastDashboards(self):
        return Activity.objects.filter(
            type=ActivityType.DASHBOARD,
            usercompany_id=self.client_session.userCompanyId
        ).order_by('-updated_at')[:5]
