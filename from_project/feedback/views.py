from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        print(name)
        return HttpResponseRedirect('/done')  # перенаправление на сообщение о подтверждении
    return render(request, 'feedback/feedback.html')  # шаблон с формой


def done(request):
    return render(request, 'feedback/done.html')  # шаблон с сообщением о подтверждении
