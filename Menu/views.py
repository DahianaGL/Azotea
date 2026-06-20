from django.shortcuts import render
from Menu.models import *
# Create your views here.
def menu(request):
    categorias = Categoria.objects.all()
    platos = Plato.objects.filter(disponible=True)
    return render(request, "menu/menu.html", {
        "categorias": categorias,
        "platos": platos
    })

def detalle_plato(request, id):
    plato = Plato.objects.get(id=id)
    return render(request, 'menu/detalle_plato.html', {'plato': plato})
# Create your views here.
