import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from management.forms import UserRegisterForm
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def buy(request):
    location = True
    admin = True
    buy_template = True
    title_pag = "Compra"
    registers = Buy.objects.all()
    form = BuyForm()
    if request.method == 'POST':
        print('--------------------------------> COMPRA')
        form = BuyForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            buy = Buy.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment']
            )
            messages.success(
                request, f'La compra #{buy.id} está lista para añadir productos')
            return redirect('buy-detail', pk=buy.id)
        else:
            form = BuyForm()
            
    print(request.POST)
            
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
    }
    return render(request, 'invoice/buy.html', context)

def detail_buy(request, pk):
    location = True
    admin = True
    buy_template = True
    title_pag = "Compra"
    modal = True
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    
    registers = DetailBuy.objects.filter(buy=pk)
    buy_a = Buy.objects.filter(id=pk)
    buy_id = Buy.objects.get(id=pk)
    total = 0
    
    factura = Buy.objects.get(id=pk)

    if request.method == 'POST':
        form = DetailBuyForm(request.POST)
        if form.is_valid():
            print('------------------------> Formato válido')
            product = Product.objects.get(
                id=request.POST['product']
            )
            print('------------------------> Producto con id')
            
            detail = DetailBuy.objects.filter(
                buy = buy_id,
                product = request.POST['product'],
            )
            print('------------------------> Filtra si hay detalle')
            
            if detail.exists(): # ------------------------ Busca detalle, si existe, la filtra
                print('------------------------> Detalle Existe')
                detail_a = DetailBuy.objects.filter(
                    buy = pk,
                    product = request.POST['product'], 
                )
                print('------------------------> Busca si ya está el producto')
                if detail_a.exists():
                    print('Producto encontrado ')
                    total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                    print('------------------------> ',total)
                    detail_a.update(
                        amount =  detail_a[0].amount + form.cleaned_data.get('amount'),
                        total = detail_a[0].total + total
                    )
                    print('------------------------> Actualización de la cantidad de producto en el detalle existente')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = product.stock + form.cleaned_data.get('amount')
                    )
                    print('------------------------> Stock actualizado')

                    Buy.objects.filter(
                        id=pk
                        ).update(
                            finalPrice = buy_a[0].finalPrice + total
                        )
                    print('------------------------> Total actualizado')
                    
                    messages.success(request,f'{product} se añadió a la compra!')
                    return redirect('buy-detail', pk) 
           
            else:
                detail_a = DetailBuy.objects.filter(
                    buy = pk,
                    product = request.POST['product'], 
                )
                print('------------------------> Detalle NO Existe')
                
                DetailBuy.objects.create( # ------------------------ Crea un detalle
                    buy = buy_id,
                    product = product,
                    amount = request.POST['amount'], 
                )
                print('------------------------> Detalle creado:')
                
                Product.objects.filter(id = product.id).update(
                    stock = int(product.stock) + int(request.POST['amount'])
                )
                print('------------------------> Stock actualizado')

                total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                print('------------------------> ',total)
                detail_a.update(
                    total = detail_a[0].total + total
                )
                print('------------------------> Total ')

                Buy.objects.filter(
                        id=pk
                        ).update(
                            finalPrice = buy_a[0].finalPrice + total
                        )
                print('------------------------> Total Compra actualizado')
                messages.success(request,f'{product} se añadió a la compra!')
                return redirect('buy-detail', pk)            
    else:
        form = DetailBuyForm()
        
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
        'factura':factura,
        'modal':modal,
        'url_factura':url_factura,
    }
    return render(request, 'invoice/detail.html', context)

