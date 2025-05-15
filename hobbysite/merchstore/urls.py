from django.urls import path
from .views import IndividProductView, AllItemsView, ProductCreateView, ProductUpdateView, CartView, TransactionView

urlpatterns = [
    path(
        'items',
        AllItemsView.as_view(),
        name="items"
        ),
    path(
        'item/<int:pk>',
        IndividProductView.as_view(),
        name="itempage"
        ),
    path(
        'item/add',
        ProductCreateView.as_view(),
        name="itemcreate"
        ),
    path(
        'item/<int:pk>/edit',
        ProductUpdateView.as_view(),
        name="itemupdate"
        ),
    path(
        'cart',
        CartView.as_view(),
        name="cart"
        ),
    path(
        'transactions',
        TransactionView.as_view(),
        name="sellertransactions"
        ),
]

app_name = "merchstore"
