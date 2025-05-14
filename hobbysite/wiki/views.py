from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ArticleCategory, Article
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'wiki/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ArticleCategory.objects.all()
        context['form'] = ArticleForm()
        return context

    def post(self, request, *args, **kwargs):
        # form = ArticleForm(request.POST, initial={'author': self.request.user})
        form = ArticleForm(request.POST.update({'author': self.request.user, 'article': self.get_object()}))
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        # form = CommentForm(request.POST)
        form = CommentForm(request.POST.update({'author': self.request.user, 'article': self.get_object()}))
        # form = CommentForm({'author': self.request.user, 'article': self.get_object()})
        # # form = CommentForm(request.POST, initial={'author': self.request.user, 'article': self.get_object()})
        if form.is_valid():
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'wiki/article_form.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'wiki/article_form.html'
    form_class = ArticleForm