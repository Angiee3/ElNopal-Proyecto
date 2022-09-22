from django.urls import path

from .views import *
from store.views import *

urlpatterns = [
        
    path('compra/', buy, name="buy"),
    path('buy-w/', buy_w, name="buy-w"),

    path('compra/detalle/<int:pk>', detail_buy, name="buy-detail"),
    
    path('venta/', sale, name="sale"),
    path('venta/detalle/<int:pk>', detail_sale, name="sale-detail"),

]