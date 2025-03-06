from django.urls import path
from .views import article_list, article_detail

app_name = 'wiki'
urlpatterns = [
    path('articles/', article_list, name='article-list'),
    path('article/<int:pk>/', article_detail, name='article-detail'),
]