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
    
   # path('compra/<str:modal>/<int:pk>', buy_modal, name='buy-modal'),
    
    path('compra/detalle/<int:pk>/', detail_buy, name="buy-detail"),
    path('compra/detalle/<int:pkf>/<str:modal>/<int:pkd>/', detailbuy_modal, name="detailbuy-modal"),
    path('compra/detalle/<int:pk>/cerrar/', detailbuy_cerrar, name="detailbuy-cerrar"),
    
    # path('compra/detalle/<int:pkf>/<str:modal>/<int:pkd>/', buy_detail_modal, name="buy-detail-modal"),
    # path('compra/detalle/<int:pkf>/', buy_detail_modal, name="buy-detail-modal"),
    path('venta/', sale, name="sale"),
    path('venta/detalle/<int:pk>/', detail_sale, name="sale-detail"),
    

]