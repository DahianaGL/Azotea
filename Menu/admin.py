from django.contrib import admin
from .models import *
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'icono')
    search_fields = ('nombre',)

class PlatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'disponible', 'creado')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)
    readonly_fields = ('creado', 'id')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Plato, PlatoAdmin)