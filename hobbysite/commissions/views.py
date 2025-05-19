from .models import Commission, Job, JobApplication
from .forms import JobForm, JobAppForm
from django.db.models import  Case, When
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from profile.models import Profile
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect


class ComListView(ListView):
    model = Commission
    template_name = 'commission-list.html'

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
            if comm.author == Profile.objects.get(user=self.request.user):
                context['created_comms'].append(comm)

        context['applied_comms'] = []
        for jobApp in JobApplication.objects.all():
            if jobApp.applicant == Profile.objects.get(user=self.request.user):
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
        for job in Job.objects.all():
            if job.commission == self.get_object():
                context['total_manpower'] += job.manpower_required

        context['open_manpower'] = context['total_manpower']
        for jobApp in JobApplication.objects.all():
            if jobApp.job.commission == self.get_object():
                if jobApp.status == 'Accepted':
                    context['open_manpower'] -= 1

        context['form'] = JobAppForm()
        context['job'] = Job()
        context['jobApp_list'] = JobApplication.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = JobAppForm(request.POST)
        if form.is_valid():
            form.instance.applicant = Profile.objects.get(user=self.request.user)
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
        context['form'] = JobAppForm()
        context['jobApps'] = []
        context['acceptedJobApps'] = []
        for jobApp in JobApplication.objects.all():
            if jobApp.job == self.get_object():
                context['jobApps'].append(jobApp)
            if jobApp.status == 'Accepted' and jobApp.job == self.get_object():
                context['acceptedJobApps'].append(jobApp)
        context['acceptedJobAppCount'] = len(context['acceptedJobApps'])

        return context
    
    def post(self, request, *args, **kwargs):
        form = JobAppForm(request.POST)
        if form.is_valid():
            form.instance.applicant = Profile.objects.get(user=self.request.user)
            form.instance.job = self.get_object()
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


class JobAddView(LoginRequiredMixin, DetailView):
    model = Commission
    template_name = 'job-add.html'
    redirect_field_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = JobForm()
        context['all_objects'] = Commission.objects.all()
        return context

    def get_success_url(self):
        return reverse('commissions:detail', kwargs={'pk': self.object.pk})
    
    def post(self, request, *args, **kwargs):
        form = JobForm(request.POST)
        if form.is_valid():
            form.instance.commission = self.get_object()
            form.save()
            return redirect('commissions:detail', pk=self.get_object().pk)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
    
    


class ComCreateView(LoginRequiredMixin, CreateView):
    model = Commission
    template_name = 'commission-add.html'
    redirect_field_name = 'login.html'
    fields = ['title', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super(ComCreateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('commissions:job_add', kwargs={'pk': self.object.pk})


class ComUpdateView(LoginRequiredMixin, UpdateView):
    model = Commission
    fields = ['title', 'description', 'status']
    template_name = 'commission-update.html'
    redirect_field_name = 'login.html'
    