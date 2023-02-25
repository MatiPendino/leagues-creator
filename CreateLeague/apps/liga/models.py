from django.contrib.auth.models import User
from django.db import models

from apps.base.models import BaseModel


class Liga(BaseModel):
    LIGUILLA = 0
    ELIMINACION_DIRECTA = 1
    COPA = 2
    formatos_competencia = (
        (LIGUILLA, "LIGUILLA"),
        (ELIMINACION_DIRECTA, "ELIMINACIÓN DIRECTA"),
        (COPA, "COPA")
    )

    nombre = models.CharField(max_length=100)
    cantidad_equipos = models.IntegerField(default=0, blank=True)
    formato = models.IntegerField(default=0, choices=formatos_competencia)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Liga'
        verbose_name_plural = 'Ligas'