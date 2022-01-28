
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home, register_user

urlpatterns = [
    path('', home, name='home'),

    path('register/', register_user, name='register'),

]