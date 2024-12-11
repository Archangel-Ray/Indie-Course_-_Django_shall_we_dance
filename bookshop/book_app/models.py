from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=70)  # текстовое поле не длиннее 70 символов
    rating = models.IntegerField()  # числовое поле
    is_best_selling = models.BooleanField()  # логическое поле
    author = models.CharField(max_length=100, null=True)  # текстовое поле, по умолчанию пустое

    def __str__(self):
        return f"{self.title}, {self.author}, {self.is_best_selling}, {self.rating}%"


# python manage.py shell_plus --print-sql
# from book_app.models import Book
