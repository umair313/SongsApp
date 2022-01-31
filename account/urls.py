from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegiserUserView,HomeView, ApplicationHomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegiserUserView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('userhome/', ApplicationHomeView.as_view(), name='userhome'),
    path('logout', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),

    path('password-reset/' ,
        auth_views.PasswordResetView.as_view(template_name='account/password_reset_email.html'),
        name='password_reset'),
    
    path('password-reset-done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('password-reset-complete',
        auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
        name='password_reset_complete')
]
