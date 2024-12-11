""".../проект/приложение>admin.py"""
from django.contrib import admin, messages
from django.db.models import QuerySet

from .models import Movie, Director, Actor, DressingRoom

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Рейтинг'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('40-69', 'Средний'),
            ('70-84', 'Высокий'),
            ('85<=', 'Максимальный')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40-69':
            return queryset.filter(rating__gte=40).filter(rating__lt=70)
        if self.value() == '70-84':
            return queryset.filter(rating__gte=70).filter(rating__lt=85)
        if self.value() == '85<=':
            return queryset.filter(rating__gte=85)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'director', 'rating', 'genres', 'budget', 'rating_status']  # отображаемые поля
    list_editable = ['rating', 'genres', 'director']  # редактируемые поля
    ordering = ['-rating', 'name']  # сортировка
    list_per_page = 10  # колличество строк на странице
    actions = ['set_genre_action', 'set_genre_western', 'set_genre_comedy']  # строка "действий"
    search_fields = ['name__startswith', 'rating']  # строка поиска со списком полей в которых идёт поиск
    list_filter = [RatingFilter, 'genres']  # панель фильтрации
    # fields = ['name', 'rating', 'genres', 'budget']  # поля отображаемые на странице элементов
    # exclude = ['genres']  # поля исключаемые из отображения на странице элементов
    readonly_fields = ['budget']  # поля только для чтения на странице элементов
    prepopulated_fields = {'slug': ('name',)}  # автоматическое заполнение поля URL-имени элемента
    # filter_horizontal = ['actors']  # горизонтальное отображение окон таблиц многие ко многим на странице элементов
    filter_vertical = ['actors']  # вертикальное отображение окон таблиц многие ко многим на странице элементов

    @admin.display(ordering='rating', description='Рекомендация')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Ничего интересного'
        if movie.rating < 70:
            return 'более-менее'
        if movie.rating < 85:
            return 'можно посмотреть'
        return 'к просмотру'

    @admin.action(description="установить жанр - боевик")
    def set_genre_action(self, request, queryset: QuerySet):
        queryset.update(genres=Movie.ACTION)

    @admin.action(description="установить жанр - вестерн")
    def set_genre_western(self, request, queryset: QuerySet):
        count_updated = queryset.update(genres=Movie.WESTERN)
        self.message_user(request, f'изменено {count_updated} записей', level=messages.ERROR)

    @admin.action(description="установить жанр - комедия")
    def set_genre_comedy(self, request, queryset: QuerySet):
        count_updated = queryset.update(genres=Movie.COMEDY)
        self.message_user(request, f'изменено {count_updated} записей', level=messages.WARNING)
