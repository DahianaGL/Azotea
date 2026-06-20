from django.shortcuts import render, redirect
from Menu.models import Plato
from .models import Reserva

def home(request):
    if request.method == 'POST':
        Reserva.objects.create(
            nombre   = request.POST.get('nombre'),
            telefono = request.POST.get('telefono'),
            fecha    = request.POST.get('fecha'),
            hora     = request.POST.get('hora'),
            personas = request.POST.get('personas'),
            email    = request.POST.get('email'),
            nota     = request.POST.get('nota'),
        )
        return redirect('Home')  # ← redirige y limpia el POST

    platos_destacados = Plato.objects.filter(disponible=True)[:4]
    return render(request, "home/home.html", {
        "platos": platos_destacados,
    })