from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'itens_list.html')


def anuncio(request):
    return render(request, 'relogio.html')


def home(request):
    return render(request, '')
