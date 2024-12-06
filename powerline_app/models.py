from django.db import models


class PowerLine(models.Model):
    VOLTAGE_CHOICES = [
        ('low', 'Low Voltage'),
        ('medium', 'Medium Voltage'),
        ('high', 'High Voltage'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название линии")
    voltage = models.CharField(max_length=10, choices=VOLTAGE_CHOICES, verbose_name="Напряжение")
    condition = models.CharField(max_length=100, verbose_name="Техническое состояние")
    last_service_date = models.DateField(verbose_name="Дата последнего обслуживания")
    coordinates = models.JSONField(verbose_name="Координаты линии")

    def __str__(self):
        return self.name
