from django.urls import path
from .views import ProfileUpdateView

app_name = 'profile'
urlpatterns = [
    path('<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
]
