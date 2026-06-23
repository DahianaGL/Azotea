from django.shortcuts import render,redirect
from Contacto.models import Contacto
from django.core.mail import send_mail
from django.conf import settings
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

        # Notificación al admin cuando llega un mensaje de contacto
        if settings.ADMIN_EMAIL_LIST:
            send_mail(
                subject = f'Nuevo mensaje de contacto de {nombre} - Azotea',
                message = f'''Nuevo mensaje de contacto recibido:
Nombre: {nombre}
Email: {email or "No proporcionó"}
Teléfono: {telefono or "No proporcionó"}
Asunto: {asunto}
Mensaje: {mensaje}''',

                from_email = settings.DEFAULT_FROM_EMAIL,
                recipient_list = settings.ADMIN_EMAIL_LIST,
                fail_silently = False,
            )
        return redirect('Contacto')  

    return render(request, "contacto/contacto.html")