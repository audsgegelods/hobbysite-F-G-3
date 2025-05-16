from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from profile.admin import ProfileInline

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
