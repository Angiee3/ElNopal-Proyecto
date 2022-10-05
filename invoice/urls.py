from django.urls import path

from .views import *
from store.views import *

urlpatterns = [
    
    path('compra/', buy, name="buy"),
    
    path('compra/modal/<str:modal>/<int:pk>/', buy_actions, name='buy-actions'),
    
    path('compra/ver/<int:pk>/', buy_view, name='buy-view'),
    
    path('compra/eliminar/<int:pk>/', buy_delete, name='buy-delete'),
    
    path('compra/inactivas/', buy_inactiva, name="buy-inactiva"),
    
    path('compra/inactivas/<str:modal>/<int:pk>/', buy_inactiva_modal, name="buy-inactiva-modal"),
    
    path('compra/detalle/<int:pk>/', detail_buy, name="buy-detail"),
    
    path('compra/detalle/<int:pkf>/<str:modal>/<int:pkd>/', detailbuy_modal, name="detailbuy-modal"),
    
    path('compra/detalle/cerrar/<int:pk>/', detailbuy_cerrar, name="detailbuy-cerrar"),
    
    
    path('venta/', sale, name="sale"),
    
    path('venta/modal/<str:modal>/<int:pk>/', sale_actions, name='sale-actions'),
    
    path('venta/ver/<int:pk>/', sale_view, name='sale-view'),
    
    path('venta/eliminar/<int:pk>/', sale_delete, name='sale-delete'),
    
    path('venta/inactivas/', sale_inactiva, name="sale-inactiva"),
    
    path('venta/inactivas/<str:modal>/<int:pk>/', sale_inactiva_modal, name="sale-inactiva-modal"),
    
    path('venta/detalle/<int:pk>/', detail_sale, name="sale-detail"),
    
    path('venta/detalle/<int:pkf>/<str:modal>/<int:pkd>/', detailsale_modal, name="detailsale-modal"),
    
    path('venta/detalle/cerrar/<int:pk>/', detailsale_cerrar, name="detailsale-cerrar"),
    
]