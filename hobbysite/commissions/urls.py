from django.urls import path
from .views import ComListView, ComDetailView, ComCreateView, ComUpdateView, JobDetailView, JobAddView

urlpatterns = [
    path('list', ComListView.as_view(), name='list'),
    path('detail/<int:pk>', ComDetailView.as_view(), name='detail'),
    path('add', ComCreateView.as_view(), name='add'),
    path('<int:pk>/edit', ComUpdateView.as_view(), name='edit'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/add-job', JobAddView.as_view(), name='job_add'),
]

app_name = 'commissions'
