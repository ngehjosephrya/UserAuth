from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('signup/',SignupView.as_view() , name='signup'),
    path('home/',homePage.as_view() , name='home'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    
]