from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView, RedirectView
from cthulhu.forms.chargenForms import TiradasForm, OcupacionForm, ArmasForm, HabProfForm, HabIntForm, PersonalesForm
from cthulhu.views import estandar, escenarios
from cthulhu.views.chargen import PersonajeWizard
from cthulhu.api import v1_api
from django.contrib import admin

FORMS = [
    ("tiradas", TiradasForm),
    ("ocupacion", OcupacionForm),
    ("armas", ArmasForm),
    ("habprof", HabProfForm),
    ("habint", HabIntForm),
    ("personales", PersonalesForm)
]

urlpatterns = patterns(
    '',
    url(r'^api', include(v1_api.urls)),
    url(r'^ayudas/nombres$', 'cthulhu.views.estandar.nombres'),
    url(r'^ayudas/calles$', 'cthulhu.views.estandar.calles'),
    url(r'^ayudas$', TemplateView.as_view(template_name='ayudas/ayudas.html')),
    #url(r'^chargen/importar$', 'cthulhu.views.chargen.importar'),
    url(r'^chargen', PersonajeWizard.as_view(FORMS)),
    url(r'^escenarios/escenario/(?P<id>[\d]+)$', 'cthulhu.views.escenarios.escenario'),
    url(r'^escenarios/importar$', 'cthulhu.views.escenarios.importar'),
    #url(r'^escenarios/$', 'cthulhu.views.escenarios.escenarios'),
    url(r'^escenarios', escenarios.escenarios),
    url(r'^$', estandar.index, name='index'),
    #url(r'^$', 'cthulhu.views.estandar.index'),
)

