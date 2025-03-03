from django.urls import path
from .views import ComListView, ComDetailView

urlpatterns = [
    path('list', ComListView.as_view(), name='list'),
    path('detail/<int:pk>', ComDetailView.as_view(), name='detail'),
]

app_name = 'commissions'