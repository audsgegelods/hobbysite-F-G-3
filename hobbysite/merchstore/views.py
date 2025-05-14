from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductType, Transaction
from .forms import ProductCreateForm, ProductUpdateForm, TransactionForm

# Create your views here.


class IndividProductView(DetailView):
    model = Product
    template_name = 'merchstore/itempage.html'

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.instance.buyer = self.request.user
            form.instance.product = self.get_object()
            form.instance.status =  'CART'
            form.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class AllItemsView(ListView):
    model = ProductType
    template_name = 'merchstore/items.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'merchstore/productform.html'
    redirect_field_name = '/accounts/login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProductCreateView, self).form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'merchstore/productform.html'
    redirect_field_name = '/accounts/login'

class CartView(ListView):
    model = Transaction
    template_name = 'merchstore/cart.html'

class TransactionView(ListView):
    model = Transaction
    template_name = 'merchstore/transactions.html'

