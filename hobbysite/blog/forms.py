# app/forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	#entry = forms.CharField(label="Comment", max_length=255)
	class Meta: 
		model = Comment
		#fields = '__all__'
		fields = ['entry']
		