def detailbuy_modal(request, pkf, modal, pkd):
    print(request)
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/detalle/"+str(pkf)+"/"
    registers = DetailBuy.objects.all()
    register_id = DetailBuy.objects.get(id=pkd)
    buy_a = Buy.objects.filter(id=pkf)
    
    if modal == 'eliminar':
        modal_title = 'Eliminar detalle'
        modal_txt = 'eliminar el detalle'
        modal_submit = 'eliminar'
        form = DetailBuyForm(request.POST, request.FILES)
        if request.method == 'POST':
            product = Product.objects.get(
                id = register_id.product.id
            )
            print('----------------------------------------ELIMINANDO')
            
            detail_a = DetailBuy.objects.filter(
                buy = pkf,
                product = product, 
            )
            print(detail_a)
            print('------------------------> Detalle en donde está el producto')
            
            amount = register_id.amount
            print(amount)
            
            Product.objects.filter(id = product.id).update(
                stock = int(product.stock) - amount
            )
            print(product.id)
            print('------------------------> Stock actualizado')

            total = amount * int(product.price)
            print('------------------------> Total de la actualización')
            print('------------------------> ',total)
            
            detail_a.update(
                total =  detail_a[0].total - total
            )
            print('------------------------> Total ')
            
            DetailBuy.objects.filter(buy=pkf, product=product).update(
                status = False
            )
            
            Buy.objects.filter(id=pkf).update(
                finalPrice = buy_a[0].finalPrice - total
            )
            
            Product.objects.filter(id=pkd).update(
                status = False
            )
            messages.success(request, f'El detalle se eliminó correctamente!')
            return redirect ('buy-detail', pkf)
                
            
        else:
            form=DetailBuyForm()
            
    elif modal == 'editar':
        modal_title = 'Editar detalle'
        modal_txt = 'editar el detalle'
        modal_submit = 'guardar'
        form = DetailBuyEditForm(request.POST, request.FILES, instance=register_id)
        cantidad = register_id.amount
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                product = Product.objects.get(
                    id = register_id.product.id
                )
                print(request.POST['amount'])
                print(cantidad)
                
                if int(request.POST['amount'])>cantidad:
                    print('------------------------> Si la cantidad ingresada es mayor a la que teniamos')
                    amount = int(request.POST['amount']) - cantidad
                    print('------------------------> Se saca la diferencia')
                    print(amount)
                    
                    detail_a = DetailBuy.objects.filter(
                        buy = pkf,
                        product = product, 
                    )
                    print(detail_a)
                    print('------------------------> Detalle en donde está el producto')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = int(product.stock) + amount
                    )
                    print(product.id)
                    print('------------------------> Stock actualizado')

                    total = amount * int(product.price)
                    print('------------------------> Total de la actualización')
                    print('------------------------> ',total)
                    
                    detail_a.update(
                        total = detail_a[0].total + total
                    )
                    print('------------------------> Total ')
                    
                    DetailBuy.objects.filter(buy=pkf, product=product).update(
                        amount = request.POST['amount']
                    )
                    
                    Buy.objects.filter(id=pkf).update(
                        finalPrice = buy_a[0].finalPrice + total
                    )
                    
                    messages.success(request, f'El detalle se editó correctamente!')
                    return redirect ('buy-detail', pkf)
                
                
                else:
                    print('------------------------> Si la cantidad ingresada es menor a la que teniamos')
                    amount = cantidad - int(request.POST['amount'])
                    print('------------------------> Se saca la diferencia')
                    print(amount)
                    
                    detail_a = DetailBuy.objects.filter(
                        buy = pkf,
                        product = product, 
                    )
                    print(detail_a)
                    print('------------------------> Detalle en donde está el producto')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = int(product.stock) - amount
                    )
                    print(product.id)
                    print('------------------------> Stock actualizado')

                    total = amount * int(product.price)
                    print('------------------------> Total de la actualización')
                    print('------------------------> ',total)
                    
                    detail_a.update(
                        total =  detail_a[0].total - total
                    )
                    print('------------------------> Total ')
                    
                    DetailBuy.objects.filter(buy=pkf, product=product).update(
                        amount = request.POST['amount']
                    )
                    
                    Buy.objects.filter(id=pkf).update(
                        finalPrice = buy_a[0].finalPrice - total
                    )
                    
                    messages.success(request, f'El detalle se editó correctamente!')
                    return redirect ('buy-detail', pkf)
        else:
            form=DetailBuyEditForm(instance=register_id)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def detailbuy_cerrar(request, pk):
    print(request)
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    modal = 'cerrar'
    url_back="/facturacion/compra/detalle/"+str(pk)+"/"
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    registers = DetailBuy.objects.filter(buy=pk)
    
    detail = DetailBuy.objects.filter(buy = pk)
    print('------------------------> Filtra si hay detalle')
            
    print('------------------------> Cerrando facturaxd')
    if detail.exists():
        modal_title = 'Cerrar compra'
        modal_txt = 'cerrar la compra No.'
        modal_submit = 'cerrar'
        form = BuyForm(request.POST, request.FILES)
        print('xdd')
        if request.method == 'POST':
            print('----------------------------------------CERRANDO')
            Buy.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Cerrado')
            messages.success(request, f'La compra No.{pk} se cerró correctamente!')
            return redirect ('buy')
    else:
        messages.warning(request, f'No hay detalles en esta compra, agrega productos para poder cerrarla!')
        return redirect ('buy-detail', pk)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'url_factura':url_factura,
        'modal':modal,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def buy_actions(request, modal, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    ver_compra = False
    form = " "
    
    if modal == 'editar':
        modal_title = 'Editar la compra'
        modal_txt = 'editar la compra'
        modal_submit = 'guardar'
        form =  BuyForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                messages.success(request, f'La compra {pk} se editó correctamente!')
                return redirect ('buy')
        else:
            form=  BuyForm(instance=register_id) 
    
    elif modal == 'marcar':
        print('---------------------------------------marcar')
        modal_title = 'Marcar compra'
        modal_txt = 'marcar la compra'
        modal_submit = 'marcar'
        form = BuyFormStatus(request.POST, request.FILES)
            
        if request.method == 'POST':
            print('----------------------------------------MARCANDO')
            Buy.objects.filter(id=pk).update(
                status = "Pendiente",
                observation = request.POST['observation']
            )
            print('Marcada')
            messages.success(request, f'La compra No.{pk} se marcó correctamente!')
            return redirect ('buy')
        else:
            form = BuyFormStatus()
    
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'ver_compra':ver_compra,
    }
    return render(request, 'invoice/modal-buy.html', context)

