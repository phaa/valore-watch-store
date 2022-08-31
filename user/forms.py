from django import forms  
from .models import Address, CreditCard, Product 

class AddressForm(forms.ModelForm):  
    class Meta:  
        model = Address  
        fields = [
            "description",
            "zip",
            "public_place",
            "number",
            "complement",
            "reference",
            "neighborhood",
            "city",
            "state",
            "is_main",
        ]  


class CreditCardForm(forms.ModelForm):  
    class Meta:  
        model = CreditCard  
        fields = [
            "owner",
            "number",
            "valid_until",
            "cvv"
        ] 


class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = [
            "name",
            "price",
            "brand",
            "description",
            "category",
        ] 