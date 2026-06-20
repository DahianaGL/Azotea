from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'telefono', 'fecha', 'hora', 'personas', 'email', 'confirmada', 'creado')
    list_filter   = ('confirmada', 'fecha', 'personas')
    search_fields = ('nombre', 'email', 'telefono')
    readonly_fields = ('creado',)
    list_editable = ('confirmada',)

admin.site.register(Reserva, ReservaAdmin)