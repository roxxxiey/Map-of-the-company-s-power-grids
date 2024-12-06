from django.urls import path
from . import views

urlpatterns = [
    path('', views.powerline_map, name='powerline_map'),
    path('about/', views.about_view, name='about'),  # Страница "О проекте"
]
