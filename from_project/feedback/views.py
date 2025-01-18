from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        if not name:
            # форма с выводом сообщения об ошибке
            return render(request, 'feedback/feedback.html', context={'got_error': True})
        print(name)
        # перенаправление на сообщение о подтверждении
        return HttpResponseRedirect('/done')
    # шаблон с формой. сообщение об ошибке не выводить
    return render(request, 'feedback/feedback.html', context={'got_error': False})


def done(request):
    # шаблон с сообщением о подтверждении
    return render(request, 'feedback/done.html')
