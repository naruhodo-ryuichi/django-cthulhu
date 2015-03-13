# -*- coding: utf-8 -*-
from django.db import models


class Escena(models.Model):
    nombre = models.CharField(max_length=200)
    contenido = models.TextField(blank=True)
    escenario = models.ForeignKey('Escenario')
    localizaciones = models.ManyToManyField('Localizacion', blank=True, null=True, related_name='Acontecimiento+')
    pnjs = models.ManyToManyField('PNJ', blank=True, null=True, related_name='Actores+')

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Escenario(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    lugares = models.ManyToManyField('Lugar', blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Actores(models.Model):
    escena = models.ForeignKey(Escena)
    pnj = models.ForeignKey('PNJ')
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'cthulhu'


class Acontecimiento(models.Model):
    escena = models.ForeignKey(Escena)
    localizacion = models.ForeignKey('Localizacion')
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        app_label = 'cthulhu'
