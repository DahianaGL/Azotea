from django.shortcuts import render
from django.core.paginator import Paginator
from Menu.models import *

def menu(request):
    categorias = Categoria.objects.all()
    
    # Leer la categoría seleccionada de la URL (?categoria=1)
    categoria_id = request.GET.get('categoria', None)
    
    if categoria_id:
        platos = Plato.objects.filter(disponible=True, categoria__id=categoria_id)
    else:
        platos = Plato.objects.filter(disponible=True)

    # Paginación — máximo 6 platos por página
    paginator = Paginator(platos, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "menu/menu.html", {
        "categorias": categorias,
        "platos": page_obj,
        "page_obj": page_obj,
        "categoria_id": categoria_id,  # para saber qué filtro está activo
    })

def detalle_plato(request, id):
    plato = Plato.objects.get(id=id)
    return render(request, 'menu/detalle_plato.html', {'plato': plato})