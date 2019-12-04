from django.contrib import admin
from .models import UserCompany


@admin.register(UserCompany)
class UserCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'active', 'company_name', 'user_id', 'username', 'name', 'get_departments',)

    list_display_links = ('id', 'username',)

    preserve_filters = True
    search_fields = ['user__username', 'user__last_name', 'user__first_name', 'departments__name', ]

    def company_name(self, obj):
        return obj.company.name

    def username(self, obj):
        return obj.user.username

    def name(self, obj):
        if obj.user.last_name:
            return f'{obj.user.first_name}, {obj.user.last_name}'
        return obj.user.first_name

    def user_id(self, obj):
        return obj.user.id

    def get_departments(self, obj):
        return ',\n'.join([department.name for department in obj.departments.all()])

    get_departments.short_description = 'Departments'
