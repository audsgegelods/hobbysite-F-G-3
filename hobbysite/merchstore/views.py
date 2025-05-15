from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Product, ProductType, Transaction
from .forms import ProductCreateForm, ProductUpdateForm, TransactionForm

# Create your views here.


class IndividProductView(DetailView):
    model = Product
    template_name = 'merchstore/itempage.html'

    def get_context_data(self, **kwargs):
        context = super(IndividProductView, self).get_context_data(**kwargs)
        context['all_objects'] = Product.objects.all()
        context['form'] = TransactionForm()
        context['cart'] = reverse_lazy('merchstore:cart')
        return context

    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        product = Product.objects.get(pk=self.kwargs['pk'])
        if form.is_valid():
            form.instance.product = product
            form.instance.status =  'On cart'
            form.instance.amount = request.POST.get('amount')
            product.stock -= int(form.instance.amount)
            if product.stock < 1:
                product.status = 'Out of Stock'
            if not (request.user.is_authenticated):
                return redirect('login')
            form.instance.buyer = self.request.user
            product.save()
            form.save()
            return redirect('merchstore:cart')
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
        if form.instance.stock < 1:
            form.instance.status = 'Out of Stock'
        else:
            form.instance.status = 'Available'
        return super(ProductCreateView, self).form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'merchstore/productform.html'
    redirect_field_name = '/accounts/login'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        if form.instance.stock < 1:
            form.instance.status = 'Out of Stock'
        else:
            form.instance.status = 'Available'
        return super(ProductUpdateView, self).form_valid(form)

class CartView(ListView):
    model = Transaction
    template_name = 'merchstore/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['owner_order'] = Transaction.objects.all().order_by(product__owner).values
        return context

class TransactionView(ListView):
    model = Transaction
    template_name = 'merchstore/transactions.html'

