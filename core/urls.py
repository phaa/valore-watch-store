from django.urls import path

from .views import anuncio, home, index

urlpatterns = [
    path('', index, name='index'),
    path('relogio/', anuncio, name='anuncio_individual'),
    path('', home, name='homepage')
]
