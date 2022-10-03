from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# class User(AbstractBaseUser):
#     first_name = models.CharField(max_length=50, verbose_name="Nombre")
#     last_name = models.CharField(max_length=50, verbose_name="Apellido")
#     email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico")
#     username = models.CharField(verbose_name=u"Nombre de Usuario", max_length=100, unique=True)
#     user_admin = models.BooleanField(default=False)
#     status = models.BooleanField(default=True)
    
#     USERNAME_FIELD='username'
#     REQUIRED_FIELDS=['first_name','last_name','email']
    
#     def __str__(self):
#         return ' %s %s' %(self.first_name, self.lastName)  
#     def has_perm(self,perm,obj = None):
#         return True
#     def has_module_perms(self,app_label):
#         return True
    
#     @property
#     def is_staff(self):
#         return self.user_admin
#     class Meta:
#         verbose_name = "Usuario"
#         verbose_name_plural = "Usuarios"