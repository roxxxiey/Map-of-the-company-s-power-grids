from django.urls import path
from . import views

urlpatterns = [
    path('', views.powerline_map, name='powerline_map'),
]
