from django.contrib import admin
from .models import UserCompanyPreference


@admin.register(UserCompanyPreference)
class UserCompanyPreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'preference_code', 'definition')

    def preference_code(self, obj):
        return obj.preference.code

    def company_name(self, obj):
        return obj.company.name

    preference_code.admin_order_field = 'preference__code'
