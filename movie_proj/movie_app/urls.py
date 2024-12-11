"""movie_proj/movie_proj/urls.py"""
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.book_display, name="отображение фильма"),
    path('directors/', views.directors_display, name="все режисёры"),
    path('directors/<id_director>', views.director_display, name="режисёр"),
    path('actors/', views.actors_display, name="актёры"),
    path('actors/<id_actor>', views.actor_display, name="актёр"),
]
