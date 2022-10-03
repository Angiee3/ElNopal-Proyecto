from django import forms
from store.models import *

# class UserRegisterForm(forms.ModelForm):
#     first_name = forms.CharField(label='Nombre')
#     last_name = forms.CharField(label='Apellido')
#     email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico")
#     username = forms.CharField(label='Nombre de usuario')
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
#     is_active = forms.CharField()

#     class Meta:
#         model = User
#         fields = ['first_name','last_name','email','username', 'password1', 'password2']
#         help_texts = {k:"" for k in fields }
  
