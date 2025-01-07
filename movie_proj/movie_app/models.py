""".../movie_proj/movie_app/models.py"""
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    # отображение элемента
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # реконструкция url-адреса отдельного элемента модели
    def get_url(self):
        return reverse('режисёр', args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = [
        (MALE, "Мужчина"),
        (FEMALE, "Женщина"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    # отображение элемента
    def __str__(self):
        if self.gender == self.MALE:
            return f"Актёр {self.first_name} {self.last_name}"
        else:
            return f"Актрисса {self.first_name} {self.last_name}"


class Movie(models.Model):
    COMEDY = 'COM'
    ACTION = 'ACT'
    THRILLER = 'THR'
    WESTERN = 'WES'
    CHOICES_OF_GENRES = [
        (COMEDY, "Комедия"),
        (ACTION, "Боевик"),
        (THRILLER, "Триллер"),
        (WESTERN, "Вестерн"),
    ]

    # поле строкового типа, длина до 40 символов
    name = models.CharField(max_length=40)

    # поле числового типа с валидацией
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    # поле числового типа, может быть пустым
    year = models.IntegerField(null=True, blank=True)

    # поле числового типа, значение по умолчанию и проверка
    budget = models.IntegerField(default=1_000_000, validators=[MinValueValidator(1)])

    # поле со списком
    genres = models.CharField(
        max_length=3,
        choices=CHOICES_OF_GENRES,  # выпадающий список
        default=COMEDY
    )

    # поле для url-адреса
    slug = models.SlugField(default="", null=False, db_index=True)

    # связь с другой таблицей один ко многим
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')

    # связь с другой таблицей многие ко многим
    actors = models.ManyToManyField(Actor, related_name='movies')

    # сохранение с конвертацией автоматического поля url-адреса
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = self.converter(slugify(self.name, allow_unicode=True))
    #     super().save(*args, **kwargs)

    # конвертер латиницы в кириллицу
    @staticmethod
    def converter(text):
        cyrillic_to_latin = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
                             'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
                             'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
                             'ш': 'sh', 'щ': 'sh', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        new_text = ""
        for x in text:
            if x in cyrillic_to_latin:
                new_text += cyrillic_to_latin[x]
            else:
                new_text += x
        return new_text

    # реконструкция url-адреса отдельного элемента модели
    def get_url(self):
        return reverse('отображение фильма', args=[self.slug])

    # отображение элемента
    def __str__(self):
        return f"{self.name} - {self.rating}%"

# команды терминала на память
# python manage.py shell_plus --print-sql
# from movie_app.models import Movie, Director, Actor
