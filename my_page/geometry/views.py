from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def main(request):
    menu = ""
    for el in (('rectangle', '1', '2'), ('square', '5'), ('circle', '3')):
        # link = reverse("Площадь прямоугольника", args=[el])
        joining_elements = '/'.join(el)
        menu += f"""<h2><li><a href="{joining_elements}">{el[0]}</li></h2>"""
    return HttpResponse(menu)


def get_rectangle_area(request, width, height):
    return render(request, 'geometry/rectangle.html')
    # return HttpResponse(f"Площадь прямоугольника {width}х{height} равна {width * height}")


def get_rectangle_area_redirect(request, width, height):
    link = reverse("площадь прямоугольника", args=[width, height])
    return HttpResponseRedirect(link)


def get_square_area(request, width):
    return render(request, 'geometry/square.html')
    # return HttpResponse(f"Площадь квадрата размером {width}х{width} равна {width * width}")


def get_square_area_redirect(request, width):
    link = reverse("площадь квадрата", args=[width])
    return HttpResponseRedirect(f"/calculate_geometry/square/{width}")


def get_circle_area(request, radius):
    return render(request, 'geometry/circle.html')
    # return HttpResponse(f"Площадь круга с радиусом {radius} равна {radius ** 2 * 3.14}")


def get_circle_area_redirect(request, radius):
    link = reverse("площадь круга", args=[radius])
    return HttpResponseRedirect(f"/calculate_geometry/circle/{radius}")
