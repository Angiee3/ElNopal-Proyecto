import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required(login_url="admin-login")
def buy(request):
    print(request.POST) # Datos enviados
    location = True # Header
    template = 'buy'   # Datos en invoice.html 
    title_pag = "compras" 
    registers = Buy.objects.all()
    
    if request.method == 'POST':
        print('--------------------------------> Agregando una compra')
        form = BuyForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            buy = Buy.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment']
            )
            print('--------------------------------> Compra agregada')
            messages.success(request, f'La compra No.{buy.id} está lista para añadir productos.')
            return redirect('buy-detail', pk=buy.id)
    else:
        form = BuyForm()
            
    context = {
        'form':form,
        'title_pag':title_pag,
        'registers': registers,
        'location':location,
        'template':template,
    }
    return render(request, 'invoice/invoice.html', context)
@login_required(login_url="admin-login")
def detail_buy(request, pk):
    print(request.POST) # Datos enviados
    location = True # Header
    template = 'buy' # Datos en detail.html 
    title_pag = "productos - Compra No."+str(pk)
    
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    registers = DetailBuy.objects.filter(buy=pk)
    factura = Buy.objects.filter(id=pk)
    buy_id = Buy.objects.get(id=pk)
    total = 0 

    if request.method == 'POST':
        form = DetailBuyForm(request.POST)
        if form.is_valid():
            product = Product.objects.get(
                id = request.POST['product']
            )
            print('------------------------> Obtiene producto con id '+str(product.id))            
            detail = DetailBuy.objects.filter(
                buy = buy_id,
                product = request.POST['product'],
            )
            print('------------------------> Filtra si hay detalle con ese producto')
            
            if detail.exists(): # ------------------------ Busca detalle, si existe, la filtra
                print('------------------------> Sí lo hay')
                total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                print('------------------------> Se agrega el total ',total)
                detail.update(
                    amount =  detail[0].amount + form.cleaned_data.get('amount'),
                    total = detail[0].total + total
                )
                print('------------------------> Actualización de la cantidad de producto en el detalle existente y el total')
                
                Product.objects.filter(id = product.id).update(
                    stock = product.stock + form.cleaned_data.get('amount')
                )
                print('------------------------> Stock actualizado del producto')

                Buy.objects.filter(id=pk).update(
                    finalPrice = factura[0].finalPrice + total
                )
                print('------------------------> Total de la factura actualizado')
                
                messages.success(request,f'{product} se añadió a la compra!')
                return redirect('buy-detail', pk) 
        
            else:
                print('------------------------> No lo hay')
                
                DetailBuy.objects.create( # ------------------------ Crea un detalle
                    buy = buy_id,
                    product = product,
                    amount = request.POST['amount'], 
                )
                print('------------------------> Detalle creado:')
                
                Product.objects.filter(id = product.id).update(
                    stock = int(product.stock) + int(request.POST['amount'])
                )
                print('------------------------> Stock actualizado del producto')

                total = form.cleaned_data.get('amount') * int(form.cleaned_data.get('product').price)
                print('------------------------> ',total)
                
                detail.update(
                    total = detail[0].total + total
                )
                print('------------------------> Total del detalle actualizado')

                Buy.objects.filter(id=pk
                        ).update(
                            finalPrice = factura[0].finalPrice + total
                        )
                print('------------------------> Total de la factura actualizado')
                
                messages.success(request,f'{product} se añadió a la compra!')
                return redirect('buy-detail', pk)            
    else:
        form = DetailBuyForm()
        
    context = {
        'form':form,
        'title_pag':title_pag,
        'registers': registers,
        'location':location,
        'template':template,
        'factura': Buy.objects.get(id=pk),
        'url_factura':url_factura,
    }
    return render(request, 'invoice/detail.html', context)
