from django.urls import path, converters
from . import views

urlpatterns = [
    path('', views.index, name='главная страница гороскопа'),
    path('elements/', views.call_elements, name="стихии зодика"),
    path('elements/<element>', views.index, name="знаки стихии"),
    path('<int:sign>/', views.get_info_about_sign_by_number),
    path('<sign>/', views.get_info_about_sign, name="знак зодиака"),
    path('<int:month>/<int:date>', views.get_sign),
]
