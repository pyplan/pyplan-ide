from django.contrib import admin

from .models import NodeExternalLink


@admin.register(NodeExternalLink)
class NodeExternalLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_path', 'is_active', 'owner', 'node_id', 'common_instance')
