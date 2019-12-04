from django.contrib import admin
from .models import ExternalLink


@admin.register(ExternalLink)
class ExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_path', 'is_active', 'owner', 'common_instance')
