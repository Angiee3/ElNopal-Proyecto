from django.urls import path

from management.views import *
from store.views import *

urlpatterns = [
    path('',index_admin, name="index-admin"),
    path('backup/<str:tipo>/', backup , name="backup"), 
    
    path('categoria/', category, name="category"),
    path('categoria/crear/', categoryCreatePopup, name = "m_category"),
    path('categoria/<str:modal>/<int:pk>', category_modal, name='category-modal'),

    path('subcategoria/', subcategory, name="subcategory"),
    path('subcategoria/crear/', subcategoryCreatePopup, name = "m_subcategory"),
    path('subcategoria/<str:modal>/<int:pk>', subcategory_modal, name="subcategory-modal"),

    path('marca/', brand, name="brand"),
    path('marca/crear/', brandCreatePopup, name = "m_brand"),
    path('marca/<str:modal>/<int:pk>', brand_modal, name="brand-modal"),

    path('producto/', product, name="product"),
    path('producto/crear/', productCreatePopup, name = "m_product"),
    path('producto/<str:modal>/<int:pk>', product_modal, name="product-modal"),

    path('proveedor/', provider, name="provider"),
    path('proveedor/crear/', providerCreatePopup, name = "m_provider"),
    path('proveedor/<str:modal>/<int:pk>', provider_modal, name="provider-modal"),
    
    path('registrar/', registerU, name='registerU'),
    path('registrar/<str:modal>/<int:pk>', user_modal, name='user-modal'),
    path('registrar/crear/', registerCreatePopup, name = "m_register"),


    
]

