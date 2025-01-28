"""movie_proj/movie_proj/urls.py"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.displaying_movie, name="отображение фильма"),
    path('directors/', views.DirectorsDisplay.as_view(), name="все режиссёры"),
    path('directors/<id_director>', views.director_display, name="режиссёр"),
    path('actors/', views.actors_display, name="актёры"),
    path('actors/<id_actor>', views.actor_display, name="актёр"),
]
