from django.urls import path
from .views import ComListView, ComDetailView, ComCreateView, ComUpdateView

urlpatterns = [
    path('list', ComListView.as_view(), name='list'),
    path('detail/<int:pk>', ComDetailView.as_view(), name='detail'),
    path('add', ComCreateView.as_view(), name='add'),
    path('edit/<int:pk>', ComUpdateView.as_view(), name='edit'),
    
]

app_name = 'commissions'
