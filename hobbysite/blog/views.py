from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Article, ArticleCategory, Comment
from .forms import CommentForm
import random
# Create your views here.


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'article_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        if len(Article.objects.all()) > 1:
            all_articles = Article.objects.all()
            random_articles = [
                random.randint(0, len(all_articles)-1)
                for _ in range(5)
            ]
            context['random_articles'] = []
            for i in random_articles:
                context['random_articles'].append(all_articles[i])
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['all_objects'] = Article.objects.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.article = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'category', 'entry', 'header_image']
    template_name = 'article_form.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ['title', 'category', 'entry', 'header_image']
    template_name = 'article_form.html'
