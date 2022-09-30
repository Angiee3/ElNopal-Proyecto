import os
from datetime import datetime, date
from django.shortcuts import render , redirect
from django.contrib import messages
from management.forms import *
from management.models import *
from store.forms import *
from store.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from invoice.models import *

from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index_admin(request):
    location = True
    admin = True
    title_pag = "Menú de Administracion"
    registros=DetailSale.objects.all()
    registrosci=Sale.objects.all()

    registros_stats=registros.values('product').annotate(total_registros=Sum(('amount'), output_field=models.PositiveIntegerField())).order_by('total_registros')
    total_registros=DetailSale.objects.aggregate(Sum('amount'))['amount__sum']

    # for mes in range(12):
    #     fecha_stats1=Sale.objects.get(id=mes['sale'])
    #     mes['sale'].append(Sale.filter(date__month=mes+1, date__year=datetime.now().year)
        
    #     mes['DetailSale'].objects.agreggate(Sum('amount'))['amount__sum']) 

    # for i in registros_stats:
    #     i['product']=Product.objects.get(id=i['product'])
    # registros_grupos=registros_stats.all()
    # registros_grupos_final={}
    
    # for j in registros_grupos:
    #     j['product']=Product.objects.get(id=j['product']).subcategory
    #     if registros_grupos_final.get(j['product']) != None:
    #        registros_grupos_final[j['product']]+= j['total_registros']
    #     else:
    #        registros_grupos_final[j['product']]= j['total_registros']

    fecha_stats=registrosci.values("date")
    # fecha_aux = datetime.now().strftime("%Y-%m-%d")

    valor=registros.annotate(total_registros=Sum(('amount'),  output_field=models.IntegerField()))

    context = {
        'title_pag':title_pag,
        'admin':admin,
        'location':location,
        'registros_stats':registros_stats,
        'fecha_stats':fecha_stats,
        'valor':valor,
        'total_registros':total_registros,
        # 'registros_grupos':registros_grupos_final
    }
    return render(request, "admin/index-admin.html", context)

########################### SUBCATEGORY ############################
########################### SUBCATEGORY ############################
def subcategory(request):
    location = True
    admin = True
    title_pag = "Subcategoría"
    registers = Subcategory.objects.all()
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f'La subcategoría {name} se agregó correctamente!')
            return redirect('subcategory')
    else:
        form = SubcategoryForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, 'admin/subcategory.html', context)

def subcategoryCreatePopup(request):
    location = True
    admin = True
    title_pag = "Subcategoría"
    registers = Subcategory.objects.all()    
    form = SubcategoryForm(request.POST, request.FILES ) 

    if form.is_valid():
        instance = form.save()
        name = form.cleaned_data.get('name')
        messages.success(request,f'La subcategoría {name} se agregó correctamente!')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_subcategory");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_subcategory.html", context)

def subcategory_modal(request, modal, pk):
    location = True
    admin = True
    title_pag = "Subcategoría"
    modal_title = ''
    modal_txt = ''
    modal_submit = ''
    url_back="/administracion/subcategoria/"
    registers = Subcategory.objects.all()
    register_id = Subcategory.objects.get(id=pk)
    
    
    
    if modal == 'eliminar':
        modal_title = 'Eliminar subcategoría'
        modal_txt = 'eliminar la subcategoría'
        modal_submit = 'eliminar'
        form = SubcategoryForm(request.POST, request.FILES)
        if request.method == 'POST' :
            print('----------------------------------------ELIMINANDO')
            Subcategory.objects.filter(id=pk).update(
                status = False
            )
            print('-------------------------------------------------SE ELIMINÓ')
            subcategoryName = register_id.name.title()
            messages.success(request, f'La subcategoría {subcategoryName} se eliminó correctamente!')

            return redirect ('subcategory')
        else:
            form=SubcategoryForm()
            
            
            
    elif modal == 'editar':
        modal_title = 'Editar subcategoría'
        modal_txt = 'editar la subcategoría'
        modal_submit = 'guardar'
        form = SubcategoryForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                subcategoryName = form.cleaned_data.get('name')
                messages.success(request, f'La subcategoría {subcategoryName} se editó correctamente!')
                return redirect ('subcategory')
        else:
            form=SubcategoryForm(instance=register_id)
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
        'location':location
    }
    return render(request, 'admin/modal-category.html', context)


