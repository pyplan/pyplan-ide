from django.contrib import admin, messages

from .models import InputTemplate
from .service import InputTemplateService


@admin.register(InputTemplate)
class InputTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'filepath', 'owner',)

    def generate_entity(self, request, queryset):
        res = []
        srv = InputTemplateService()
        lvl = messages.SUCCESS
        for item in queryset.iterator():
            try:
                if srv.generate_entity(item):
                    res.append(f"Entity '{item.name}': GENERATED")
                else:
                    res.append(f"Entity '{item.name}': Exists")
            except Exception as ex:
                lvl = messages.ERROR
                res.append(f"Entity '{item.name}': ERROR {ex}")

        self.message_user(request, ' - '.join(res), level=lvl)

    generate_entity.short_description = "Generate Entity"

    def drop_entity(self, request, queryset):
        res = []
        srv = InputTemplateService()
        for item in queryset.iterator():
            try:
                srv.drop_entity(item)
                res.append(f"Entity '{item.name}': DELETED")
            except Exception as ex:
                res.append(f"Entity '{item.name}': ERROR {ex}")

        self.message_user(request, ' - '.join(res))

    drop_entity.short_description = "DROP Entity ! WARNING"

    actions = [generate_entity, drop_entity]
