# from django.contrib import admin
from django.urls import path

from .views import index, done

urlpatterns = [
    path('done', done),  # подтверждение о получении формы
    path('', index),  # запуск представления с формой
]
