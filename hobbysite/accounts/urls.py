from django.urls import path
from django.contrib.auth.views import (LoginView,
                                       LogoutView,
                                       PasswordChangeView,
                                       PasswordChangeDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView)

app_name = 'profile'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