@login_required(login_url="admin-login")
def detailbuy_modal(request, pkf, modal, pkd):
    print(request.POST) # Datos enviados
    location = True # Header
    title_pag = "productos - Compra No."+str(pkf)
    template = 'buy'
    modal_title = ''
    modal_txt = ''    
    modal_submit = ''
    url_back="/facturacion/compra/detalle/"+str(pkf)+"/"
    
    registers = DetailBuy.objects.all()
    register_id = DetailBuy.objects.get(id=pkd)
    buy_a = Buy.objects.filter(id=pkf)
    
    if modal == 'eliminar':
        modal_title = 'Eliminar detalle'
        modal_txt = 'eliminar el producto'
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
            
            DetailBuy.objects.filter(buy=pkf, product=product).delete()
            
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
        modal_txt = 'editar el producto'
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
        'registers':registers,
        'location':location,
        'template':template,
    }
    return render(request, 'invoice/modal-detail.html', context)
@login_required(login_url="admin-login")
def detailbuy_cerrar(request, pk):
    print(request)
    location = True # Header
    template = 'buy' # Datos en invoice.html 
    title_pag = "productos - Compra No."+str(pk)
    modal_title = ''
    modal_txt = ''
    location = True
    modal_submit = ''
    modal = 'cerrar'
    url_back="/facturacion/compra/detalle/"+str(pk)+"/"
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    factura = Buy.objects.get(id=pk)
    registers = DetailBuy.objects.filter(buy=pk)
    register_id = pk
    detail = DetailBuy.objects.filter(buy = pk)
    print('------------------------> Filtra si hay detalle')
            
    print('------------------------> Cerrando facturaxd')
    if detail.exists():
        modal_title = 'Cerrar compra'
        modal_txt = 'cerrar la compra'
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
        'template':template,
        'registers':registers,
        'location':location,
        'register_id':register_id,
        'factura':factura,
    }
    return render(request, 'invoice/modal-detail.html', context)
@login_required(login_url="admin-login")
def buy_actions(request, modal, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    template = 'buy'
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
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
        url_back = '/facturacion/compra/'
            
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
        'template':template,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-invoice.html', context)
@login_required(login_url="admin-login")
def buy_view(request, pk):
    location = True
    template = 'buy'
    title_pag = "compra No."+str(pk)
    modal = True
    url_factura="/facturacion/compra/detalle/"+str(pk)+"/cerrar/"
    
    registers = DetailBuy.objects.filter(buy=pk)
    factura = Buy.objects.filter(id=pk)
    url_back = "/facturacion/compra/"
    
    factura = Buy.objects.get(id=pk)
    context = {
        'title_pag':title_pag,
        'registers': registers,
        'location':location,
        'template':template,
        'factura':factura,
        'modal':modal,
        'url_factura':url_factura,
        'url_back':url_back,
    }
    return render(request, 'invoice/detail-view.html', context)
@login_required(login_url="admin-login")
def buy_delete(request, pk):
    title_pag = "Compra"
    modal_title = ''
    modal_txt = ''
    location = True
    template = 'buy'
    modal_submit = ''
    url_back="/facturacion/compra/"
    registers = Buy.objects.all()
    register_id = Buy.objects.get(id=pk)
    print(request)
    modal = 'eliminar'
    detail = DetailBuy.objects.filter(buy=pk)
    print(detail)    
    if detail.exists():
        if not user.is_staff :
            messages.warning(request, f'La compra No.{pk} no se puede eliminar, tiene detalles de compra.')
            return redirect ('buy')
        else: 
            messages.warning(request, f'La compra No.{pk} tiene detalles de compra. Deben eliminarse.')
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

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'template':template,
        'registers':registers,
        'location':location,
        'modal':modal,
    }
    return render(request, 'invoice/modal-invoice.html', context)
@login_required(login_url="admin-login")
def buy_inactiva(request):
    location = True
    template = 'buy'
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
        'registers': registers,
        'location':location,
        'template':template,
        'inactivas':inactivas,
    }
    return render(request, 'invoice/inactiva.html', context)
@login_required(login_url="admin-login")
def buy_inactiva_modal(request, modal, pk):
    title_pag = "Compra"
    location = True
    template = 'buy'
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
        'template':template,
        'register_id':register_id,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-invoice.html', context)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(login_url="admin-login")
