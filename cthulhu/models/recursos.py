# -*- coding: utf-8 -*-
from cthulhu.models.documentacion import Aventura, Libro
from django.db import models
from cthulhu.models.partida import Escena


class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, default="")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Lugares"
        app_label = 'cthulhu'


class Localizacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, default="")
    lugar = models.ForeignKey(Lugar, blank=True, null=True)
    escena = models.ForeignKey(Escena, blank=True, null=True)
    TIPOS = (
        ("BI", "Biblioteca"),
        ("HO", "Hospital"),
        ("PE", "Periódico"),
        ("PO", "Policía"),
        ("RE", "Residencia"),
        ("NE", "Negocio"),
        ("DI", "Distrito"),
        ("OT", "Otros"),
        ("UN", "Universidad"),
    )
    tipo = models.CharField(max_length=2, choices=TIPOS, default="OT")
    tomos = models.ManyToManyField('Tomo', null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        verbose_name_plural = "Localizaciones"
        app_label = 'cthulhu'


class PNJ(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, default="")
    localizacion = models.ForeignKey(Localizacion, blank=True, null=True)
    aventura = models.ForeignKey(Aventura, blank=True, null=True)
    escena = models.ForeignKey(Escena, blank=True, null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Tomo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True, default="")
    lengua = models.CharField(max_length=20, blank=True, null=True, default="")
    autor = models.CharField(max_length=200, blank=True, null=True, default="")
    semanas = models.CharField(max_length=20, blank=True, null=True, default="")
    COR = models.CharField(max_length=20, blank=True, null=True, default="")
    plus = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    relato = models.CharField(max_length=200, blank=True, null=True, default="")
    hechizos = models.ManyToManyField('Hechizo', null=True, blank=True)
    apariencia = models.TextField(blank=True, null=True, default="")
    ojear = models.TextField(blank=True, null=True, default="")
    investigar = models.TextField(blank=True, null=True, default="")
    leer = models.TextField(blank=True, null=True, default="")
    citas = models.TextField(blank=True, null=True, default="")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Monstruo(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    libro = models.ForeignKey(Libro, blank=True, null=True)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'


class Hechizo(models.Model):
    nombre = models.CharField(max_length=200, blank=True)
    libro = models.ForeignKey(Libro, blank=True, null=True)
    descripcion = models.TextField(blank=True)
    alias = models.TextField(blank=True, null=True)
    TIPOS = (
        ("GE", "General"),
        ("CA", "Convocación/Atadura"),
        ("CD", "Contactar con Dios"),
        ("CO", "Contacto"),
        ("EN", "Encantamiento"),
        ("LE", "Llamada/Expulsión"),
    )
    tipo = models.CharField(max_length=2, choices=TIPOS, default="GE")

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ('nombre',)
        app_label = 'cthulhu'