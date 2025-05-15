from django.urls import path
from .views import ProfileUpdateView

urlpatterns = [
    path('/profile/<str:name>', ProfileUpdateView.as_view(), name='profile'),
]
