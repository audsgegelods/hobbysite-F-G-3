from django.urls import path
from .views import ProfileUpdateView

app_name = 'user_management'
urlpatterns = [
    path('profile/<str:name>', ProfileUpdateView.as_view(), name='profile'),
]
