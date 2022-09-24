from django.urls import path

from management.views import *
from store.views import *

urlpatterns = [
    path('product/create/', product, name="product"),
    path('subcategory/create/', subcategoryCreatePopup, name = "subcategory"),


    # path('',index_admin, name="index-admin"),
    # path('backup/<str:tipo>/', backup , name="backup"), 
    
    # path('categoria/', category, name="category"),
    # path('categoria/<str:modal>/<int:pk>', category_modal, name='category-modal'),
    # # path('subcategoria/', subcategory, name="subcategory"),
    # # path('subcategoria/<str:modal>/<int:pk>', subcategory_modal, name="subcategory-modal"),
    # path('marca/', brand, name="brand"),
    # path('marca/<str:modal>/<int:pk>', brand_modal, name="brand-modal"),
    # path('producto/', product, name="product"),
    # path('producto/<str:modal>/<int:pk>', product_modal, name="product-modal"),
    # path('proveedor/', provider, name="provider"),
    # path('proveedor/<str:modal>/<int:pk>', provider_modal, name="provider-modal"),
    # # path('usuario/<int:pk>', user, name="user"),
    # path('usuario/<str:modal>/<int:pk>', user_modal, name="user-modal"),

    # path('registrar/', registrar, name='registrar'),
    
]

