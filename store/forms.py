from django import forms
from store.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','name','lastName','tDocument','nDocument','phone','dateBirth','email','user_admin']  
        widgets={
            'dateBirth':forms.DateInput(format=(' %m/%d/%Y'),
                                    attrs={'class':'form-control',
                                            'placeholder':'Seleccione la fecha de nacimiento',
                                            'type':'date'})
        }