def buy_view(request, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    ver_compra = False
    
    print('----------------------------------------------> Ver factura')
    modal_title = 'Ver factura'
    registers = DetailBuy.objects.filter(buy=pk)
    ver_compra = True
    factura = Buy.objects.filter(id=pk)
    print(factura)
    print(registers)    

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'ver_compra':ver_compra,
    }
    return render(request, 'invoice/modal-buy.html', context)

def buy_delete(request, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    modal = 'eliminar'
    detail = DetailBuy.objects.filter(buy=pk)
    print(detail)    
    if detail.exists():
        if not User.is_staff:
            messages.warning(request, f'La compra No.{pk} no se puede eliminar, tiene detalles de compra.')
            return redirect ('buy')
        else: 
            messages.warning(request, f'La compra No.{pk} tiene detalles de compra. Debe ser marcada antes de eliminarse')
            return redirect ('buy')
    else: 
        modal_title = 'Eliminar compra'
        modal_txt = 'eliminar la compra'
        modal_submit = 'eliminar'
            
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Buy.objects.filter(id=pk).update(
                status = "Anulada"
            )
            print('Eliminado')
            messages.success(request, f'La compra No.{pk} se eliminó correctamente!')
            return redirect ('buy')  

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'modal':modal,
    }
    return render(request, 'invoice/modal-buy.html', context)
    
def buy_inactiva(request):
    location = True
    admin = True
    buy_template = True
    title_pag = "Compras Inactivas/Pendientes"
    registers = Buy.objects.all()
    inactivas = True
    
    if request.method == 'POST':
        print('COMPRA-------------------------------->')
        form = BuyForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            buy = Buy.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment']
            )
            messages.success(
                request, f'La compra #{buy.id} está lista para añadir productos')
            return redirect('buy-detail', pk=buy.id)
    else:
        form = BuyForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
        'inactivas':inactivas,
    }
    return render(request, 'invoice/buy-inactiva.html', context)

