from django.contrib import admin
from .models import Commission, Job, JobApplication 
from user_management.models import Profile


class ProfileInline(admin.TabularInline):
   model = Profile


class JobInline(admin.TabularInline):
    model = Job


class JobAppAdmin(admin.ModelAdmin):
    model = JobApplication


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline]


class JobAdmin(admin.ModelAdmin):
    model = Job


admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobAppAdmin)
admin.site.register(Commission, CommissionAdmin)