def sale(request):
    location = True
    template = 'sale'
    title_pag = "Venta"
    registers = Sale.objects.all()
    if request.method == 'POST':
        print('VENTA-------------------------------->')
        form = SaleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            sale = Sale.objects.create(
                date = date_aux,
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
        'registers': registers,
        'location':location,
        'template':template,
    }
    return render(request, 'invoice/invoice.html', context)
@login_required(login_url="admin-login")
def detail_sale(request, pk):
    location = True
    template = 'sale'
    title_pag = "Venta"
    
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
        
        'registers': registers,
        'location':location,
        'template':template,
        'factura':factura,
    }
    return render(request, 'invoice/detail.html', context)

def detailsale_modal(request, pkf, modal, pkd):
    print(request.POST) # Datos enviados
    location = True # Header
    title_pag = "productos - Venta No."+str(pkf)
    template = 'sale'
    modal_title = ''
    modal_txt = ''    
    modal_submit = ''
    url_back="/facturacion/venta/detalle/"+str(pkf)+"/"
    
    registers = DetailSale.objects.all()
    register_id = DetailSale.objects.get(id=pkd)
    sale_a = Sale.objects.filter(id=pkf)
    
    if modal == 'eliminar':
        modal_title = 'Eliminar detalle'
        modal_txt = 'eliminar el detalle'
        modal_submit = 'eliminar'
        form = DetailSaleForm(request.POST, request.FILES)
        if request.method == 'POST':
            product = Product.objects.get(
                id = register_id.product.id
            )
            print('----------------------------------------ELIMINANDO')
            
            detail_a = DetailSale.objects.filter(
                sale = pkf,
                product = product, 
            )
            print(detail_a)
            print('------------------------> Detalle en donde está el producto')
            
            amount = register_id.amount
            print(amount)
            
            Product.objects.filter(id = product.id).update(
                stock = int(product.stock) + amount
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
            
            DetailSale.objects.filter(sale=pkf, product=product).delete()
            
            Sale.objects.filter(id=pkf).update(
                finalPrice = sale_a[0].finalPrice - total
            )
            
            messages.success(request, f'El detalle se eliminó correctamente!')
            return redirect ('sale-detail', pkf)
                
            
        else:
            form=DetailSaleForm()
            
    elif modal == 'editar':
        modal_title = 'Editar detalle'
        modal_txt = 'editar el detalle'
        modal_submit = 'guardar'
        form = DetailSaleEditForm(request.POST, request.FILES, instance=register_id)
        cantidad = register_id.amount
        if request.method == 'POST':
            print('----------------------------------------EDITANDO venta')  
            product = Product.objects.get(
                        id = register_id.product.id
                    )
            
            stock_f = product.stock + register_id.amount
            print('Stock que queda',product.stock)
            print('Stock completo')
            print(stock_f)
            
            if form.is_valid():
                if(stock_f >= int(request.POST['amount'])):    
                    print(request.POST['amount'])
                    print(cantidad)
                    
                    if int(request.POST['amount'])>cantidad:
                        print('------------------------> Si la cantidad ingresada es mayor a la que teniamos')
                        amount = int(request.POST['amount']) - cantidad
                        print('------------------------> Se saca la diferencia')
                        print(amount)
                        
                        detail_a = DetailSale.objects.filter(
                            sale = pkf,
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
                            total = detail_a[0].total + total
                        )
                        print('------------------------> Total ')
                        
                        DetailSale.objects.filter(sale=pkf, product=product).update(
                            amount = request.POST['amount']
                        )
                        
                        Sale.objects.filter(id=pkf).update(
                            finalPrice = sale_a[0].finalPrice + total
                        )
                        
                        messages.success(request, f'El detalle se editó correctamente!')
                        return redirect ('sale-detail', pkf)
                    
                    
                    else:
                        print('------------------------> Si la cantidad ingresada es menor a la que teniamos')
                        amount = cantidad - int(request.POST['amount'])
                        print('------------------------> Se saca la diferencia')
                        print(amount)
                        
                        detail_a = DetailSale.objects.filter(
                            sale = pkf,
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
                            total =  detail_a[0].total - total
                        )
                        print('------------------------> Total ')
                        
                        DetailSale.objects.filter(sale=pkf, product=product).update(
                            amount = request.POST['amount']
                        )
                        
                        Sale.objects.filter(id=pkf).update(
                            finalPrice = sale_a[0].finalPrice - total
                        )
                        
                        messages.success(request, f'El detalle se editó correctamente!')
                        return redirect ('sale-detail', pkf)
                else:
                    messages.warning(request, f'Sólo tenemos {stock_f} {product.name_unitMeasurement} disponibles de {product} :c')
                        
        else:
            form=DetailSaleEditForm(instance=register_id)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'template':template,  
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def detailsale_cerrar(request, pk):
    print(request)
    location = True # Header
    template = 'sale' # Datos en invoice.html 
    title_pag = "productos - Venta No."+str(pk)
    modal_title = ''
    modal_txt = ''
    location = True
    
    modal_submit = ''
    modal = 'cerrar'
    url_back="/facturacion/venta/detalle/"+str(pk)+"/"
    url_factura="/facturacion/venta/detalle/"+str(pk)+"/cerrar/"
    registers = DetailSale.objects.filter(sale=pk)
    
    detail = DetailSale.objects.filter(sale = pk)
    print('------------------------> Filtra si hay detalle')
            
    print('------------------------> Cerrando facturaxd')
    if detail.exists():
        modal_title = 'Cerrar venta'
        modal_txt = 'cerrar la venta No.'
        modal_submit = 'cerrar'
        form = SaleForm(request.POST, request.FILES)
        print('xdd')
        if request.method == 'POST':
            print('----------------------------------------CERRANDO')
            Sale.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Cerrado')
            messages.success(request, f'La venta No.{pk} se cerró correctamente!')
            return redirect ('sale')
    else:
        messages.warning(request, f'No hay detalles en esta venta, agrega productos para poder cerrarla!')
        return redirect ('sale-detail', pk)
        
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'url_factura':url_factura,
        'modal':modal,
        'title_pag':title_pag,
        'template':template,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-detail.html', context)

def sale_actions(request, modal, pk):
    title_pag = "Venta"
    modal_title = ''
    modal_txt = ''
    location = True
    template = 'sale'
    modal_submit = ''
    url_back="/facturacion/venta/"
    registers = Sale.objects.all()
    register_id = Sale.objects.get(id=pk)
    print(request)
    form = " "
    
    if modal == 'editar':
        modal_title = 'Editar la venta'
        modal_txt = 'editar la venta'
        modal_submit = 'guardar'
        form =  SaleForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                messages.success(request, f'La venta {pk} se editó correctamente!')
                return redirect ('sale')
        else:
            form=  SaleForm(instance=register_id) 
    
    elif modal == 'marcar':
        print('---------------------------------------marcar')
        modal_title = 'Marcar venta'
        modal_txt = 'marcar la venta'
        modal_submit = 'marcar'
        form = SaleFormStatus(request.POST, request.FILES)
        url_back = '/facturacion/venta/'
            
        if request.method == 'POST':
            print('----------------------------------------MARCANDO')
            Sale.objects.filter(id=pk).update(
                status = "Pendiente",
                observation = request.POST['observation']
            )
            print('Marcada')
            messages.success(request, f'La venta No.{pk} se marcó correctamente!')
            return redirect ('sale')
        else:
            form = SaleFormStatus()
    
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'register_id':register_id,
        'title_pag':title_pag,
        'template':template,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-invoice.html', context)

def sale_view(request, pk):
    location = True
    template = 'sale'
    title_pag = "venta No."+str(pk)
    modal = True
    url_factura="/facturacion/venta/detalle/"+str(pk)+"/cerrar/"
    
    registers = DetailSale.objects.filter(sale=pk)
    factura = Sale.objects.filter(id=pk)
    url_back = "/facturacion/venta/"
    
    factura = Sale.objects.get(id=pk)
    context = {
        'title_pag':title_pag,
        'registers': registers,
        'location':location,
        'template':template,
        'factura':factura,
        'modal':modal,
        'url_factura':url_factura,
        'url_back':url_back,
    }
    return render(request, 'invoice/detail-view.html', context)

def sale_delete(request, pk):
    title_pag = "venta"
    modal_title = ''
    modal_txt = ''
    location = True
    template = 'sale'
    modal_submit = ''
    url_back="/facturacion/venta/"
    registers = Sale.objects.all()
    register_id = Sale.objects.get(id=pk)
    print(request)
    modal = 'eliminar'
    detail = DetailSale.objects.filter(sale=pk)
    print(detail)    
    if detail.exists():
        if not user.is_staff :
            messages.warning(request, f'La venta No.{pk} no se puede eliminar, tiene detalles de venta.')
            return redirect ('sale')
        else: 
            messages.warning(request, f'La venta No.{pk} tiene detalles de venta. Debe ser marcada antes de eliminarse')
            return redirect ('sale')
    else: 
        modal_title = 'Eliminar venta'
        modal_txt = 'eliminar la venta'
        modal_submit = 'eliminar'
            
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Sale.objects.filter(id=pk).update(
                status = "Anulada"
            )
            print('Eliminado')
            messages.success(request, f'La venta No.{pk} se eliminó correctamente!')
            return redirect ('sale')  

    context ={
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'register_id':register_id,
        'title_pag':title_pag,
        'template':template,
        'registers':registers,
        'location':location,
        'modal':modal,
    }
    return render(request, 'invoice/modal-invoice.html', context)
    
def sale_inactiva(request):
    location = True
    template = 'sale'
    title_pag = "ventas Inactivas/Pendientes"
    registers = Sale.objects.all()
    inactivas = True
    
    if request.method == 'POST':
        print('venta-------------------------------->')
        form = SaleForm(request.POST)
        if form.is_valid():
            print(request.POST)
            date_aux = datetime.now().strftime("%Y-%m-%d")
            sale = Sale.objects.create(
                date = date_aux,
                user = form.cleaned_data['user'],
                payment = request.POST['payment']
            )
            messages.success(
                request, f'La venta #{sale.id} está lista para añadir productos')
            return redirect('sale-detail', pk=sale.id)
    else:
        form = SaleForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'registers': registers,
        'location':location,
        'template':template,
        'inactivas':inactivas,
    }
    return render(request, 'invoice/inactiva.html', context)

