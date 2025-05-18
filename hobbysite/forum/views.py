from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from profile.models import Profile
from .models import ThreadCategory, Thread
from .forms import CommentForm


class ThreadListView(ListView):
    model = ThreadCategory
    template_name = 'thread_list.html'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ThreadDetailView, self).get_context_data(**kwargs)
        context['all_objects'] = Thread.objects.all()
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = Profile.objects.get(user=self.request.user)
            form.instance.thread = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'optional_image']
    template_name = 'thread_form.html'

    def form_valid(self, form):
        user = Profile.objects.get(user=self.request.user)
        form.instance.author = user
        return super(ThreadCreateView, self).form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'optional_image']
    template_name = 'thread_form.html'
