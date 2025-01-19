from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField()  # текстовое поле
    surname = forms.CharField()  # текстовое поле
    # текстовое поле с настройкой отображения
    feedback = forms.CharField(widget=forms.Textarea(attrs={"cols": "20", "rows": "2"}))
