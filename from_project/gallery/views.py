from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import GalleryUploadForm


def storage_file(file):
    """функция записывающая файл в директорию на сервере"""
    with open(f'gallery_tmp/{file.name}', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


class GalleryView(View):
    def get(self, request):
        form = GalleryUploadForm()  # экземпляр формы
        return render(request, 'gallery/load_file.html', {"form": form})

    def post(self, request):
        # экземпляр формы заполняется из запроса данными
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            storage_file(request.FILES['image'])
            return HttpResponseRedirect("load_image")
        return render(request, 'gallery/load_file.html', {"form": form})
