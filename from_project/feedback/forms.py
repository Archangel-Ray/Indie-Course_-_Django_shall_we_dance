from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        labels = {
            "name": "Имя",
            "surname": "Фамилия",
            "feedback": "Отзыв",
            "rating": "Рейтинг",
        }

        error_messages = {
            "name": {  # сообщения при ошибочном вводе
                "max_length": "За что тебя так наказали? А по короче можно?",
                "min_length": "У тебя китайское имя? Может полное напишешь?",
                "required": "У тебя имя есть?",
            },
            "surname": {  # сообщения при ошибочном вводе
                "max_length": "Это от какого поколения столько набралось? Давай только последнее.",
                "min_length": "Ты инициалы ввёл? можешь полностью написать?",
                "required": "Совсем фамилии нет?",
            },
            "feedback": {  # сообщения при ошибочном вводе
                "required": "Ну хоть что-то напиши.",
            },
            "rating": {  # сообщения при ошибочном вводе
                "max_value": "Ну ты заценил. это по двенадцати бальной шкале? у нас пяти бальная",
                "min_value": "всё так плохо?",
                "required": "без оценки дальше не идём.",
            },
        }


class FeedbackFormOld(forms.Form):
    name = forms.CharField(  # текстовое поле
        label="Имя",  # подпись
        max_length=7,  # максимальная длина
        min_length=2,  # минимальная длина
        error_messages={  # сообщения при ошибочном вводе
            "max_length": "Слишком длинное",
            "min_length": "Слишком короткое",
            "required": "Надо что-то написать",
        }
    )
    surname = forms.CharField()  # текстовое поле
    # текстовое поле с настройкой отображения
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "2"}))
    rating = forms.IntegerField(label="Рейтинг", max_value=5, min_value=1)
