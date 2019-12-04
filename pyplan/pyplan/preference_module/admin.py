from django.contrib import admin
from .models import PreferenceModule


@admin.register(PreferenceModule)
class PreferenceModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'description')
