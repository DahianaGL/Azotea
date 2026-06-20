from django.contrib import admin
from .models import Contacto
# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'asunto', 'fecha', 'leido') #Mostrar 
    list_filter  = ('leido',) 
    search_fields = ('nombre', 'email', 'asunto') #Buscar
    readonly_fields = ('nombre', 'email', 'telefono', 'asunto', 'mensaje', 'fecha') #Solo lectura

admin.site.register(Contacto, ContactoAdmin)