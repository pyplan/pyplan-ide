from django.contrib import admin
from .models import Preference


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'module_code', 'code', 'description', 'definition')

    def module_code(self, obj):
        return obj.module.code