def sale_inactiva_modal(request, modal, pk):
    title_pag = "venta"
    location = True
    template = 'sale'
    modal_title = ''
    modal_txt = ''
    modal_submit = ''
    url_back = "/facturacion/venta/inactivas/"
    registers = Sale.objects.all()
    register = Sale.objects.get(id=pk)
    register_id = register.id
    form = ""
    
    if modal == 'eliminar': 
        detail = DetailSale.objects.filter(sale=pk)
        print(detail)    
        if detail.exists():
                
            messages.warning(request, f'La venta No.{pk} no se puede eliminar, tiene detalles de venta. Debe eliminarlos antes.')
            return redirect ('sale-detail', pk)
        else: 
            modal_title = 'Eliminar venta'
            modal_txt = 'eliminar la venta'
            modal_submit = 'eliminar'
                
            if request.method == 'POST':
                print('----------------------------------------ELIMINANDO')
                Sale.objects.filter(id=pk).update(
                    status = "Anulada"
                )
                print('Eliminado')
                messages.success(request, f'La venta No.{pk} se eliminó correctamente!')
                return redirect ('sale') 
            
    elif modal == 'desmarcar':  
        print('----------------------------------------> Editar Modal')
        modal_title = 'Desmarcar venta'
        modal_txt = 'desmarcar la venta'
        modal_submit = 'Desmarcar'
        form = SaleForm(request.POST, instance=register)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Sale.objects.filter(id=pk).update(
                status = "Cerrada"
            )
            print('Eliminado')
            messages.success(request, f'La venta No.{pk} se desmarcó correctamente!')
            return redirect ('buy-inactiva')
        else:
            form = SaleForm()    
            
    context ={
        'form':form,
        'modal_title':modal_title,
        'modal_txt':modal_txt,
        'modal_submit':modal_submit,
        'url_back':url_back,
        'modal':modal,
        'title_pag':title_pag,
        'template':template,
        'register_id':register_id,
        'registers':registers,
        'location':location,
    }
    return render(request, 'invoice/modal-invoice.html', context)
