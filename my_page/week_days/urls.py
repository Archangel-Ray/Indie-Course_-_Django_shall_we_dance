from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'YYYY')

urlpatterns = [
    path('', views.main),
    path('<YYYY:what_year>/', views.get_years_converter),
    path('<int:day_of_the_week>/', views.what_is_day_of_week_number),
    path('<day_of_the_week>/', views.what_day_of_the_week, name="день недели"),
]
