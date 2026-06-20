from django.contrib import admin
from Blog.models import Foto
# Register your models here.

class FotoAdmin(admin.ModelAdmin):
    list_display  = ('id', 'descripcion', 'categoria', 'fecha')
    list_filter   = ('categoria',)
    readonly_fields = ('fecha', 'id')

admin.site.register(Foto, FotoAdmin)