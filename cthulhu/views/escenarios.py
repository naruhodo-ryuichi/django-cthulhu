# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from cthulhu.models.partida import Escenario


def escenario(request, id):
    escenario = Escenario.objects.get(pk=id)
    return render(request, 'escenarios/escenario.html', {'escenario': escenario})


def importar(request):
    return render(request, 'escenarios/importar.html')


def escenarios(request):
    escenarios = Escenario.objects.all()
    return render(request, 'escenarios/escenarios.html', {'escenarios': escenarios})