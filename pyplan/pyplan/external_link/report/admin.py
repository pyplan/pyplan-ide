from django.contrib import admin

from .models import ReportExternalLink


@admin.register(ReportExternalLink)
class ReportExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_path', 'is_active', 'owner', 'report', 'common_instance')
