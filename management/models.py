from asyncio.windows_events import NULL
from enum import unique
import os
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u"Nombre", blank=False, db_column="Nombre")
    status = models.BooleanField(default=True, db_column="Status")
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        
class Subcategory(models.Model):
    name = models.CharField(max_length=50,  unique=True, verbose_name=u"Nombre", blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name=u"Categoría")
    image = models.ImageField(upload_to='subcategory', null=True, verbose_name=u"Imagen", default='subcategory/Logo.png')
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Subcategoría"
        verbose_name_plural = "Subcategorías"

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nombre", blank=False, db_column="Nombre")
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return (self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u"Unidad de medida", blank=False)
    class Type(models.TextChoices):
        MASA = 'Masa',_('Masa')
        VOLUMEN = 'Volumen',_('Volumen')
    type = models.CharField(max_length=30, choices=Type.choices, default=Type.MASA, verbose_name="Tipo de medida")
    status = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return (self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=u"Nombre", blank=False)
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=False, verbose_name=u"Precio")
    description = models.TextField(max_length=150, blank=True, verbose_name=u"Descripción")
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, verbose_name=u"Subcategoría")
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, verbose_name=u"Marca")
    unitMeasurement = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, verbose_name=u"Unidad de Medida")
    stock = models.PositiveIntegerField(validators=[MinValueValidator(1)], blank=False, null=True, verbose_name=u"Stock", default=0)
    type = models.CharField(max_length=30, verbose_name="Tipo de medida", null=True , blank=True )
    name_unitMeasurement= models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='product', null=True, verbose_name=u"Imagen", default='product/Logo.png')
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
    
class Provider(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"Nombre", blank=False)
    phone = models.CharField(max_length=10, verbose_name=u"Teléfono", blank=True)
    email = models.EmailField(max_length=254, verbose_name=u"Correo Electrónico", unique=True)
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return (self.name)
    def clean(self):
        self.name = self.name.title()
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.sql']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Archivo no válido')

class Backup(models.Model):
    name = models.CharField(max_length = 200,default="Copia de Seguridad", blank=True,  verbose_name="Nombre") 
    file = models.FileField(upload_to="media",validators=[validate_file_extension],  verbose_name="Archivo")
    date = models.DateTimeField(auto_now = True)
