from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home.html', views.main, name='main'),
    path('gallery.html', views.gallery, name='gallery'),
    path('about.html', views.about, name='about'),
    path('medida.html', views.medida, name='medida'),
    path('metraje.html', views.metraje, name='metraje'),
    path('contact.html', views.contact, name='contact'),
]