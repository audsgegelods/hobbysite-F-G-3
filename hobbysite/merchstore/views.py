from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ProductType, Product

# Create your views here.


class IndividProductView(DetailView):
    model = Product
    template_name = 'merchstore/itempage.html'


class AllItemsView(ListView):
    model = ProductType
    template_name = 'merchstore/items.html'
