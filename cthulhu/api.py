# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tastypie.api import Api
from tastypie.resources import ModelResource
from models import Personaje
__author__ = "naruhodo-ryuichi"


class PersonajeResource(ModelResource):
    class Meta:
        queryset = Personaje.objects.all()
        resource_name = 'personaje'

v1_api = Api(api_name='v1')
v1_api.register(PersonajeResource())
