from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'user.html')

def user_data(request):
    return render(request, 'personal.html')

def orders(request):
    return render(request, 'orders.html')

def products(request):
    return render(request, 'my_products.html')

def cards(request):
    return render(request, 'cards.html')

def addresses(request):
    return render(request, 'address.html')

def add_product(request):
    return render(request, 'add_product.html')