def buy_inactiva_modal(request, modal, pk):
    title_pag = "Compra"
    location = True
    admin = True
    modal_title = ''
    modal_txt = ''
    modal_submit = ''
    url_back = "/facturacion/compra/inactivas/"
    registers = Buy.objects.all()
    register = Buy.objects.get(id=pk)
    register_id = register.id
    form = ""
    
    if modal == 'eliminar': 
        detail = DetailBuy.objects.filter(buy=pk)
        print(detail)    
        if detail.exists():
                
            messages.warning(request, f'La compra No.{pk} no se puede eliminar, tiene detalles de compra. Debe eliminarlos antes.')
            return redirect ('buy-detail', pk)
        else: 
            modal_title = 'Eliminar compra'
            modal_txt = 'eliminar la compra'
            modal_submit = 'eliminar'
                
            if request.method == 'POST':
                print('----------------------------------------ELIMINANDO')
                Buy.objects.filter(id=pk).update(
                    status = "Anulada"
                )
                print('Eliminado')
                messages.success(request, f'La compra No.{pk} se eliminó correctamente!')
                return redirect ('buy') 
            
    elif modal == 'desmarcar':  
        print('----------------------------------------> Editar Modal')
        modal_title = 'Desmarcar compra'
        modal_txt = 'desmarcar la compra'
        modal_submit = 'Desmarcar'
        form = BuyForm(request.POST, instance=register)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Buy.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Eliminado')
            messages.success(request, f'La compra No.{pk} se desmarcó correctamente!')
            return redirect ('buy-inactiva')
        else:
            form = BuyForm()    
            
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'title_pag':title_pag,
        'admin':admin,
        'register_id':register_id,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-.html', context)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def sale(request):
    location = True
    admin = True
    buy_template = False
    title_pag = "Venta"
    registers = Sale.objects.all()
    
    usuarios= User.objects.values_list('username')
    res = [value for value, in usuarios]
    if request.method == 'POST':
        print('VENTA-------------------------------->')
        form = SaleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            sale = Sale.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment'],
            )
            if request.POST['client'] or request.POST['address'] or request.POST['nDocument']:
                Sale.objects.filter(id=sale.id).update(
                    client = request.POST['client'],
                    address = request.POST['address'],
                    nDocument = request.POST['nDocument'],
                )
            messages.success(
                request, f'La venta #{sale.id} está lista para añadir productos')
            return redirect('sale-detail', pk=sale.id)
    else:
        form = SaleForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
        'res':res
    }
    return render(request, 'invoice/sale.html', context)

def detail_sale(request, pk):
    location = True
    admin = True
    buy_template = False
    title_pag = "Venta"
    modal = False
    
    registers = DetailSale.objects.filter(sale=pk)
    sale_a = Sale.objects.filter(id=pk)
    sale_id = Sale.objects.get(id=pk)
    total = 0
    
    factura = Sale.objects.get(id=pk)

    if request.method == 'POST':
        form = DetailSaleForm(request.POST)
        if form.is_valid():
            print('------------------------> Formato válido')
            product = Product.objects.get(
                id=request.POST['product']
            )
            print('------------------------> Producto con id')
            
            detail = DetailSale.objects.filter(
                sale = sale_id,
                product = request.POST['product'],
            )
            print('------------------------> Filtra si hay detalle')
            
            
            if(product.stock >= int(request.POST['amount'])):
                if detail.exists(): # ------------------------ Busca detalle, si existe, la filtra
                    print('------------------------> Detalle Existe')
                    detail_a = DetailSale.objects.filter(
                        sale = pk,
                        product = request.POST['product'], 
                    )
                    print('------------------------> Busca si ya está el producto')
                    if detail_a.exists():
                        print('Producto encontrado ')
                        
                    
                        total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                        print('------------------------> ',total)
                        detail_a.update(
                            amount =  detail_a[0].amount + form.cleaned_data.get('amount'),
                            total = detail_a[0].total + total
                        )
                        print('------------------------> Actualización de la cantidad de producto en el detalle existente')
                        
                        Product.objects.filter(id = product.id).update(
                            stock = product.stock - form.cleaned_data.get('amount')
                        )
                        print('------------------------> Stock actualizado')

                        Sale.objects.filter(
                            id=pk
                            ).update(
                                finalPrice = sale_a[0].finalPrice + total
                            )
                        print('------------------------> Total actualizado')
                        
                        messages.success(request,f'{product} se añadió a la venta!')
                        return redirect('sale-detail', pk=pk) 
            
                else:
                    detail_a = DetailSale.objects.filter(
                        sale = pk,
                        product = request.POST['product'], 
                    )
                    print('------------------------> Detalle NO Existe')
                    
                    DetailSale.objects.create( # ------------------------ Crea un detalle
                        sale = sale_id,
                        product = product,
                        amount = request.POST['amount'], 
                    )
                    print('------------------------> Detalle creado:')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = int(product.stock) - int(request.POST['amount'])
                    )
                    print('------------------------> Stock actualizado')

                    total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                    print('------------------------> ',total)
                    detail_a.update(
                        total = detail_a[0].total + total
                    )
                    print('------------------------> Total ')

                    Sale.objects.filter(
                            id=pk
                            ).update(
                                finalPrice = sale_a[0].finalPrice + total
                            )
                    print('------------------------> Total Venta actualizado')
                    messages.success(request,f'{product} se añadió a la venta!')
                    return redirect('sale-detail', pk=pk)
            else:
                messages.warning(request, f'Sólo tenemos {product.stock} disponibles de {product} :c')
    else:
        form = DetailSaleForm()
        
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
        'factura':factura,
        'modal':modal
    }
    return render(request, 'invoice/detail.html', context)