############################# CATEGORY #############################
def category(request):
    location = True
    admin = True
    title_pag = "Categoría"
    registers = Category.objects.all()
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f'La categoría {name} se agregó correctamente!')
            return redirect('category')
    else:
        form = CategoryForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, 'admin/category.html', context)
def categoryCreatePopup(request):
    location = True
    admin = True
    title_pag = "Categoría"
    registers = Category.objects.all()    
    form = CategoryForm(request.POST, request.FILES) 

    if form.is_valid():
        instance = form.save()
        name = form.cleaned_data.get('name')
        messages.success(request,f'La categoría {name} se agregó correctamente!')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_subcategory");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_category.html", context)

def category_modal(request, modal, pk):
    title_pag = "Categoría"
    location = True
    admin = True
    modal_title = ''
    modal_txt = ''
    modal_submit = ''
    url_back="/administracion/categoria/"
    registers = Category.objects.all()
    register_id = Category.objects.get(id=pk)
    
    
    
    if modal == 'eliminar':
        modal_title = 'Eliminar categoría'
        modal_txt = 'eliminar la categoría'
        modal_submit = 'eliminar'
        form = SubcategoryForm(request.POST, request.FILES)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Category.objects.filter(id=pk).update(
                status = False
            )
            print('Eliminado')
            categoryName = register_id.name.title()
            messages.success(request, f'La categoría {categoryName} se eliminó correctamente!')
            return redirect ('category')
        else:
            form = CategoryForm()
        
    
    
    elif modal == 'editar':
        modal_title = 'Editar categoría'
        modal_txt = 'editar la categoría'
        modal_submit = 'guardar'
        form = CategoryForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                categoryName = form.cleaned_data.get('name')
                messages.success(request, f'La categoría {categoryName} se editó correctamente!')
                return redirect ('category')
        else:
            form = CategoryForm(instance=register_id)
            
            
            
            
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
    return render(request, 'admin/modal-category.html', context)

############################## BRAND ###############################
def brand(request):
    location = True
    admin = True
    title_pag = "Marca"
    registers = Brand.objects.all()
    # fields = [f.name for f in Subcategory()._meta.get_fields()][2:-1]
    fields = ['name']
    # print(fields)
    atributes = ['Nombre']
    if request.method   == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f'La marca {name} se agregó correctamente!')
            return redirect('brand')
    else:
        form = BrandForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'fields':fields,
        'atributes':atributes
    }
    return render(request, 'admin/brand.html', context)

def brandCreatePopup(request):
    location = True
    admin = True
    title_pag = "Marca"
    registers = Brand.objects.all()    
    form = BrandForm(request.POST, request.FILES) 

    if form.is_valid():
        instance = form.save()
        name = form.cleaned_data.get('name')
        messages.success(request,f'La marca {name} se agregó correctamente!')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_subcategory");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_brand.html", context)

def brand_modal(request, modal, pk):
    title_pag = "Marca"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/administracion/marca/"
    registers = Brand.objects.all()
    register_id = Brand.objects.get(id=pk)
    if modal == 'eliminar':
        modal_title = 'Eliminar marca'
        modal_txt = 'eliminar la marca'
        modal_submit = 'eliminar'
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Brand.objects.filter(id=pk).update(
                status = False
            )
            brandName = register_id.name.title()
            messages.success(request, f'La marca {brandName} se eliminó correctamente!')
            return redirect ('brand')
        else:
            form=BrandForm()
    elif modal == 'editar':
        modal_title = 'Editar marca'
        modal_txt = 'editar la marca'
        modal_submit = 'guardar'
        form = BrandForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                brandName = form.cleaned_data.get('name')
                messages.success(request, f'La marca {brandName} se editó correctamente!')
                return redirect ('brand')
        else:
            form=BrandForm(instance=register_id)
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
    return render(request, 'admin/modal-brand.html', context)

