from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre    = models.CharField(max_length=100)
    email     = models.EmailField()
    telefono  = models.CharField(max_length=20, blank=True)
    asunto    = models.CharField(max_length=150)
    mensaje   = models.TextField()
    fecha     = models.DateTimeField(auto_now_add=True)
    leido     = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'mensaje'
        verbose_name_plural = 'mensajes'

    def __str__(self):
        return f"{self.nombre} — {self.asunto}" # define como se representa el objeto, cuando Django necesita mostar como Texto simple en el admin