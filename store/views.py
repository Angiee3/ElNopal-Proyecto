from ast import Pass
from multiprocessing import context
from django.shortcuts import render , redirect
from management.models import *
from django.contrib import messages
from nopal.carrito import Carro

# Create your views here.
def index_user(request):
    title_pag="Inicio"
    products = Product.objects.all()
    categories= Subcategory.objects.all()
    if request.method == "POST":                                                                    
        ids =  list(request.POST)[1]
        xd = request.POST                                                                   
        products = Product.objects.all().filter(subcategory_id = ids)
        print('aknsjnajsnjnajsnajnsjnjansjnas' , ids , xd )
    context={
        'title_pag':title_pag,
        'categories':categories,
        'products':products
    }
    return render(request, "index.html",context)


def carrito(request):
    title_pag="Carrito"
    context={
        'title_pag':title_pag,
    }
    return render(request, "user/shopping-car.html",context)

def agregar_elemento(request, product_id):   
    carro = Carro(request)
    product_db = Product.objects.get(id=product_id)
    print('skmdkmskmkdmskmdnjsnjndjnjdn3', product_id , product_db.name  )
    carro.agregar(producto=product_db)
    messages.success(request,'Se ha añadido correctamente el producto.')
    return redirect("inicio")

def agregar_elemento_carrito(request, product_id):   
    carro = Carro(request)
    product_db = Product.objects.get(id=product_id)
    carro.agregar(producto=product_db)
    return redirect("usuario-carrito")

def eliminar_elemento(request, product_id):
    carro = Carro(request)
    product_db = Product.objects.get(id=product_id)
    carro.eliminar(producto=product_db)
    return redirect("inicio")

def restar_elemento(request, product_id):
    carro = Carro(request)
    product_db = Product.objects.get(id=product_id)
    carro.restar_producto(producto=product_db)
    return redirect("usuario-carrito")

def limpiar_carrito(request):
    carro = Carro(request)
    carro.limpiar_carro()
    messages.success(request,'Se ha limpiado correctamente el carrito.')
    return redirect("usuario-carrito")

def contact(request):
    title_pag="Contacto"
    context={
        'title_pag':title_pag
    }
    return render(request, "user/contact.html",context)

def gestion_usuario(request):
    title_pag="Gestión Usuario"
    context={
        'title_pag':title_pag
    }
    return render(request, "user/gestionusuario.html",context)
    
