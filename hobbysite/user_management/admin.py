from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    search_fields = ['name', 'email']
    list_filter = ['name']
    list_display = ['user', 'name', 'email']

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)