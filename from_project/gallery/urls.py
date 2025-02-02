from django.urls import path

from . import views

urlpatterns = [
    # форма загрузки файла
    path('load_image', views.GalleryView.as_view()),
]
