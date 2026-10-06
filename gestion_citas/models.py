from django.db import models


class Cita(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('confirmada', 'Confirmada'),
            ('cancelada', 'Cancelada'),
        ],
        default='pendiente',
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha} {self.hora}"























