from django.contrib import admin
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    can_delete = False
    search_fields = ['display_name', 'email_address']
    list_filter = ['display_name']
    list_display = ['user', 'display_name', 'email_address']


admin.site.register(Profile, ProfileAdmin)
