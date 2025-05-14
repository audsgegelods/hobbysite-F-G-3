from django import forms
from .models import Article, ArticleCategory, Comment

class ArticleForm(forms.Form):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': ('Article Title'),
            'author': ('Author'),
            'category': ('Category'),
            'entry': ('Article Contents'),
            'header_image': ('Article Header Image'),
            'created_on': ('First created on'),
            'updated_on': ('Last updated on'),
        }
        readonly_fields = ['author', 'created_on', 'updated_on']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'