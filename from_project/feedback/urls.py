# from django.contrib import admin
from django.urls import path

from .views import FeedBackView, UpdateFeedbackView, DoneView

urlpatterns = [
    path('done', DoneView.as_view()),  # подтверждение о получении формы
    path('', FeedBackView.as_view()),  # запуск представления с формой
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),  # запуск представления с указанной записью из базы
]
