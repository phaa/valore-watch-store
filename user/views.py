from django.shortcuts import render, redirect
from .forms import CreditCardForm  
from .models import CreditCard  


# Create your views here.
def index(request):
    return render(request, 'user.html')

def user_data(request):
    return render(request, 'personal.html')

def orders(request):
    return render(request, 'orders.html')

def products(request):
    return render(request, 'my_products.html')
'''
def cards(request):
    return render(request, 'cards.html')
'''
def addresses(request):
    return render(request, 'address.html')

def add_product(request):
    return render(request, 'add_product.html')


# Credit card views
def show_credit_cards(request):  
    cards = CreditCard.objects.all()  
    context = {
        "cards": cards
    }
    return render(request, "cards.html", context)   


def create_credit_card(request):
    context = {}
    if request.method == "POST":
        form = CreditCardForm(request.POST or None)
        
        if form.is_valid():
            try:
                form.save()
                return redirect('user_cards')
            except:
                pass
    else:
        context["cards"] = CreditCard.objects.all() 
        context["form"]= CreditCardForm()
     
    return render(request, 'cards.html', context)



def edit_card(request, id):  
    card = CreditCard.objects.get(id=id)  
    context = {
        "card": card
    }
    return render(request, 'edit.html', context)  


def update_card(request, id):  
    card = CreditCard.objects.get(id=id)  
    form = CreditCardForm(request.POST, instance=card)  
    
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    
    context = {
        "card": card
    }
    return render(request, 'edit.html', context)  


def destroy_card(request, id):  
    card = CreditCard.objects.get(id=id)  
    card.delete()  
    return redirect("/show")  