from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from profile.models import Profile
from .models import ArticleCategory, Article, Comment
from .forms import ArticleForm, CommentForm


class ArticleListView(ListView):
    model = ArticleCategory
    template_name = 'wiki/article_list.html'
    # redirect_field_name = 'wiki:article_create'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['all_objects'] = Article.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = Profile.objects.get(user=self.request.user)
            form.instance.article = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = 'wiki/article_form.html'
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super(ArticleCreateView, self).form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'wiki/article_form.html'
    form_class = ArticleForm
    success_url = reverse_lazy('wiki:article_detail')

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super(ArticleUpdateView, self).form_valid(form)
