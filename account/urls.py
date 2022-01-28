from django.urls import path

from .views import home, register_user

urlpatterns = [
    path('', home, name='home'),

    path('register/', register_user, name='register'),

]
