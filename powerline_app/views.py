from django.shortcuts import render
from .models import PowerLine
import json

def powerline_map(request):
    lines = PowerLine.objects.all()
    # Преобразуем объект QuerySet в список словарей
    lines_data = [{
        'name': line.name,
        'voltage': line.voltage,
        'condition': line.condition,
        'coordinates': line.coordinates,
    } for line in lines]

    # Передаем данные в шаблон
    return render(request, 'powerline_app/power_line_map.html', {'lines': json.dumps(lines_data)})

def about_view(request):
    # Логика для страницы "О проекте"
    return render(request, 'powerline_app/about.html')
