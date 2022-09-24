from django import forms
from management.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
        
# class SubcategoryForm(forms.ModelForm):
#     class Meta:
#         model = Subcategory
#         fields = ['name','category','image']
#         widgets = {
#             'name':forms.TextInput(attrs={'class':'form-control'}),
#             'category':forms.Select(attrs={'class':'form-control'}),
#             'image':forms.FileInput(attrs={'class':'form-control'})
#         }     
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
           
        }  

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','subcategory','brand','unitMeasurement','image','description']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'subcategory':forms.Select(attrs={'class':'form-control'}),
            'brand':forms.Select(attrs={'class':'form-control'}),
            'unitMeasurement':forms.Select(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})            
        }
        
class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = ['name','phone','email']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = ['name','file']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'file':forms.FileInput(attrs={'class':'form-control'})
        }

class UserRegisterForm(UserCreationForm):
	username = forms.CharField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
  
# class CambiarContraForm(forms.ModelForm):
#     class Meta:
#         model= CambiarContra
#         fields= ['username','password1','password2']
        