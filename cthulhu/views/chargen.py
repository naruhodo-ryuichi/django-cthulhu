# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
import unicodedata
from cthulhu.models.reglas import Ocupacion


TEMPLATES = {"tiradas": "chargen/tiradas.html",
             "ocupacion": "chargen/ocupacion.html",
             "armas": "chargen/armas.html",
             "habprof": "chargen/habprof.html",
             "habint": "chargen/habint.html",
             "personales": "chargen/personales.html"
            }


class PersonajeWizard(SessionWizardView):

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form(self, step=None, data=None, files=None):
        form = super(PersonajeWizard, self).get_form(step, data, files)
        # Intento de corregir los acentos sin exito
        # step = step or self.steps.current
        # if step == 'habprof' or step == 'habint':
        #     step_0_data = self.storage.get_step_data('ocupacion')
        #     habsprof = Ocupacion.objects.get(pk=step_0_data.get('ocupacion-ocupacion')).habilidades
        #     for habilidad in habsprof.all():
        #         if type(habilidad) == str:
        #             nombrelimpio = unicodedata.normalize('NFKD', habilidad.nombre.encode('ascii', 'xmlcharrefreplace'))
        #         else:
        #             nombrelimpio = habilidad
        #         print habilidad, nombrelimpio
        #         form.fields[nombrelimpio] = forms.IntegerField(max_value=100, min_value=0, initial=habilidad.base)
        return form

    def done(self, form_list, **kwargs):
        return render_to_response('chargen/done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })