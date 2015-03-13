# -*- coding: utf-8 -*-
from django.db import models


class Aventura(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    sinopsis = models.TextField(blank=True)
    gancho = models.CharField(max_length=200, blank=True)
    NIVELES = (
        ("PR", "Principiante"),
        ("IN", "Intermedio"),
        ("EX", "Experto"),
        ("DE", "Desconocido"),
    )
    nivel = models.CharField(max_length=2, choices=NIVELES, default="DE")
    campania = models.CharField(max_length=200, blank=True)
    sesiones = models.CharField(max_length=200, blank=True)
    jugadores = models.CharField(max_length=4, blank=True)
    libro = models.ForeignKey('Libro', blank=True, null=True)
    lugares = models.ManyToManyField('Lugar', blank=True, null=True)

    def get_lugares(self):
        return "\n".join([s.nombre for s in self.lugares.all()])

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    IDIOMAS = (
        ("ES", "Español"),
        ("EN", "Inglés"),
    )
    idioma = models.CharField(max_length=2, choices=IDIOMAS, default="ES")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'
