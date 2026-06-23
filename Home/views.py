from django.shortcuts import render, redirect
from Menu.models import Plato
from .models import Reserva
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def home(request):
    if request.method == 'POST':
            nombre   = request.POST.get('nombre')
            telefono = request.POST.get('telefono')
            fecha    = request.POST.get('fecha')
            hora     = request.POST.get('hora')
            personas = request.POST.get('personas')
            email    = request.POST.get('email')
            nota     = request.POST.get('nota')

            #Guardar la reserva en la base de datos
            Reserva.objects.create(
                nombre = nombre, 
                telefono = telefono, 
                fecha = fecha, 
                hora = hora, 
                personas = personas, 
                email = email, 
                nota = nota, 
            )

            #Si el cliente escribió su email, le enviamos el correo
            if email:
                cuerpo_html = render_to_string('home/correo_confirmacion.html',{
                    'nombre': nombre,
                    'fecha': fecha,
                    'hora': hora,
                    'personas': personas,
                    'nota': nota,
                })
                #Se le envia el correo
                send_mail(
                    subject = 'Confirmacion de reserva - Azotea Rooftop',
                    message = f'Hola {nombre}, tu reserva para el {fecha} a las {hora} fue recibida.',
                    from_email = settings.DEFAULT_FROM_EMAIL,
                    recipient_list = [email],
                    html_message = cuerpo_html,
                    fail_silently = False
                )
            
            if settings.ADMIN_EMAIL_LIST:
                send_mail(
                    subject = f'Nueva reserva de {nombre} - Azotea Rooftop',
                    message = f'''Nueva reserva recibida:
Nombre: {nombre}
Teléfono: {telefono or "No proporcionó"}
Fecha: {fecha}
Hora: {hora}
Personas: {personas}
Email: {email or "No proporcionó"}
Nota: {nota or "No proporcionó"}''',
                        
                    from_email = settings.DEFAULT_FROM_EMAIL,
                    recipient_list = settings.ADMIN_EMAIL_LIST,
                    fail_silently = False
                )

            return redirect('Home')
    
    platos_destacados = Plato.objects.filter(disponible=True)[:4]
    return render(request, "home/home.html",{
        "platos": platos_destacados,
    })        