from django import forms
import re

class ContactoForm(forms.Form):

    ASUNTO_CHOICES = [
        ('', 'Selecciona un asunto'),
        ('Reserva de mesa', 'Reserva de mesa'),
        ('Evento privado', 'Evento privado'),
        ('Catering', 'Catering'),
        ("Chef's Table", "Chef's Table"),
        ('Información general', 'Información general'),
        ('Otro', 'Otro'),
    ]

    nombre = forms.CharField(max_length= 100)
    email = forms.EmailField()
    telefono = forms.CharField(max_length= 20, required= False)
    asunto   = forms.ChoiceField(choices=ASUNTO_CHOICES)
    mensaje = forms.CharField()

    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if telefono: #Solo valida si escribio algo
            patron = r'^(\+57|57|0)?[3][0-9]{9}$'
            if not re.match(patron, telefono.replace(' ', '')):
                raise forms.ValidationError(
                    "Ingresa un numero de telefono colombiano valido. Ejemplo: 3147775965"
                )
        return telefono
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError(
                "Ingrese un correo electrónico válido."
            )
        return email
