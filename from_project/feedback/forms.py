from django import forms


class FeedbackForm(forms.Form):
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
