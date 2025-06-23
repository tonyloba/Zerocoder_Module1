from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'), # custom logout works
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'), # dont work as wants post
    path('', views.home, name='home'),
]