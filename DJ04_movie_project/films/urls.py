from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_movie, name='add_movie'),
    path('', views.movie_list, name='movie_list'),
]