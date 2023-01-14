from django.db import models

from apps.liga.models import Liga


class Equipo(models.Model):
    nombre = models.CharField(max_length=55)
    jugados = models.IntegerField(default=0)
    ganados = models.IntegerField(default=0)
    empatados = models.IntegerField(default=0)
    perdidos = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)

    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, default=1)

    def set_puntos(self, ganados, empatados):
        self.puntos = ganados*3 + empatados

    def set_diferencia_goles(self, goles_favor, goles_en_contra):
        self.diferencia_goles = goles_favor - goles_en_contra

    def set_liga(self, liga):
        self.liga = liga

    def __str__(self):
        return self.nombre
