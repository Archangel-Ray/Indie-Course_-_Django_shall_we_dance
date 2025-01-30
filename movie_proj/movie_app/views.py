""".../movie_proj/movie_app/views.py"""
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Movie, Director, Actor


def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_first=True), '-rating')
    movies = Movie.objects.annotate(
        field_bool=Value(True),
        str_field=Value("какое-то слово"),
        int_field=Value(123),
        f_field=F('year') + 100,
    ).annotate(math=F('budget') * F('rating'), )
    aggregate_movies = movies.aggregate(Sum('budget'), Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    # for movie in movies: # перебор делался для заполнения поля слаг там где оно не заполнено
    #     movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'ag': aggregate_movies,
        'total': movies.count(),
    })


def displaying_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/movie.html', {
        'movie': movie
    })


class DirectorsDisplay(ListView):
    template_name = "movie_app/directors.html"
    model = Director
    context_object_name = "directors"


class DirectorDisplay(DetailView):
    template_name = "movie_app/director.html"
    model = Director
    context_object_name = "director"


class ActorsDisplay(ListView):
    template_name = "movie_app/actors.html"
    model = Actor
    context_object_name = "actors"


class ActorDisplay(DetailView):
    template_name = "movie_app/actor.html"
    model = Actor
    context_object_name = "actor"
