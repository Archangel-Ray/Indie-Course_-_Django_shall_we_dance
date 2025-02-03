from django import forms


class GalleryUploadForm(forms.Form):
    image = forms.FileField(label="Что загружаем")  # поле загрузки - открывает окно проводника для выбора файла
