from django import forms
from .models import *
        
class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields =['user','payment']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control js-example-basic-simple'}),
            'payment':forms.Select(attrs={'class':'form-control'}),
            'observations':forms.Select(attrs={'class':'form-control'})
        }
        
class BuyFormStatus(forms.ModelForm):
    class Meta:
        model = Buy
        fields =['observation']
        widgets = {
            'observation':forms.Select(attrs={'class':'form-control'}),
        }
        
class DetailBuyForm(forms.ModelForm):
    class Meta:
        model = DetailBuy
        fields = ['product','amount']
        widgets = {
            'product':forms.Select(attrs={'class':'form-control '}),
            'amount':forms.NumberInput(attrs={'class':'form-control'})
        }
    
class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields=['user','typeSale','payment','client','nDocument','address']
        widgets = {
            'user':forms.Select(attrs={'class':'form-control '}),
            'typeSale':forms.Select(attrs={'class':'form-control'}),
            'payment':forms.Select(attrs={'class':'form-control'}),
            'client':forms.TextInput(attrs={'class':'form-control'}),
            'nDocument':forms.NumberInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'observations':forms.Select(attrs={'class':'form-control'})
        }
        
class SaleFormStatus(forms.ModelForm):
    class Meta:
        model = Sale
        fields =['observation']
        widgets = {
            'observation':forms.Select(attrs={'class':'form-control'}),
        }
        
class DetailSaleForm(forms.ModelForm):
    class Meta:
        model = DetailSale
        fields =['product','amount']
        widgets = {
            'product':forms.Select(attrs={'class':'form-control '}),
            'amount':forms.NumberInput(attrs={'class':'form-control'})
        }
     