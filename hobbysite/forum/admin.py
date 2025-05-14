from django.contrib import admin
from .models import ThreadCategory, Thread, Comment


class ThreadCategoryAdmin(admin.ModelAdmin):
    model = ThreadCategory


class CommentInLine(admin.TabularInline):
    model = Comment


class ThreadAdmin(admin.ModelAdmin):
    model = Thread
    inlines = [CommentInLine]


admin.site.register(ThreadCategory, ThreadCategoryAdmin)
admin.site.register(Thread, ThreadAdmin)