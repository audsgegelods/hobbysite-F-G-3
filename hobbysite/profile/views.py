from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Profile
from .forms import ProfileForm, UserCreateForm


class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'profile/profile-add.html'
    form_class = UserCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreateForm()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreateView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile/profile.html'
    form_class = ProfileForm

    def form_valid(self, form):
        if self.request.user in Profile.objects.all():
            form.instance.user = self.request.user
            form.instance.email_address.widget.attrs['readonly'] = True
            return super(ProfileUpdateView, self).form_valid(form)
