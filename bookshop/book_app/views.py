from django.shortcuts import render
from django.urls import reverse

from book_app.models import Book


def displaying_a_list_of_all_books(requests):
    return render(requests, 'book_app/all_books.html', {
        'books': Book.objects.all()
    })


def get_a_specific_book(requests, id_book):
    return render(requests, 'book_app/book.html', {
        'book': Book.objects.get(id=id_book),
        'link': reverse('specific book', args=[id_book]),
    })
