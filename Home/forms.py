from django import forms
from datetime import date
import re

class ReservaForm(forms.Form):

    nombre = forms.CharField(max_length= 100)
    telefono = forms.CharField(max_length= 20)
    fecha = forms.DateField()
    hora = forms.TimeField()
    personas = forms.ChoiceField(choices=[
        ('1', '1 persona'),
        ('2', '2 personas'),
        ('3', '3 personas'),
        ('4', '4 personas'),
        ('5', '5+ personas'),
    ])
    email = forms.EmailField(required= False)
    nota = forms.CharField(required=False)

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha < date.today():
            raise forms.ValidationError(
                "No puedes reservar en una fecha pasada."
            )
        return fecha
    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        patron = r'^(\+57|57|0)?[3][0-9]{9}$'
        if not re.match(patron, telefono.replace(' ', '')):
            raise forms.ValidationError(
                "Ingresa un numero de telefono colombiano valido. Ejemplo: 3147775965"
            )
        return telefono
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if email and '@' not in email:
            raise forms.ValidationError(
                "Ingrese un correo electrónico válido."
            )
        return email