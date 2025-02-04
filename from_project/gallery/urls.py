from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # форма загрузки файла
    path('load_image', views.GalleryView.as_view(), name="загрузка файла в ручную"),
    path('create_load_image', views.CreateGalleryView.as_view(), name="загрузка файла автоматически"),
    path('list_image', views.ListGallery.as_view(), name="вывод всех файлов"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
