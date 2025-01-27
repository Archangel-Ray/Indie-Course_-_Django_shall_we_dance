from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .forms import FeedbackForm
from .models import FeedBack


class FeedBackView(View):
    def get(self, request):
        window = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'about_the_window': window})

    def post(self, request):
        window = FeedbackForm(request.POST)
        if window.is_valid():
            window.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'about_the_window': window})


class ListFeedBack(ListView):
    """
    отображение списка всех отзывов
    """
    template_name = "feedback/list_feedback.html"
    model = FeedBack
    context_object_name = "all"

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.order_by("-rating")
        return filter_qs


class DetailFeedBack(TemplateView):
    """
    вывод отдельного отзыва
    """
    template_name = "feedback/detail_feedback.html"

    def get_context_data(self, **kwargs):
        """
        передача конкретной записи из базы в контекст
        """
        context = super().get_context_data(**kwargs)
        note = FeedBack.objects.get(id=kwargs["id_feedback"])
        context["specific_entry"] = note
        return context


class UpdateFeedbackView(View):
    def get(self, request, id_feedback):
        feed = FeedBack.objects.get(id=id_feedback)
        window = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'about_the_window': window})

    def post(self, request, id_feedback):
        feed = FeedBack.objects.get(id=id_feedback)
        window = FeedbackForm(request.POST, instance=feed)
        if window.is_valid():
            window.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'about_the_window': window})


class DoneView(TemplateView):
    """
    класс простого отображения шаблонов
    """
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        """
        добавление контекста в шаблон
        """
        context = super().get_context_data(**kwargs)
        context["text"] = "Дополнительный текст"
        context["date"] = "23.04.2022"
        return context


"""
дальше идут старые функции. оставил на память.
"""


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
    # получение записи из базы данных
    feed = FeedBack.objects.get(id=id_feedback)
    if request.method == 'POST':  # проверка, на то что это -- редактирование
        # форма с привязкой к записи из базы и новое наполнение
        window = FeedbackForm(request.POST, instance=feed)
        if window.is_valid():  # проверка на соответствие настройкам
            window.save()  # сохранение в базу
        return HttpResponseRedirect(f'/{id_feedback}')  # перенаправление на изменённую запись
    else:
        window = FeedbackForm(instance=feed)  # если был запрос без изменений
    # отправляет в шаблон форму с привязкой к записи
    return render(request, 'feedback/feedback.html', context={'about_the_window': window})


def done(request):
    # шаблон с сообщением о подтверждении
    return render(request, 'feedback/done.html')
