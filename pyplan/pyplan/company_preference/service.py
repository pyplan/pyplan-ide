from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.company_preference.models import CompanyPreference
from pyplan.pyplan.preference.models import Preference

from .models import CompanyPreference


class CompanyPreferenceService(BaseService):

    def getCompanyPreferences(self):
        company_id = self.client_session.companyId

        c_preferences = CompanyPreference.objects.filter(company_id=company_id)

        preferences = Preference.objects.all()
        for pref in preferences:
            c_pref = c_preferences.filter(preference__code=pref.code).first()
            if c_pref:
                pref.definition = c_pref.definition
        return preferences

    def getCompanyPreference(self, code):
        preference = Preference.objects.filter(code=code).first()
        if preference:
            company_id = self.client_session.companyId
            c_pref = CompanyPreference.objects.filter(
                company_id=company_id, preference__code=code).first()
            if c_pref:
                preference.definition = c_pref.definition
        return preference
