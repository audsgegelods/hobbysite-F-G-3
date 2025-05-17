from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Profile
from .forms import ProfileForm


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile/profile.html'
    form_class = ProfileForm

    def form_valid(self, form):
        if self.request.user in Profile.objects.all():
            form.instance.user = self.request.user
            form.instance.email_address.widget.attrs['readonly'] = True
            return super(ProfileUpdateView, self).form_valid(form)
