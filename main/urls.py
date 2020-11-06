from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home.html', views.main, name='main'),
    path('galeria.html', views.main, name='galeria'),
]