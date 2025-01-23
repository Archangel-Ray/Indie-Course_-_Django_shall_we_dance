# from django.contrib import admin
from django.urls import path

from .views import index, done, update_feedback

urlpatterns = [
    path('done', done),  # подтверждение о получении формы
    path('', index),  # запуск представления с формой
    path('<int:id_feedback>', update_feedback),  # запуск представления с указанной записью из базы
]
