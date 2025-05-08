from django.contrib import admin
from .models import Commission, Job 
from user_management.models import Profile


#class ProfileInline(admin.TabularInline):
#   model = Profile


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline]



admin.site.register(Commission, CommissionAdmin)
