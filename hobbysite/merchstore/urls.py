from django.urls import path
from .views import IndividProductView, AllItemsView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path(
        'merchstore/items',
        AllItemsView.as_view(),
        name="items"
        ),
    path(
        'merchstore/item/<int:pk>',
        IndividProductView.as_view(),
        name="itempage"
        ),
    path(
        'merchstore/item/add',
        ProductCreateView.as_view(),
        name="itemcreate"
        ),
    path(
        'merchstore/item/edit',
        ProductUpdateView.as_view(),
        name="itemupdate"
        ),
]

app_name = "merchstore"
