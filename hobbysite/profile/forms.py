from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'user': ('Profile User'),
            'display_name': ('Profile Name'),
            'email_address': ('Profile Email')
        }

