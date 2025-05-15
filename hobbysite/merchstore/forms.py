from django import forms
from .models import Product, Transaction


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['owner']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']