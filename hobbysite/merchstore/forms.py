from django import forms
from .models import Product, Transaction


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','producttype','description','price','stock',]

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'