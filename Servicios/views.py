from django.shortcuts import render
from Servicios.models import Evento
# Create your views here.
def servicios(request):
    eventos = Evento.objects.filter(activo=True) 
    return render(request, "servicios/servicios.html", {"eventos": eventos})
