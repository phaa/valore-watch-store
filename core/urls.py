from django.urls import path

from .views import anuncio, index

urlpatterns = [
    path('', index, name='index'),
    path('relogio/', anuncio, name='anuncio_individual'),
]
