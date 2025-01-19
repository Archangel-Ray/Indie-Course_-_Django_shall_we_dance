from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm


def index(request):
    if request.method == 'POST':
        # создание формы и наполнение её полученными данными
        filled_window = FeedbackForm(request.POST)
        # проверка данных формы
        if filled_window.is_valid():
            print(filled_window.cleaned_data)
            # перенаправление на сообщение о подтверждении
            return HttpResponseRedirect('/done')
    # создание формы
    window = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'about_the_window': window})


def done(request):
    # шаблон с сообщением о подтверждении
    return render(request, 'feedback/done.html')
