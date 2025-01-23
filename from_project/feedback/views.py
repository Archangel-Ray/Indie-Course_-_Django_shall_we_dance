from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Feedback


def index(request):
    if request.method == 'POST':
        # создание формы и наполнение её полученными данными
        window = FeedbackForm(request.POST)
        # проверка данных формы
        if window.is_valid():
            print(window.cleaned_data)
            # feed = Feedback(  # экземпляр модели с данными из формы
            #     name=window.cleaned_data['name'],
            #     surname=window.cleaned_data['surname'],
            #     feedback=window.cleaned_data['feedback'],
            #     rating=window.cleaned_data['rating'],
            # )
            window.save()  # сохранение в базу

            # перенаправление на сообщение о подтверждении
            return HttpResponseRedirect('/done')
    else:
        # создание формы
        window = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'about_the_window': window})


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    window = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'about_the_window': window})


def done(request):
    # шаблон с сообщением о подтверждении
    return render(request, 'feedback/done.html')
