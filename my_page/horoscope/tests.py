from django.test import TestCase


class TestHoroscope(TestCase):
    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
                      response.content.decode())

    def test_libra_redirect(self):
        zodiac_list = ['', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
                       'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
        for i in range(1, 13):
            response = self.client.get(f'/horoscope/{i}/')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f"/horoscope/{zodiac_list[i]}/")

    def test_signs(self):
        zodiac_dict = {
            'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
            'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
            'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
            'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
            'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
            'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
            'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
            'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
            'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
            'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
            'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
            'pisces': 'Рыбы - двенадцатый знак зодиака, планета Юпитер (с 20 февраля по 20 марта).',
        }
        for i in range(len(zodiac_dict)):
            key = list(zodiac_dict)[i]
            response = self.client.get(f'/horoscope/{key}/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(zodiac_dict[key], response.content.decode())
            response_redirect = self.client.get(f'/horoscope/{i + 1}/')
            self.assertEqual(response_redirect.status_code, 302)
            self.assertEqual(response_redirect.url, f"/horoscope/{key}/")
