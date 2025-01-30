"""movie_proj/movie_proj/urls.py"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug>', views.DisplayingMovie.as_view(), name="отображение фильма"),
    path('directors/', views.DirectorsDisplay.as_view(), name="все режиссёры"),
    path('directors/<int:pk>', views.DirectorDisplay.as_view(), name="режиссёр"),
    path('actors/', views.ActorsDisplay.as_view(), name="актёры"),
    path('actors/<int:pk>', views.ActorDisplay.as_view(), name="актёр"),
]
