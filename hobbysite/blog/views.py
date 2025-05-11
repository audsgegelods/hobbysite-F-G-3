from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Article, ArticleCategory
# Create your views here.


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(CreateView):#LoginRequiredMixin, CreateView):
    model = Article
    fields = '__all__'
    template_name = 'article_form.html'