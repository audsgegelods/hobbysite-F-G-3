from django import forms
from .models import Commission, JobApplication


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'


class JobAppForm(forms.ModelForm): #TODO
    class Meta:
        model = JobApplication
        fields = ['job', 'applicant']
        