def detailsale_modal(request, pkf, modal, pkd):
    print(request)
    title_pag = "Venta"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/venta/detalle/"+str(pkf)+"/"
    registers = DetailSale.objects.all()
    register_id = DetailSale.objects.get(id=pkd)
    sale_a = Sale.objects.filter(id=pkf)
    
    if modal == 'eliminar':
        modal_title = 'Eliminar detalle'
        modal_txt = 'eliminar el detalle'
        modal_submit = 'eliminar'
        form = DetailBuyForm(request.POST, request.FILES)
        if request.method == 'POST':
            product = Product.objects.get(
                id = register_id.product.id
            )
            print('----------------------------------------ELIMINANDO')
            
            detail_a = DetailBuy.objects.filter(
                buy = pkf,
                product = product, 
            )
            print(detail_a)
            print('------------------------> Detalle en donde está el producto')
            
            amount = register_id.amount
            print(amount)
            
            Product.objects.filter(id = product.id).update(
                stock = int(product.stock) - amount
            )
            print(product.id)
            print('------------------------> Stock actualizado')

            total = amount * int(product.price)
            print('------------------------> Total de la actualización')
            print('------------------------> ',total)
            
            detail_a.update(
                total =  detail_a[0].total - total
            )
            print('------------------------> Total ')
            
            DetailBuy.objects.filter(buy=pkf, product=product).update(
                status = False
            )
            
            Buy.objects.filter(id=pkf).update(
                finalPrice = buy_a[0].finalPrice - total
            )
            
            Product.objects.filter(id=pkd).update(
                status = False
            )
            messages.success(request, f'El detalle se eliminó correctamente!')
            return redirect ('buy-detail', pkf)
                
            
        else:
            form=DetailBuyForm()
            
    elif modal == 'editar':
        modal_title = 'Editar detalle'
        modal_txt = 'editar el detalle'
        modal_submit = 'guardar'
        form = DetailBuyEditForm(request.POST, request.FILES, instance=register_id)
        cantidad = register_id.amount
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                product = Product.objects.get(
                    id = register_id.product.id
                )
                print(request.POST['amount'])
                print(cantidad)
                
                if int(request.POST['amount'])>cantidad:
                    print('------------------------> Si la cantidad ingresada es mayor a la que teniamos')
                    amount = int(request.POST['amount']) - cantidad
                    print('------------------------> Se saca la diferencia')
                    print(amount)
                    
                    detail_a = DetailBuy.objects.filter(
                        buy = pkf,
                        product = product, 
                    )
                    print(detail_a)
                    print('------------------------> Detalle en donde está el producto')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = int(product.stock) + amount
                    )
                    print(product.id)
                    print('------------------------> Stock actualizado')

                    total = amount * int(product.price)
                    print('------------------------> Total de la actualización')
                    print('------------------------> ',total)
                    
                    detail_a.update(
                        total = detail_a[0].total + total
                    )
                    print('------------------------> Total ')
                    
                    DetailBuy.objects.filter(buy=pkf, product=product).update(
                        amount = request.POST['amount']
                    )
                    
                    Buy.objects.filter(id=pkf).update(
                        finalPrice = buy_a[0].finalPrice + total
                    )
                    
                    messages.success(request, f'El detalle se editó correctamente!')
                    return redirect ('buy-detail', pkf)
                
                
                else:
                    print('------------------------> Si la cantidad ingresada es menor a la que teniamos')
                    amount = cantidad - int(request.POST['amount'])
                    print('------------------------> Se saca la diferencia')
                    print(amount)
                    
                    detail_a = DetailBuy.objects.filter(
                        buy = pkf,
                        product = product, 
                    )
                    print(detail_a)
                    print('------------------------> Detalle en donde está el producto')
                    
                    Product.objects.filter(id = product.id).update(
                        stock = int(product.stock) - amount
                    )
                    print(product.id)
                    print('------------------------> Stock actualizado')

                    total = amount * int(product.price)
                    print('------------------------> Total de la actualización')
                    print('------------------------> ',total)
                    
                    detail_a.update(
                        total =  detail_a[0].total - total
                    )
                    print('------------------------> Total ')
                    
                    DetailBuy.objects.filter(buy=pkf, product=product).update(
                        amount = request.POST['amount']
                    )
                    
                    Buy.objects.filter(id=pkf).update(
                        finalPrice = buy_a[0].finalPrice - total
                    )
                    
                    messages.success(request, f'El detalle se editó correctamente!')
                    return redirect ('buy-detail', pkf)
        else:
            form=DetailBuyEditForm(instance=register_id)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def detailbuy_cerrar(request, pk):
    print(request)
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    modal = 'cerrar'
    url_back="/facturacion/compra/detalle/"+str(pk)+"/"
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    registers = DetailBuy.objects.filter(buy=pk)
    
    detail = DetailBuy.objects.filter(buy = pk)
    print('------------------------> Filtra si hay detalle')
            
    print('------------------------> Cerrando facturaxd')
    if detail.exists():
        modal_title = 'Cerrar compra'
        modal_txt = 'cerrar la compra No.'
        modal_submit = 'cerrar'
        form = BuyForm(request.POST, request.FILES)
        print('xdd')
        if request.method == 'POST':
            print('----------------------------------------CERRANDO')
            Buy.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Cerrado')
            messages.success(request, f'La compra No.{pk} se cerró correctamente!')
            return redirect ('buy')
    else:
        messages.warning(request, f'No hay detalles en esta compra, agrega productos para poder cerrarla!')
        return redirect ('buy-detail', pk)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'url_factura':url_factura,
        'modal':modal,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def buy_actions(request, modal, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    ver_compra = False
    form = " "
    
    if modal == 'editar':
        modal_title = 'Editar la compra'
        modal_txt = 'editar la compra'
        modal_submit = 'guardar'
        form =  BuyForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                messages.success(request, f'La compra {pk} se editó correctamente!')
                return redirect ('buy')
        else:
            form=  BuyForm(instance=register_id) 
    
    elif modal == 'marcar':
        print('---------------------------------------marcar')
        modal_title = 'Marcar compra'
        modal_txt = 'marcar la compra'
        modal_submit = 'marcar'
        form = BuyFormStatus(request.POST, request.FILES)
            
        if request.method == 'POST':
            print('----------------------------------------MARCANDO')
            Buy.objects.filter(id=pk).update(
                status = "Pendiente",
                observation = request.POST['observation']
            )
            print('Marcada')
            messages.success(request, f'La compra No.{pk} se marcó correctamente!')
            return redirect ('buy')
        else:
            form = BuyFormStatus()
    
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'ver_compra':ver_compra,
    }
    return render(request, 'invoice/modal-buy.html', context)

