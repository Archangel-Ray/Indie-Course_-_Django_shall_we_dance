from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView

from .forms import GalleryUploadForm
from .models import Gallery


def storage_file(file):
    """
    оставил на память (и папку в проекте которая тут создавалась).
    функция записывающая файл в директорию на сервере
    """
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
            new_image = Gallery(image=form.cleaned_data["image"])
            new_image.save()
            return HttpResponseRedirect("load_image")
        return render(request, 'gallery/load_file.html', {"form": form})


class CreateGalleryView(CreateView):
    model = Gallery
    form_class = GalleryUploadForm
    template_name = 'gallery/load_file.html'
    success_url = "load_image"
