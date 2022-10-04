from django.urls import path
from store.views import *
urlpatterns = [
        path('', index_user, name='inicio'),
        path('carrito/', carrito, name='usuario-carrito'),
        path('contacto/', contact, name='usuario-contacto'),
        path('agregar/<int:product_id>/', agregar_elemento, name="agregar-producto"),
        path('agregar/d/<int:product_id>/', agregar_elemento_carrito, name="agregar_producto_carrito"),
        path('eliminar/<int:product_id>/', eliminar_elemento, name="eliminar_Producto"),
        path('restar/<int:product_id>/', restar_elemento, name="restar_producto"),
        path('limpiar/', limpiar_carrito, name="limpiar_producto"),
]