from django.http import HttpResponse

directions = ["Знаки зодиака", "Расписание", "Геометрия", "Актёр", "Новостная лента",
              "Информция о людях", "табличка"]
project_links = ['horoscope/', 'week_days/', 'calculate_geometry/', 'actors/',
                 'guinn/', 'people', 'beautiful_table/']
project_directions = [f"<li><a href={link}>{direction}</a></li>"
                      for link, direction in zip(project_links, directions)]


def main(request):
    return HttpResponse(project_directions)
