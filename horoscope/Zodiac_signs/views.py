from django.http import HttpResponse


def main(request):
    return HttpResponse("Главная страница")
