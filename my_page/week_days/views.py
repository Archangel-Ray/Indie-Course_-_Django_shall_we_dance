from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

week = {
    'monday': "Понедельник день бездельник",
    'tuesday': "Вторник - повторник",
    'wednesday': "Среда - тамада",
    'thursday': "Четверг - я заботы все отверг",
    'friday': "Пятница - пьяница",
    'saturday': "Суббота - безработа",
    'sunday': "Воскресенье - день веселья"
}


def main(request):
    return render(request, "week_days/greeting.html")


def what_day_of_the_week(request, day_of_the_week):
    if day_of_the_week.lower() in week:
        return HttpResponse(week[day_of_the_week.lower()])
    else:
        return HttpResponse(f"Появился новый день недели - {day_of_the_week}?")


def what_is_day_of_week_number(request, day_of_the_week):
    if 0 < day_of_the_week < 8:
        link = reverse("день недели", args=[list(week)[day_of_the_week - 1]])
        return redirect(link)
    else:
        return HttpResponseNotFound(f"Неверный номер дня недели - {day_of_the_week}")


def get_years_converter(request, what_year):
    return HttpResponse(f"{what_year} год")
