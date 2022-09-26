from django.urls import path

from .views import *
from store.views import *

urlpatterns = [
    path('compra/', buy, name="buy"),
    path('compra/inactivas/', buy_status, name="buy-status"),
    path('compra/inactivas/<str:modal>/<int:pk>/', buy_status_modal, name="buy-status-modal"),
    
    path('compra/detalle/<int:pk>', detail_buy, name="buy-detail"),
    path('compra/<str:modal>/<int:pk>', buy_modal, name='buy-modal'),
    
    path('venta/', sale, name="sale"),
    path('venta/detalle/<int:pk>', detail_sale, name="sale-detail"),

]