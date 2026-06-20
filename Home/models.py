from django.db import models

class Reserva(models.Model):
    PERSONAS_CHOICES = [
        ('1', '1 persona'),
        ('2', '2 personas'),
        ('3', '3 personas'),
        ('4', '4 personas'),
        ('5', '5+ personas'),
    ]

    nombre   = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    fecha    = models.DateField()
    hora     = models.TimeField()
    personas = models.CharField(max_length=2, choices=PERSONAS_CHOICES, default='2')
    email    = models.EmailField(blank=True)
    nota     = models.TextField(blank=True)
    creado   = models.DateTimeField(auto_now_add=True)
    confirmada = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'reserva'
        verbose_name_plural = 'reservas'
        
    def __str__(self):
        return f"{self.nombre} — {self.fecha} {self.hora} ({self.personas} personas)"