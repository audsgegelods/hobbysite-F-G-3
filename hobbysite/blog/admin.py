from django.contrib import admin

from .models import Article, ArticleCategory, Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory


class CommentAdmin(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentAdmin, ]


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
