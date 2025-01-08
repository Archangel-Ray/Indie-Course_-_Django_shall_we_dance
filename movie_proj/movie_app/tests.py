from django.test import TestCase
from django.urls import reverse

from .models import Movie


class MovieModelTestCase(TestCase):

    @staticmethod
    def print_info(message):
        # служебный метод для вывода сообщения и подсчёта количества записей на данный момент
        count = Movie.objects.count()
        print(f"{message}: #all_movies={count}")

    def setUp(self):
        print('-' * 20)  # визуальное разделение
        self.print_info('Start setUp')  # сообщение о создании тестовой базы данных
        self.movie = Movie.objects.create(name='Test Movie', rating=80, year=2022)  # добавление записи
        Movie.objects.create(name='Test Matrix', rating=90, year=2021)  # добавление записи
        Movie.objects.create(name='Mask', rating=50, year=1995)  # добавление записи
        self.print_info('Finish setUp')  # сообщение о завершении создания тестовой базы данных

    def test_movie_creation(self):
        # Проверка создания объекта Movie
        self.print_info('Start test_movie_creation')  # сообщение о начале теста
        self.assertEqual(self.movie.name, 'Test Movie')  # проверка поля
        self.assertEqual(self.movie.rating, 80)  # проверка поля
        self.assertEqual(self.movie.year, 2022)  # проверка поля
        self.assertEqual(self.movie.budget, 1000000)  # проверка поля
        self.assertEqual(self.movie.slug, 'test-movie')  # проверка поля
        self.print_info('Finish test_movie_creation')  # сообщение о завершении теста

    def test_movie_get_all_records(self):
        # Проверка получения всех записей из бд
        self.print_info('Start test_movie_get_all_records')
        movies = Movie.objects.all()
        self.assertEqual(len(movies), 3)
        self.print_info('Finish test_movie_get_all_records')

    def test_movie_get_record(self):
        # Проверка получения записи из бд
        self.print_info('Start test_movie_get_record')
        mask = Movie.objects.get(name='Mask')
        self.assertEqual(mask.year, 1995)
        self.print_info('Finish test_movie_get_record')

    def test_movie_get_url(self):
        # Проверка метода get_url()
        self.print_info('Start test_movie_get_url')
        url = self.movie.get_url()
        expected_url = reverse('отображение фильма', args=['test-movie'])
        self.assertEqual(url, expected_url)
        self.print_info('Finish test_movie_get_url')

    def test_movie_str(self):
        # Проверка метода __str__()
        self.print_info('Start test_movie_str')
        expected_str = 'Test Movie - 80%'
        self.assertEqual(str(self.movie), expected_str)
        self.print_info('Finish test_movie_str')

    def test_movie_save_slug(self):
        # Проверка сохранения корректного slug при сохранении объекта
        self.print_info('Start test_movie_creation')
        self.assertEqual(self.movie.slug, 'test-movie')
        self.print_info('Finish test_movie_save_slug')

    def test_movie_budget_default_value(self):
        # Проверка значения по умолчанию для budget
        self.print_info('Start test_movie_budget_default_value')
        movie = Movie.objects.create(name='Default Budget Movie', rating=75)
        self.assertEqual(movie.budget, 1000000)
        self.print_info('Finish test_movie_budget_default_value')

    def test_record_deletion(self):
        # Проверка на удаление записи
        self.print_info('начало проверки удаления записи')
        self.movie.delete()
        self.assertEqual(Movie.objects.count(), 2)
        self.print_info('запись успешно удалена')

    def test_changing_data_in_a_record(self):
        # Проверка изменений данных в записи
        self.print_info('начало проверки изменения данных в записи')
        self.movie.rating = 82
        self.movie.save()
        self.assertEqual(Movie.objects.get(id=1).rating, 82)
        self.print_info('запись была успешно изменена')

    def test_the_slug_field_in_cyrillic(self):
        # Проверка слаг-поля если название будет заполнено на кириллице
        self.print_info('начало проверки слаг-поля на кириллице')
        self.cyrillic = Movie.objects.create(name='Название Фильма', rating=1)  # добавление записи
        self.assertEqual(self.cyrillic.slug, 'nazvanie-filma')
        self.print_info('слаг-поле на кириллице успешно конвертировано')


# запуск тестов в терминале
# python manage.py test
