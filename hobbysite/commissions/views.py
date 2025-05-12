from .models import Commission
from .forms import CommissionForm
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


class ComCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    #form_class = CommissionForm
    template_name = 'commission-add.html'
    redirect_field_name = 'login.html'
    fields = '__all__'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(ComCreateView, self).form_valid(form)


class ComUpdateView(UpdateView):
    pass
