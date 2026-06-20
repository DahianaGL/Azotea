from django.shortcuts import render,redirect
from Contacto.models import Contacto
# Create your views here.
def contacto(request):
    if request.method == 'POST':
        nombre  = request.POST.get('nombre')
        email   = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto  = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        Contacto.objects.create(
            nombre   = nombre,
            email    = email,
            telefono = telefono,
            asunto   = asunto,
            mensaje  = mensaje
        )
        return redirect('Contacto')  

    return render(request, "contacto/contacto.html")