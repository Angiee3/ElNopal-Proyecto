from django.db import models
from management.models import *
from django.utils.translation import gettext_lazy as _

        
class Payment(models.TextChoices):
        dtf = 'Datáfono', _('Datafono')
        eft = 'Efectivo', _('Efectivo')
        tsc = 'Transacción', _('Transaccion')
class Status(models.TextChoices):
        ABIERTA='Abierta', _('Abierta')
        CERRADA='Cerrada', _('Cerrada')
        ANULADA='Anulada', _('Anulada')
        
class Buy(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Compra")
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, verbose_name=u"Proveedor")
    payment = models.CharField(max_length=11, choices=Payment.choices, default=Payment.eft, verbose_name=u"Método de Pago", blank=False)
    finalPrice = models.IntegerField(default=0, null=False, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name="Estado", default=Status.ABIERTA)
    statusBuy = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.date)
    class Meta:
        verbose_name="Compra"
        verbose_name_plural = "Compras"
        
class DetailBuy(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.SET_NULL, null=True, verbose_name=u"Id Compra")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,verbose_name=u"Producto")
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1, verbose_name=u"Cantidad")
    total = models.IntegerField(default=0, null=False, blank=True)
    status = models.BooleanField(default=True, verbose_name="Estado")
    class Meta:
        verbose_name="Detalle de compra"
        verbose_name_plural = "Detalle de compras"
        
class Sale(models.Model):
    date = models.DateField(auto_now=True, verbose_name="Fecha de Venta")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name=u"Empleado")
    client = models.CharField(blank=True, null=False, max_length=50, verbose_name=u"Cliente", default=u"Cliente local")
    nDocument = models.CharField(blank=True, null=False, max_length=20, verbose_name=u"Número de Documento / NIT", default=1234567890)
    address = models.CharField(blank=True, null=False, verbose_name=u"Dirección", max_length=254, default=u"Local")
    class TypeSale(models.TextChoices):
        store = 'store', _('Local')
        address = 'Domicilio', _('Domicilio')
    typeSale = models.CharField(max_length=9, choices=TypeSale.choices, default=TypeSale.store, verbose_name=u"Tipo de Venta")
    finalPrice = models.IntegerField(default=0, null=False, blank=True)
    payment = models.CharField(max_length=11, choices=Payment.choices, default=Payment.eft, verbose_name=u"Método de Pago", blank=False)
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name="Estado", default=Status.ABIERTA)
    statusSale = models.BooleanField(default=True)
    def __str__(self) -> str:
        return ' %s' %(self.date)
    def clean(self):
        self.client = self.client.title()
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        
class DetailSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True, verbose_name=u"Id Venta")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True,verbose_name=u"Producto")
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)],default=1, verbose_name=u"Cantidad")
    total = models.IntegerField(default=0, null=False, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name="Estado", default=Status.ABIERTA)
    class Meta:
        verbose_name="Detalle de venta"
        verbose_name_plural = "Detalle de ventas"
        
