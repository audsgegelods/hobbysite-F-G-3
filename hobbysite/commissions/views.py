from .models import Commission
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ComListView(ListView):
    model = Commission
    template_name = 'commission-list.html'


class ComDetailView(DetailView):
    model = Commission
    template_name = 'commission-detail.html'
