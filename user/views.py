from django.shortcuts import render, redirect
from .forms import AddressForm, CreditCardForm, ProductForm
from .models import Address, CreditCard, Product, ProductImage  


# Create your views here.
def index(request):
    return render(request, 'user.html')

def user_data(request):
    return render(request, 'personal.html')

def orders(request):
    return render(request, 'orders.html')

def products(request):
    return render(request, 'my_products.html')

def addresses(request):
    return render(request, 'address.html')

def add_product(request):
    return render(request, 'add_product.html')


# Address views
def create_address(request):
    print("acessando addresses")
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_addresses')
            except:
                pass
    else:
        addresses = Address.objects.all() 
        form = AddressForm()
     
    context = {
        "addresses": addresses,
        "form": form
    }

    return render(request, 'address.html', context)


def update_address(request, id):  
    address = Address.objects.get(id=id)  
    form = AddressForm(request.POST, instance=address)  
    
    if form.is_valid():  
        form.save()  
        return redirect("user_addresses")  
    
    context = {
        "address": address,
        "addresses": Address.objects.all(),
        "form": form
    }
    return render(request, 'address_edit.html', context)  


def destroy_address(request, id):  
    address = Address.objects.get(id=id)  
    address.delete()  
    return redirect("user_addresses")  



# Credit card views
def create_credit_card(request):
    if request.method == "POST":
        form = CreditCardForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('user_cards')
            except:
                pass
    else:
        cards = CreditCard.objects.all() 
        form = CreditCardForm()
     
    context = {
        "cards": cards,
        "form": form
    }

    return render(request, 'cards.html', context)


def update_card(request, id):  
    card = CreditCard.objects.get(id=id)  
    form = CreditCardForm(request.POST, instance=card)  
    
    if form.is_valid():  
        form.save()  
        return redirect("user_cards")  
    
    context = {
        "card": card,
        "cards": CreditCard.objects.all(),
        "form": form
    }
    return render(request, 'card_edit.html', context)  


def destroy_card(request, id):  
    card = CreditCard.objects.get(id=id)  
    card.delete()  
    return redirect("user_cards")  


# Product views
def show_products(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'products_show.html', context)


def create_product(request):
    if request.method == "POST":
        print("Dentro do post")
        form = ProductForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            print("Form válido")
            try:
                new_product= form.save()

                for image in images:
                    print(vars(image))
                    ProductImage.objects.create(name=image.name, product=new_product, image=image)

                return redirect('user_products')
            except:
                pass
        else:
            print("Form invalido")
    else:
        form = ProductForm()
     
    context = {
        "form": form
    }

    return render(request, 'product_add.html', context)


def update_product(request, id):  
    card = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance=card)  
    
    if form.is_valid():  
        form.save()  
        return redirect("user_cards")  
    
    context = {
        "card": card,
        "form": form
    }
    return render(request, 'product_edit.html', context)  


def destroy_product(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("user_products") 