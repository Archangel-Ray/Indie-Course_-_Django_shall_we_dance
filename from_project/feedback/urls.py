# from django.contrib import admin
from django.urls import path

from .views import FeedBackView, UpdateFeedbackView, DoneView, ListFeedBack, DetailFeedBack

urlpatterns = [
    path('done', DoneView.as_view()),  # подтверждение о получении формы
    path('', FeedBackView.as_view()),  # запуск представления с формой
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),  # запуск представления с указанной записью из базы
    path('list', ListFeedBack.as_view()),  # отображение всех записей
    path('detail/<int:id_feedback>', DetailFeedBack.as_view()),  # отображение конкретной записи
]
