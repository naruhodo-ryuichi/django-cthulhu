# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from cthulhu.models.Personaje import Personaje
from cthulhu.models.reglas import ArmaF, Habilidad, Ocupacion


class TiradasForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = ['FUE', 'DES', 'INT', 'CON', 'APA', 'POD', 'TAM', 'EDU', 'edad']


class ArmasForm(forms.Form):
    armas = forms.ModelMultipleChoiceField(queryset=ArmaF.objects.all(), required=False)


class HabIntForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(HabIntForm, self).__init__(*args, **kwargs)
        habs = Habilidad.objects.all()
        for hab in habs:
            self.fields[hab.nombre.encode("ascii", "ignore")] = forms.IntegerField(max_value=100, min_value=0, initial=hab.base)


class HabProfForm(forms.Form):
    pass


class OcupacionForm(forms.Form):
    ocupaciones = tuple(Ocupacion.objects.all().values_list('id', 'nombre'))
    ocupacion = forms.ChoiceField(choices=ocupaciones)


class PersonalesForm(forms.Form):
    class Meta:
        model = Personaje
        fields = ['nombre', 'jugador', 'ocupacion', 'sexo', 'edad', 'nacimiento', 'residencia', 'retrato']
