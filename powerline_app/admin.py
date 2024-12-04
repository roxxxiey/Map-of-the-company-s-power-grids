from django.contrib import admin
from .models import PowerLine

@admin.register(PowerLine)
class PowerLineAdmin(admin.ModelAdmin):
    list_display = ('name', 'voltage', 'condition', 'last_service_date')
    search_fields = ('name',)
