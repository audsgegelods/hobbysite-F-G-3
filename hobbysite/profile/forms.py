from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class UserCreateForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
