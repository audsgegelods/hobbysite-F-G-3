from django.urls import path
from .views import IndividProductView, AllItemsView

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
]

app_name = "merchstore"
