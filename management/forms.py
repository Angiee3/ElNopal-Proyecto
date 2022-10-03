from select import select
from django import forms
from management.models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_select2.forms import ModelSelect2Widget


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
        
class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name','category','image']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
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
        fields = ['name','price','subcategory','brand','image','description','name_unitMeasurement']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'subcategory':forms.Select(attrs={'class':'form-control'}),
            'brand':forms.Select(attrs={'class':'form-control'}),
            'unitMeasurement':forms.Select(attrs={'class':'form-control select2'}),
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
        
class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name','type']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control select2 select_padre'}),
        }


class UserRegisterForm(UserCreationForm):
    # name = forms.CharField(label='Nombre')
    # lastname = forms.CharField(label='Apellido')
    # nDocument = forms.CharField(label='Número de documento')
    # phone = forms.CharField(label='Número de celular')
    email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico")
    username = forms.CharField(label='Nombre de usuario')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    status = models.BooleanField(default=True, db_column="Status")

    class Meta:
        model = User
        fields = ['email','username', 'password1', 'password2']
        help_texts = {k:"" for k in fields }