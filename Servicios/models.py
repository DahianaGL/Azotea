from django.db import models

class Evento(models.Model):         
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cupos = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'

    def __str__(self):
        return self.titulo
    
    