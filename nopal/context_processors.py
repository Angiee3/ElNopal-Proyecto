from management.models import *
from django.apps import apps



def menu_user(request): 
    MENU_USER_CATEGORIA = Category.objects.all()
    MENU_USER_SUBCATEGORIA = Subcategory.objects.all()
    context={
        'MENU_USER_CATEGORIA': MENU_USER_CATEGORIA,
        'MENU_USER_SUBCATEGORIA': MENU_USER_SUBCATEGORIA,
        }
    # return the value you want as a dictionnary. you may add multiple values in there. 
    return context

def menu_admin(request):
    models= list(map(
        lambda x: x._meta,
        apps.get_models()[6:-5]
        ))
    return {"models":models}
    
def total_carrito(request):
    total = 0
    if "carro" in request.session.keys():
          for key, value in request.session["carro"].items():
            total=total+float(value["precio"])
    return {"total_carrito": total}
