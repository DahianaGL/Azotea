from django.contrib import admin
from .models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha', 'cupos', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo',)

admin.site.register(Evento, EventoAdmin)
