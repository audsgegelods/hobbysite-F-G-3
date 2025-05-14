from django.urls import path
from .views import ComListView, ComDetailView, ComCreateView, ComUpdateView, JobDetailView

urlpatterns = [
    path('list', ComListView.as_view(), name='list'),
    path('detail/<int:pk>', ComDetailView.as_view(), name='detail'),
    path('add', ComCreateView.as_view(), name='add'),
    path('edit/<int:pk>', ComUpdateView.as_view(), name='edit'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job_detail'),
]

app_name = 'commissions'
