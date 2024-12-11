from django.urls import path

from geometry import views

urlpatterns = [
    path('', views.main),
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name="площадь прямоугольника"),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_redirect),
    path('square/<int:width>', views.get_square_area, name="площадь квадрата"),
    path('get_square_area/<int:width>', views.get_square_area_redirect),
    path('circle/<int:radius>', views.get_circle_area, name="площадь круга"),
    path('get_circle_area/<int:radius>', views.get_circle_area_redirect),
]
