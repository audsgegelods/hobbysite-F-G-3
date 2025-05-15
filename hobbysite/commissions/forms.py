from django import forms
from .models import Commission, Job, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']


class JobAppForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        exclude = ['job', 'applicant', 'status']
        