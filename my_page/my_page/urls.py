"""my_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views as views_h
from actors import views as views_a

urlpatterns = [
    path('', views_h.main),
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('week_days/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls')),
    path('actors/', views_a.main),
    path('guinn/', views_a.get_guinness_world_records),
    path('people/', views_a.peoples),
    path('beautiful_table/', views_a.style),
]
