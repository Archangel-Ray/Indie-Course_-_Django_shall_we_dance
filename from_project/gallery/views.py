from django.shortcuts import render
from django.views import View


def storage_file(file):  # функция записывающая файл в директорию на сервере
    with open('gallery_tmp/new_image.jpg', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery/load_file.html')

    def post(self, request):
        pass
