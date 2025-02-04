from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # форма загрузки файла
    path('load_image', views.GalleryView.as_view()),
    path('create_load_image', views.CreateGalleryView.as_view()),
    path('list_image', views.ListGallery.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
