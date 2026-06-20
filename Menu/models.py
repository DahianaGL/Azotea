from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255, blank=True)
    icono = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='platos/', blank=True, null=True)
    #Relacion
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'plato'
        verbose_name_plural = 'platos'

    def __str__(self):
        return self.nombre