# -*- coding: utf-8 -*-
from django.db import models
from extensiones import extmodels
EDICIONES = ((5, "5ED"),
             (6, "6ED"),
             (7, "7ED"))


class Habilidad(models.Model):
    nombre = models.CharField(max_length=200)
    ingles = models.CharField(max_length=200, blank=True, null=True, default="")
    base = models.CharField(max_length=20, blank=True, null=True, default="")
    extra = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    orden = models.BooleanField(blank=True, default=True)
    modificable = models.BooleanField(blank=True, default=True)
    opciones = models.CharField(max_length=200, blank=True, null=True, default="")
    arma = models.BooleanField(blank=True, default=True)
    descripcion = models.TextField(blank=True, null=True, default="")
    edicion = extmodels.MultiSelectField(max_length=9, blank=True, choices=EDICIONES)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Habilidades"
        app_label = 'cthulhu'


class Ocupacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, default="")
    habilidades = models.ManyToManyField(Habilidad, blank=True, null=True)
    edicion = extmodels.MultiSelectField(max_length=9, blank=True, choices=EDICIONES)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Ocupaciones"
        app_label = 'cthulhu'


class ArmaCC(models.Model):
    nombre = models.CharField(max_length=200)
    probabilidad = models.CharField(max_length=30)
    danio = models.CharField(max_length=30)
    alcance = models.CharField(max_length=20, blank=True, null=True, default="")
    ataques = models.CharField(max_length=20, blank=True, null=True, default="")
    resistencia = models.CharField(max_length=20, blank=True, null=True, default="")
    precio = models.CharField(max_length=20, blank=True, null=True, default="")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Armas de Cuerpo a Cuerpo"
        app_label = 'cthulhu'


class ArmaF(models.Model):
    nombre = models.CharField(max_length=200)
    TIPOS = (
        ("AC", "Arma Corta"),
        ("ES", "Escopeta"),
        ("FU", "Fusil"),
        ("ME", "Metralleta"),
        ("AM", "Ametralladora"),
        ("AP", "Arma Pesada"),
    )
    tipo = models.CharField(max_length=2, choices=TIPOS, default="AC")
    probabilidad = models.CharField(max_length=30)
    danio = models.CharField(max_length=30)
    alcance = models.CharField(max_length=20, blank=True, null=True, default="")
    ataques = models.CharField(max_length=20, blank=True, null=True, default="")
    resistencia = models.CharField(max_length=20, blank=True, null=True, default="")
    precio = models.CharField(max_length=20, blank=True, null=True, default="")
    capacidad = models.CharField(max_length=20, blank=True, null=True, default="")
    defecto = models.CharField(max_length=20, blank=True, null=True, default="")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('tipo',)
        verbose_name_plural = "Armas de Fuego"
        app_label = 'cthulhu'


