from django.db import models

from apps.base.models import BaseModel
from apps.equipo.models import Equipo


class Jugador(BaseModel):
    nombre = models.CharField(max_length=55)
    apellido = models.CharField(max_length=55)
    edad = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE) 
    goles = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.equipo}'

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'