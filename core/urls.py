from django.urls import path
from .views import index, anuncio

urlpatterns = [
    path('', index, name='index'),
    path('relogio/', anuncio, name='anuncio_individual'),
]
