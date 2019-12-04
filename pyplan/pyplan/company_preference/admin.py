from django.contrib import admin
from .models import CompanyPreference


@admin.register(CompanyPreference)
class CompanyPreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'definition', 'preference')

    def company_name(self, obj):
        return obj.company.name
