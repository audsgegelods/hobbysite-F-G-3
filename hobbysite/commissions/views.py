from .models import Commission, Job, JobApplication
from .forms import JobAppForm
from django.db.models import  Case, When
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class ComListView(ListView):
    model = Commission
    template_name = 'commission-list.html'

    def annotate_queryset(self):
        comms = Commission.objects.annotate(
            ordering = Case(
                When(status='Open', then=0),
                When(status='Full', then=1),
                When(status='Completed', then=2),
                When(status='Discontinued', then=3)
            )
        ).order_by('ordering')
        return comms        
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        sorted_comms = Commission.objects.annotate(
            ordering = Case(
                When(status='Open', then=0),
                When(status='Full', then=1),
                When(status='Completed', then=2),
                When(status='Discontinued', then=3)
            )
        ).order_by('ordering')

        context['created_comms'] = []
        for comm in sorted_comms:
            if comm.author == self.request.user:
                context['created_comms'].append(comm)

        context['applied_comms'] = [] #TODO TEMP
        for jobApp in JobApplication.objects.all():
            if jobApp.applicant == self.request.user:
                context['applied_comms'].append(jobApp.job.commission)

        context['sorted_comms'] = sorted_comms
        return context
    


class ComDetailView(DetailView):
    model = Commission
    template_name = 'commission-detail.html'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('commissions:detail', args=[self.pk])

    def get_context_data(self, **kwargs):
        context = super(ComDetailView, self).get_context_data(**kwargs)
        context['total_manpower'] = 0
        context['open_manpower'] = 0 #TODO Temp
        context['form'] = JobAppForm()
        context['job'] = Job()
        context['jobApp_list'] = JobApplication.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = JobAppForm(request.POST)
        if form.is_valid():
            form.instance.applicant = self.request.user
            form.instance.job = self.get_object()

            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
        

class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'job-detail.html'
    redirect_field_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jobApp_list'] = JobApplication.objects.all()
        return context


class ComCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commission-add.html'
    redirect_field_name = 'login.html'
    fields = '__all__'

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(ComCreateView, self).form_valid(form)


class ComUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ['title', 'description', 'status']
    template_name = 'commission-update.html'
    redirect_field_name = 'login.html'