from django.db import models

# Create your models here.

class Foto(models.Model):
    imagen      = models.ImageField(upload_to='galeria/')
    descripcion = models.CharField(max_length=150, blank=True)
    categoria   = models.CharField(max_length=50, choices=[
        ('ambiente', 'Ambiente'),
        ('platos',   'Platos'),
        ('eventos',  'Eventos'),
    ], default='ambiente')
    fecha       = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'foto'
        verbose_name_plural = 'fotos'
        ordering = ['-fecha']

    def __str__(self):
        return self.descripcion or f"Foto {self.id}" #Para mostrar descripcion de una imagen o no