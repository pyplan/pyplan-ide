from pyplan.pyplan.common.baseService import BaseService
from pyplan.pyplan.company_preference.models import CompanyPreference
from pyplan.pyplan.preference.models import Preference

from .models import UserCompanyPreference


class UserCompanyPreferenceService(BaseService):

    def getUserCompanyPreferences(self):
        user_company_id = self.client_session.userCompanyId
        company_id = self.client_session.companyId

        c_preferences = CompanyPreference.objects.filter(company_id=company_id)
        uc_preferences = UserCompanyPreference.objects.filter(user_company_id=user_company_id)

        preferences = Preference.objects.all()
        for pref in preferences:
            uc_pref = uc_preferences.filter(preference__code=pref.code).first()
            if uc_pref:
                pref.definition = uc_pref.definition
            else:
                c_pref = c_preferences.filter(preference__code=pref.code).first()
                if c_pref:
                    pref.definition = c_pref.definition
        return preferences

    def getUserCompanyPreference(self, code):
        preference = Preference.objects.filter(code=code).first()
        if preference:
            user_company_id = self.client_session.userCompanyId
            uc_pref = UserCompanyPreference.objects.filter(
                user_company_id=user_company_id, preference__code=code).first()
            if uc_pref:
                preference.definition = uc_pref.definition
            else:
                company_id = self.client_session.companyId
                c_pref = CompanyPreference.objects.filter(
                    company_id=company_id, preference__code=code).first()
                if c_pref:
                    preference.definition = c_pref.definition
        return preference