def buy_view(request, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    ver_compra = False
    
    print('----------------------------------------------> Ver factura')
    modal_title = 'Ver factura'
    registers = DetailBuy.objects.filter(buy=pk)
    ver_compra = True
    factura = Buy.objects.filter(id=pk)
    print(factura)
    print(registers)    

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'ver_compra':ver_compra,
    }
    return render(request, 'invoice/modal-buy.html', context)

def buy_delete(request, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    modal = 'eliminar'
    detail = DetailBuy.objects.filter(buy=pk)
    print(detail)    
    if detail.exists():
        if not User.is_staff:
            messages.warning(request, f'La compra No.{pk} no se puede eliminar, tiene detalles de compra.')
            return redirect ('buy')
        else: 
            messages.warning(request, f'La compra No.{pk} tiene detalles de compra. Debe ser marcada antes de eliminarse')
            return redirect ('buy')
    else: 
        modal_title = 'Eliminar compra'
        modal_txt = 'eliminar la compra'
        modal_submit = 'eliminar'
            
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Buy.objects.filter(id=pk).update(
                status = "Anulada"
            )
            print('Eliminado')
            messages.success(request, f'La compra No.{pk} se eliminó correctamente!')
            return redirect ('buy')  

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
        'modal':modal,
    }
    return render(request, 'invoice/modal-buy.html', context)
    
def buy_inactiva(request):
    location = True
    admin = True
    buy_template = True
    title_pag = "Compras Inactivas/Pendientes"
    registers = Buy.objects.all()
    inactivas = True
    
    if request.method == 'POST':
        print('COMPRA-------------------------------->')
        form = BuyForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            buy = Buy.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment']
            )
            messages.success(
                request, f'La compra #{buy.id} está lista para añadir productos')
            return redirect('buy-detail', pk=buy.id)
    else:
        form = BuyForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'buy_template':buy_template,
        'inactivas':inactivas,
    }
    return render(request, 'invoice/buy-inactiva.html', context)

