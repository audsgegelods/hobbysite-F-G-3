from django.contrib import admin

from .models import ArticleCategory, Article, Comment


class ArticleInline(admin.TabularInline):
    model = Article


class CommentInline(admin.StackedInline):
    model = Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInline, ]

    list_display = ['name', 'description']
    search_fields = ['name']


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentInline, ]

    list_display = ['title', 'author', 'category', 'created_on', 'updated_on']
    search_fields = ['title', 'author', 'category']
    list_filter = ['title', 'author', 'updated_on']

    fields = [
        'author',
        'title',
        'header_image',
        'category',
        'entry',
        'created_on',
        'updated_on'
    ]

    readonly_fields = ['author', 'created_on']


class CommentAdmin(admin.ModelAdmin):
    model = Comment

    list_display = ['article__title', 'author', 'created_on', 'updated_on']
    search_fields = ['article__title', 'author']
    list_filter = ['author', 'updated_on']

    fields = ['author', 'article', 'entry', 'created_on', 'updated_on']
    readonly_fields = ['author', 'created_on']


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
