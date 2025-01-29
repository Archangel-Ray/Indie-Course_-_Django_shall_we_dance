# from django.contrib import admin
from django.urls import path

from .views import FeedBackView, UpdateFeedbackView, DoneView, ListFeedBack, DetailFeedBack

urlpatterns = [
    # подтверждение о получении формы
    path('done', DoneView.as_view(), name="подтверждение"),
    # запуск представления с формой
    path('', FeedBackView.as_view(), name="добавление отзыва"),
    # запуск представления с указанной записью из базы
    path('<int:id_feedback>', UpdateFeedbackView.as_view(), name="форма отзыва"),
    # отображение всех записей
    path('list', ListFeedBack.as_view(), name="список"),
    # отображение конкретной записи
    path('detail/<int:pk>', DetailFeedBack.as_view(), name="отзыв"),
]
