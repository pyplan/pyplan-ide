from django.contrib import admin

from .models import DashboardExternalLink


@admin.register(DashboardExternalLink)
class DashboardExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_path', 'is_active', 'owner', 'dashboard', 'common_instance')
