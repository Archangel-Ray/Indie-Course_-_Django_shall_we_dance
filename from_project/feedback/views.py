from django.shortcuts import render


def index(request):
    print('ГЕТ запрос: ', request.GET)
    print('ПОСТ запрос: ', request.POST)
    return render(request, 'feedback/feedback.html')  # шаблон с формой