def buy_inactiva_modal(request, modal, pk):
    title_pag = "Compra"
    location = True
    admin = True
    modal_title = ''
    modal_txt = ''
    modal_submit = ''
    url_back = "/facturacion/compra/inactivas/"
    registers = Buy.objects.all()
    register = Buy.objects.get(id=pk)
    register_id = register.id
    form = ""
    
    if modal == 'eliminar': 
        detail = DetailBuy.objects.filter(buy=pk)
        print(detail)    
        if detail.exists():
                
            messages.warning(request, f'La compra No.{pk} no se puede eliminar, tiene detalles de compra. Debe eliminarlos antes.')
            return redirect ('buy-detail', pk)
        else: 
            modal_title = 'Eliminar compra'
            modal_txt = 'eliminar la compra'
            modal_submit = 'eliminar'
                
            if request.method == 'POST':
                print('----------------------------------------ELIMINANDO')
                Buy.objects.filter(id=pk).update(
                    status = "Anulada"
                )
                print('Eliminado')
                messages.success(request, f'La compra No.{pk} se eliminó correctamente!')
                return redirect ('buy') 
            
    elif modal == 'desmarcar':  
        print('----------------------------------------> Editar Modal')
        modal_title = 'Desmarcar compra'
        modal_txt = 'desmarcar la compra'
        modal_submit = 'Desmarcar'
        form = BuyForm(request.POST, instance=register)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Buy.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Eliminado')
            messages.success(request, f'La compra No.{pk} se desmarcó correctamente!')
            return redirect ('buy-inactiva')
        else:
            form = BuyForm()    
            
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'title_pag':title_pag,
        'admin':admin,
        'register_id':register_id,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-.html', context)


# /////////////////////////RegistroUser////////////////////

def registerU(request):
    location = True
    admin = True
    title_pag = "Registro"
    registers= User.objects.all()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
           form.save()

        name = form.cleaned_data.get('username')
        messages.success(request,f'El usuario {name} se agregó correctamente!')
                    
        return redirect('registerU')
        
    else:
        form = UserRegisterForm()
    context = { 'form' : form,
            	'registers':registers,
                'location':location,
                'admin':admin,
                'title_pag':title_pag
	}
    return render(request, 'admin/register.html', context)


def registerP(request,pk):
    location = True
    admin = True
    title_pag = "Registro"
    registers= User.objects.all()
    registers_obj = User.objects.get(id=pk)

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
           form.save()
           User.objects.filter(id=pk).update(
               email=form.cleaned_data.get('email')
            )   
        name = form.cleaned_data.get('username')
        messages.success(request,f'El usuario {name} se agregó correctamente!')
                    
        return redirect('registerU')
        
    else:
        form = UserRegisterForm()
    context = { 'form' : form,
            	'registers':registers,
                'location':location,
                'admin':admin,
                'registers_obj':registers_obj,
                'title_pag':title_pag
	}
    return render(request, 'admin/register.html', context)

def registerCreatePopup(request):
    location = True
    admin = True
    title_pag = "Registro"
    registers = User.objects.all()    
    form = UserRegisterForm(request.POST, request.FILES) 

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_register");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_register.html", context)

def user_modal(request, modal, pk):
    title_pag = "Usuario"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/administracion/usuario/"
    registers = User.objects.all()
    register_id = User.objects.get(id=pk)
    if modal == 'eliminar':
        modal_title = 'Eliminar usuario'
        modal_txt = 'eliminar el usuario'
        modal_submit = 'eliminar'
        form = UserRegisterForm(request.POST, request.FILES)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            User.objects.filter(id=pk).update(
                status = False
            )
            userName = register_id.username.title()
            messages.success(request, f'El usuario {userName} se eliminó correctamente!')
            return redirect ('user')
        else:
            form=UserRegisterForm()
    elif modal == 'editar':
        modal_title = 'Editar usuario'
        modal_txt = 'editar el usuario'
        modal_submit = 'guardar'
        form = UserRegisterForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                userName = form.cleaned_data.get('username')
                messages.success(request, f'El usuario {userName} se editó correctamente!')
                return redirect ('registerU')
        else:
            form=UserRegisterForm(instance=register_id)
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'admin':admin,
        'registers':registers,
        'location':location,
    }
    return render(request, 'admin/modal-user.html', context)
