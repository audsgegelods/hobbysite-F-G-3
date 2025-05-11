from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
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

    #https://stackoverflow.com/questions/31201124/django-detailview-get-all-objects
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['all_objects'] = Article.objects.all()

        return context


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = '__all__'
    template_name = 'article_form.html'