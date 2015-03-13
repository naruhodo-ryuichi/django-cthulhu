# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

__author__ = 'peter'


def index(request):
    return render(request, 'index.html')


def ayudas(request):
    return render(request, 'ayudas/ayudas.html')


def nombres(request):
    return render(request, 'ayudas/nombres.html')


def calles(request):
    return render(request, 'ayudas/calles.html')