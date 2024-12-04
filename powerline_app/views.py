from django.shortcuts import render
import json
from .models import PowerLine

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
