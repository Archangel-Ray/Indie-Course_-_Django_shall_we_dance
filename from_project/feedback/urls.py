# from django.contrib import admin
from django.urls import path

from .views import index, done, update_feedback, FeedBackView, UpdateFeedbackView

urlpatterns = [
    path('done', done),  # подтверждение о получении формы
    path('', FeedBackView.as_view()),  # запуск представления с формой
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),  # запуск представления с указанной записью из базы
]
