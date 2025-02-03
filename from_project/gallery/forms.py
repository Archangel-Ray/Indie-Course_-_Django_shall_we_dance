from django import forms


class GalleryUploadForm(forms.Form):
    image = forms.FileField()  # поле загрузки - открывает окно проводника для выбора файла
