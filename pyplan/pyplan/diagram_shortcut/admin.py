from django.contrib import admin
from .models import DiagramShortcut


@admin.register(DiagramShortcut)
class DiagramShortcutAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'node_id', 'name', 'usercompany')

    def usercompany(self, obj):
        return obj.usercompany.user.first_name
