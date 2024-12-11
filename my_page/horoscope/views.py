from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

elements = {
    'Воздух': ['gemini', 'libra', 'aquarius'],
    'Вода': ['cancer', 'scorpio', 'pisces'],
    'Земля': ['taurus', 'virgo', 'capricorn'],
    'Огонь': ['aries', 'leo', 'sagittarius']
}
sign_dict = {
    'aries': ["Овен - первый знак зодиака, планета Марс", 21, "марта", 20, "апреля"],
    'taurus': ["Телец - второй знак зодиака, планета Венера", 21, "апреля", 21, "мая"],
    'gemini': ["Близнецы - третий знак зодиака, планета Меркурий", 22, "мая", 21, "июня"],
    'cancer': ["Рак - четвёртый знак зодиака, Луна", 22, "июня", 22, "июля"],
    'leo': ["Лев - пятый знак зодиака, солнце", 23, "июля", 21, "августа"],
    'virgo': ["Дева - шестой знак зодиака, планета Меркурий", 22, "августа", 23, "сентября"],
    'libra': ["Весы - седьмой знак зодиака, планета Венера", 24, "сентября", 23, "октября"],
    'scorpio': ["Скорпион - восьмой знак зодиака, планета Марс", 24, "октября", 22, "ноября"],
    'sagittarius': ["Стрелец - девятый знак зодиака, планета Юпитер", 23, "ноября", 22, "декабря"],
    'capricorn': ["Козерог - десятый знак зодиака, планета Сатурн", 23, "декабря", 20, "января"],
    'aquarius': ["Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн", 21, "января", 19, "февраля"],
    'pisces': ["Рыбы - двенадцатый знак зодиака, планета Юпитер", 20, "февраля", 20, "марта"]
}

months = [("", 0), ("января", 31), ("февраля", 29), ("марта", 31), ("апреля", 30), ("мая", 31), ("июня", 30),
          ("июля", 31), ("августа", 31), ("сентября", 30), ("октября", 31), ("ноября", 30), ("декабря", 31)]


def index(request, element=None):
    signs_zodiac = None
    if element:
        signs_zodiac = elements[element]
    else:
        signs_zodiac = list(sign_dict)
    context = {
        'signs_zodiac': signs_zodiac,
        # 'стихии': reverse('стихии зодика'),
    }
    return render(request, 'horoscope/index.html', context=context)

    # menu = ""
    # for sing in elements[element] if element else list(sign_dict):
    #     link = reverse("знак зодиака", args=[sing])
    #     menu += f"<h2><li><a href='{link}'>{sing.title()}</li></h2>"
    # menu = f"<ol>{menu}</ol>"
    # menu += f"<ul><a href={reverse('стихии зодика')}>Cтихии зодика</a></ul>"
    # return HttpResponse(menu)


def call_elements(request):
    menu = "<p><h3>без шаблона</h3></p><p>представление сформировано во views</p>"
    for el in list(elements):
        link = reverse("знаки стихии", args=[el])
        menu += f"<li><a href='{link}'>{el}</li>"
    return HttpResponse(menu)


def get_info_about_sign(request, sign):
    sign_out = sign_dict.get(sign, None)
    if sign_out:
        data = {
            'description_sign': f"{sign_out[0]} (с {sign_out[1]} {sign_out[2]} по {sign_out[3]} {sign_out[4]}).",
            'title': sign_out[0].split()[0],
            'sign_data': sign_out[0],
            'start_date': sign_out[1],
            'start_month': sign_out[2],
            'ending_date': sign_out[3],
            'ending_month': sign_out[4],
            'signs_zodiac': sign_dict,
            'my_dict': elements,
        }
        return render(request, 'horoscope/info_zodiac.html', context=data)
    else:
        data = {
            'description_sign': None,
            'title': sign,
        }
        return render(request, 'horoscope/info_zodiac.html', context=data)
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)
    # sign_out = sign_dict.get(sign)
    # if sign_out:
    #     return HttpResponse(f"<h2>{sign_out[0]} (с {sign_out[1]} {sign_out[2]} по {sign_out[3]} {sign_out[4]}).</h2>")
    # else:
    #     return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign}")


def get_info_about_sign_by_number(request, sign):
    if 0 < sign <= len(sign_dict):
        name_zodiac = list(sign_dict)[sign - 1]
        link = reverse("знак зодиака", args=[name_zodiac])
        return HttpResponseRedirect(link)
    return HttpResponseNotFound(f"Знаков зодиака всего двенадцать. Знака под номером {sign} не существует.")


def get_sign(request, month, date):
    if 1 <= month <= 12:
        for key, value in sign_dict.items():
            if months[month][0] == value[2] and value[1] <= date <= months[month][1] or \
                    months[month][0] == value[4] and 1 <= date <= value[3]:
                return HttpResponseRedirect(reverse("знак зодиака", args=[key]))
    return HttpResponseNotFound(f"{month} - реальный месяц и {date} - реальное число этого месяца?")
