"""movie_proj/movie_proj/urls.py"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.displaying_movie, name="отображение фильма"),
    path('directors/', views.DirectorsDisplay.as_view(), name="все режиссёры"),
    path('directors/<id_director>', views.director_display, name="режиссёр"),
    path('actors/', views.ActorsDisplay.as_view(), name="актёры"),
    path('actors/<int:pk>', views.ActorDisplay.as_view(), name="актёр"),
]
