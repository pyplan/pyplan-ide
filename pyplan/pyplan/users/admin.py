from django.contrib.auth import admin
from django.contrib.admin import register
from .models import User


@register(User)
class UserAdmin(admin.UserAdmin):
    list_display = ('id', 'username', 'last_name', 'first_name', 'email', 'active', 'system',)
