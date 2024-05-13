from django import forms
from product.models import Products

class productform(forms.ModelForm): #Form definition
    class Meta:
        model=Products
        fields="__all__"