############################# PRODUCT ##############################
def product(request):
    location = True
    admin = True
    title_pag = "Producto"
    registers = Product.objects.all()
    # fields = [f.name for f in Subcategory()._meta.get_fields()][2:-1]
    fields = ['name','price','subcategory','brand','expirationDate','unitMeasurement','stock','description','image']
    # print(fields)
    atributes = ['Nombre','Precio','Subcategoría','Fecha de Vencimeinto','Unidad de Medida','Stock','Descripción','Imagen']
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f'El producto {name} se agregó correctamente!')
            return redirect('product')
    else:
        form = ProductForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'fields':fields,
        'atributes':atributes,
        # 'form2':UnitForm(),
        # 'unit':Unit.objects.all()
    }
    return render(request, 'admin/product.html', context)

def productCreatePopup(request):
    location = True
    admin = True
    title_pag = "Producto"
    registers = Product.objects.all()    
    form = ProductForm(request.POST, request.FILES) 

    if form.is_valid():
        instance = form.save()
        name = form.cleaned_data.get('name')
        messages.success(request,f'El producto {name} se agregó correctamente!')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_subcategory");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_product.html", context)

def product_modal(request, modal, pk):
    title_pag = "Producto"
    modal_title = ''
    modal_txt = ''
    location = True
    admin = True
    modal_submit = ''
    url_back="/administracion/producto/"
    registers = Product.objects.all()
    register_id = Product.objects.get(id=pk)
    if modal == 'eliminar':
        modal_title = 'Eliminar producto'
        modal_txt = 'eliminar el producto'
        modal_submit = 'eliminar'
        form = ProductForm(request.POST, request.FILES)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Product.objects.filter(id=pk).update(
                status = False
            )
            productName = register_id.name.title()
            messages.success(request, f'El producto {productName} se eliminó correctamente!')
            return redirect ('product')
        else:
            form=ProductForm()
    elif modal == 'editar':
        modal_title = 'Editar producto'
        modal_txt = 'editar el producto'
        modal_submit = 'guardar'
        form = ProductForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                form.save()
                productName = form.cleaned_data.get('name')
                messages.success(request, f'La producto {productName} se editó correctamente!')
                return redirect ('product')
        else:
            form=ProductForm(instance=register_id)
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
    return render(request, 'admin/modal-product.html', context)

############################# PROVIDER #############################
def provider(request):
    location = True
    admin = True
    title_pag = "Proveedor"
    registers = Provider.objects.all()
    # fields = [f.name for f in Subcategory()._meta.get_fields()][2:-1]
    fields = ['name','phone','email']
    # print(fields)
    atributes = ['Nombre','Celular','Correo Electrónico']
    if request.method == 'POST':
        form = ProviderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request,f'El proveedor {name} se agregó correctamente!')
            return redirect('provider')
    else:
        form = ProviderForm()
    context = {
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
        'fields':fields,
        'atributes':atributes
    }
    return render(request, 'admin/provider.html', context)

def providerCreatePopup(request):
    location = True
    admin = True
    title_pag = "Proveedor"
    registers = Provider.objects.all()    
    form = ProviderForm(request.POST, request.FILES) 

    if form.is_valid():
        instance = form.save()
        name = form.cleaned_data.get('name')
        messages.success(request,f'El proveedor {name} se agregó correctamente!')
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_subcategory");</script>' % (instance.pk, instance))
    context={
        'form':form,
        'title_pag':title_pag,
        'admin':admin,
        'registers': registers,
        'location':location,
    }
    return render(request, "m-forms/m_provider.html", context)

def provider_modal(request, modal, pk):
    title_pag = "Proveedor"
    modal_title = ''
    location = True
    admin = True
    modal_txt = ''
    modal_submit = ''
    url_back="/administracion/proveedor/"
    registers = Provider.objects.all()
    register_id = Provider.objects.get(id=pk)
    if modal == 'eliminar':
        modal_title = 'Eliminar proveedor'
        modal_txt = 'eliminar el proveedor'
        modal_submit = 'eliminar'
        form = ProviderForm(request.POST, request.FILES)
        if request.method == 'POST':
            print('----------------------------------------ELIMINANDO')
            Provider.objects.filter(id=pk).update(
                status = False
            )
            providerName = register_id.name.title()
            messages.success(request, f'El proveedor {providerName} se eliminó correctamente!')
            return redirect ('provider')
        else:
            form=ProviderForm()                  
            
    elif modal == 'editar':
        modal_title = 'Editar proveedor'
        modal_txt = 'editar el proveedor'
        modal_submit = 'guardar'
        form = ProviderForm(request.POST, request.FILES, instance=register_id)
        if request.method == 'POST':
            print('----------------------------------------EDITANDO')                
            if form.is_valid():
                providerName = form.cleaned_data.get('name')
                messages.success(request, f'El proveedor {providerName} se editó correctamente!')
                return redirect ('provider')
        else:
            form=ProviderForm(instance=register_id)
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
    return render(request, 'admin/modal-provider.html', context)
    
