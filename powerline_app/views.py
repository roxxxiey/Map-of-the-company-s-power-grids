from django.shortcuts import render
from .models import PowerLine
import json


def powerline_map(request):
    try:
        lines = PowerLine.objects.all()

        if not lines:
            return render(request, 'powerline_app/power_line_map.html', {'error': 'Нет данных для отображения.'})

        lines_data = []
        for line in lines:
            if isinstance(line.coordinates, str):
                try:
                    coordinates = json.loads(line.coordinates)
                except json.JSONDecodeError:
                    coordinates = None
            else:
                coordinates = line.coordinates

            lines_data.append({
                'name': line.name,
                'voltage': line.voltage,
                'condition': line.condition,
                'coordinates': coordinates,
            })

        return render(request, 'powerline_app/power_line_map.html', {'lines': json.dumps(lines_data)})

    except Exception as e:
        return render(request, 'powerline_app/power_line_map.html', {'error': f'Ошибка: {str(e)}'})


def about_view(request):
    return render(request, 'powerline_app/about.html')
