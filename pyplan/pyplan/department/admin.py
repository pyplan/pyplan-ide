from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'code', 'name', 'engine_definitions', 'login_action', 'denied_items',)