################################ USER ##############################
# def user(request, pk):
#     location = True
#     admin = True
#     title_pag = "Usuario"
#     registers = User.objects.all()
#     registers_obj = User.objects.get(id=pk)
#     fields = ['username','email','name','lastName','tDocument','nDocument','phone','dateBirth','user_admin']
#     atributes = ['Username','Correo Electrónico','Nombre','Apellido','Tipo de Documento','Número de Documento','Celular','Fecha de Nacimiento','¿Es administrador?']
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             User.objects.filter(id=pk).update(
#                 email=form.cleaned_data.get('email')
#             )
#             name = form.cleaned_data.get('username')
#             messages.success(request,f'El usuario {name} se agregó correctamente!')
#             return redirect('user')
#     else:
#         form = UserForm()
#     context = {
#         'form':form,
#         'title_pag':title_pag,
#         'admin':admin,
#         'registers': registers,
#         'registers_obj':registers_obj,
#         'location':location,
#         'fields':fields,
#         'atributes':atributes
#     }
#     return render(request, 'admin/user.html', context)
        
    

# def user_modal(request, modal, pk):
#     title_pag = "Usuario"
#     modal_title = ''
#     modal_txt = ''
#     location = True
#     admin = True
#     modal_submit = ''
#     url_back="/administracion/usuario/"
#     registers = User.objects.all()
#     register_id = User.objects.get(id=pk)
#     if modal == 'eliminar':
#         modal_title = 'Eliminar usuario'
#         modal_txt = 'eliminar el usuario'
#         modal_submit = 'eliminar'
#         form = UserForm(request.POST, request.FILES)
#         if request.method == 'POST':
#             print('----------------------------------------ELIMINANDO')
#             User.objects.filter(id=pk).update(
#                 status = False
#             )
#             userName = register_id.username.title()
#             messages.success(request, f'El usuario {userName} se eliminó correctamente!')
#             return redirect ('user')
#         else:
#             form=UserForm()
#     elif modal == 'editar':
#         modal_title = 'Editar usuario'
#         modal_txt = 'editar el usuario'
#         modal_submit = 'guardar'
#         form = UserForm(request.POST, request.FILES, instance=register_id)
#         if request.method == 'POST':
#             print('----------------------------------------EDITANDO')                
#             if form.is_valid():
#                 form.save()
#                 userName = form.cleaned_data.get('username')
#                 messages.success(request, f'El proveedor {userName} se editó correctamente!')
#                 return redirect ('user')
#         else:
#             form=UserForm(instance=register_id)
#     context ={
#         'form':form,
#         'modal_title':modal_title,
#         'modal_txt':modal_txt,
#         'modal_submit':modal_submit,
#         'url_back':url_back,
#         'modal':modal,
#         'register_id':register_id,
#         'title_pag':title_pag,
#         'admin':admin,
#         'registers':registers,
#         'location':location,
#     }
#     return render(request, 'admin/modal-user.html', context)
############################# BACKUP ###############################
def export_data(request):
    date_now = date.today()
    tabla = request.POST['opcion']
    os.system(f"mysqldump --add-drop-table --column-statistics=0 --password=%Brayan2021-2021-2021%# -u root db_elnopal --tables {tabla}> nopal/static/tablas/BKP_{tabla}_{date_now}.sql")
    print('imprimio la tabla ', tabla )
    print('-------------------------------------------------------Hecho')
def import_data(file, request):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LISTO PA´ IMPRIMIR')
    try:
        print('------------------------IMPORTAR')
        url = f'media/{file[1:]}'
        os.system(f"mysql --password=%Brayan2021-2021-2021%# -u root db_elnopal < {url} ")
        print('28288282',url)
        messages.success(request,'su backup fue realizado correctamente')
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><Salio')
    except Exception as err:
        messages.warning(request,f'error {err} ')
        print('error ', err)
def backup(request, tipo):
    title_pag = "Backup"
    location = True
    admin = True
    example_dir = 'nopal/static/tablas/'
    with os.scandir (example_dir) as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file()]
    
    ruta = 'nopal/static/backup'
    with os.scandir(ruta) as bases:
       bases = [base.name for base in bases if base.is_file()]
    
    backups = Backup.objects.all()
    if request.method == 'POST' and tipo== "U":
        print('----------------------------------INTENTO')
        form = BackupForm(request.POST, request.FILES)
        if form.is_valid():
            name= request.POST['name']
            file = request.FILES['file']
            insert = Backup(name=name, file=file)
            import_data(insert.file.url, request)
            insert.save()
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<GUARDÓ')
            return redirect('backup','A')
        else:
            print( ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Error al procesar el formulario")
              
    elif request.method == 'POST' and tipo== "D":
        export_data(request)
        return redirect('backup','A')
    
    else:
        form = BackupForm()
        
    context ={
        "ficheros":ficheros,
        'bases':bases,
        "form":form,
        "backups":backups,
        'title_pag':title_pag,
        'admin':admin,
        'location':location
    }
    return render(request, 'admin/backup.html',context) 

# def unit(request):
#     location = True
#     admin = True
#     title_pag = "Unidad de Medida"
#     registers = Unit.objects.all()
#     if request.method == 'POST':
#         form = UnitForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             name = form.cleaned_data.get('name')
#             messages.success(request,f'La unidad de medida {name} se agregó correctamente!')
#             return redirect('unit')
#     else:
#         form = UnitForm()
#     context = {
#         'form':form,
#         'title_pag':title_pag,
#         'admin':admin,
#         'registers': registers,
#         'location':location,
#     }
#     return render(request, 'admin/unit.html', context)

# def unit_modal(request, modal, pk):
#     location = True
#     admin = True
#     title_pag = "Unidad de Medida"
#     modal_title = ''
#     modal_txt = ''
#     modal_submit = ''
#     url_back="/administracion/unidad_medida/"
#     registers = Unit.objects.all()
#     register_id = Unit.objects.get(id=pk)
    
#     if modal == 'eliminar':
#         modal_title = 'Eliminar unidad de medida'
#         modal_txt = 'eliminar la unidad de medida'
#         modal_submit = 'eliminar'
#         form = UnitForm(request.POST, request.FILES)
#         if request.method == 'POST' :
#             print('----------------------------------------ELIMINANDO')
#             Unit.objects.filter(id=pk).update(
#                 status = False
#             )
#             print('-------------------------------------------------SE ELIMINÓ')
#             unitName = register_id.name.title()
#             messages.success(request, f'La unidad de medida {unitName} se eliminó correctamente!')

#             return redirect ('unit')
#         else:
#             form=UnitForm()
     
#     elif modal == 'editar':
#         modal_title = 'Editar unidad de medida'
#         modal_txt = 'editar la unidad de medida'
#         modal_submit = 'guardar'
#         form = UnitForm(request.POST, request.FILES, instance=register_id)
#         if request.method == 'POST':
#             print('----------------------------------------EDITANDO')                
#             if form.is_valid():
#                 form.save()
#                 unitName = form.cleaned_data.get('name')
#                 messages.success(request, f'La unidad de medida {unitName} se editó correctamente!')
#                 return redirect ('unit')
#         else:
#             form=UnitForm(instance=register_id)
#     context ={
#         'form':form,
#         'modal_title':modal_title,
#         'modal_txt':modal_txt,
#         'modal_submit':modal_submit,
#         'url_back':url_back,
#         'modal':modal,
#         'register_id':register_id,
#         'title_pag':title_pag,
#         'admin':admin,
#         'registers':registers,
#         'location':location
#     }
#     return render(request, 'admin/modal-unit.html', context)

