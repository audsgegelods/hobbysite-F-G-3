from django.contrib import admin
from .models import Commission, Job 


class JobInline(admin.TabularInline):
    model = Job


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline]


admin.site.register(Commission, CommissionAdmin)
