""".../movie_proj/movie_app/views.py"""
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from django.shortcuts import render, get_object_or_404

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
    # for movie in movies:
    #     movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies,
        'ag': aggregate_movies,
        'total': movies.count(),
    })


def book_display(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/movie.html', {
        'movie': movie
    })


def directors_display(request):
    return render(request, 'movie_app/directors.html', {
        'directors': Director.objects.all()
    })


def director_display(request, id_director):
    return render(request, 'movie_app/director.html', {
        'director': Director.objects.get(id=id_director)
    })


def actors_display(request):
    return render(request, 'movie_app/actors.html', {
        'actors': Actor.objects.all()
    })


def actor_display(request, id_actor):
    return render(request, 'movie_app/actor.html', {
        'actor': Actor.objects.get(id=id_actor)
    })
