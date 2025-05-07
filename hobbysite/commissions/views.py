from .models import Commission
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ComListView(ListView):
    model = Commission
    template_name = 'commission-list.html'


class ComDetailView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'commission-detail.html'
    redirect_field_name = 'login.html'


class ComCreateView(CreateView):
    pass


class ComUpdateView(UpdateView):
    pass
