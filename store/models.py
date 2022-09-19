from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser):
    username = models.CharField(verbose_name=u"Nombre de Usuario", max_length=100, unique=True)
    email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico", unique=True)
    name = models.CharField(max_length=50, verbose_name="Nombre")
    lastName = models.CharField(max_length=50, verbose_name="Apellido")
    class t_Document(models.TextChoices):
        CC = 'CC' , _('Cédula de Ciudadanía')
        CE = 'CE',_('Cédula de Extranjeria')
        TI = 'TI',_('Tarjeta de Identidad')
    tDocument = models.CharField(max_length=21,choices=t_Document.choices, verbose_name="Tipo de Documento")
    nDocument = models.IntegerField(verbose_name="Número de Documento")
    phone = models.CharField(max_length=10, verbose_name=u"Teléfono")
    dateBirth = models.DateField(verbose_name="Fecha Nacimiento")
    email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico")
    user_admin = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','name','lastName','tDocument','nDocument']
    
    def __str__(self):
        return ' %s %s' %(self.name, self.lastName)  
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.user_admin
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"