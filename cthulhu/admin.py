from cthulhu.models.documentacion import Libro, Aventura
from cthulhu.models.partida import Escena, Escenario
from cthulhu.models.Personaje import Personaje
from cthulhu.models.recursos import Monstruo, PNJ, Localizacion, Hechizo, Lugar, Tomo
from cthulhu.models.reglas import ArmaF, ArmaCC, Ocupacion, Habilidad

__author__ = 'peter'

from django.contrib import admin


class LibroInline(admin.TabularInline):
    model = Libro
    extra = 1


class MonstruoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    fieldsets = [
        (None, {'fields': ['nombre', 'descripcion', 'libro']}),
    ]
    list_display = ('nombre', 'libro')


class MonstruoInline(admin.TabularInline):
    model = Monstruo
    fieldsets = [
        (None, {'fields': ['nombre', 'descripcion', 'libro']}),
    ]
    extra = 1


class HechizoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    fieldsets = [
        (None, {'fields': ['nombre', 'tipo', 'descripcion', 'alias', 'libro']}),
    ]
    list_display = ('nombre', 'libro')


class AventuraAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    filter_horizontal = ('lugares',)
    list_display = ('nombre', 'get_lugares', 'libro')
    save_as = True


class AventuraInline(admin.TabularInline):
    model = Aventura
    fieldsets = [
        (None, {'fields': ['nombre', 'nivel', 'sesiones', 'gancho', 'jugadores', 'libro', 'campania',
                           'sinopsis']}),
    ]
    extra = 1


class PNJInline(admin.TabularInline):
    model = PNJ
    extra = 1


class LocalizacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre', 'tipo', 'lugar')
    inlines = [PNJInline]
    filter_horizontal = ('tomos',)
    list_filter = ('tipo', 'lugar')


class ArmaCCAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'probabilidad', 'danio', 'alcance', 'ataques', 'precio')


class ArmaFAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'tipo', 'probabilidad', 'danio', 'alcance', 'ataques', 'resistencia', 'capacidad', 'defecto',
        'precio')


class LibroAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    inlines = [AventuraInline]
    list_display = ('nombre',)


class TomoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    filter_horizontal = ('hechizos',)
    list_display = ('nombre', 'lengua', 'plus')
    save_as = True


class LocalizacionInline(admin.TabularInline):
    model = Localizacion
    extra = 1


class EscenaInline(admin.TabularInline):
    model = Escena
    extra = 1


class EscenaAdmin(admin.ModelAdmin):
    inlines = [LocalizacionInline, PNJInline]


class EscenarioAdmin(admin.ModelAdmin):
    inlines = [EscenaInline, ]
    filter_horizontal = ('lugares',)


@admin.register(Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre',)
    filter_horizontal = ('habilidades',)


admin.site.register(Aventura, AventuraAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Hechizo, HechizoAdmin)
admin.site.register(Monstruo, MonstruoAdmin)
admin.site.register(ArmaF, ArmaFAdmin)
admin.site.register(ArmaCC, ArmaCCAdmin)
admin.site.register(Localizacion, LocalizacionAdmin)
admin.site.register(Lugar)
admin.site.register(PNJ)
admin.site.register(Escena, EscenaAdmin)
admin.site.register(Escenario, EscenarioAdmin)
admin.site.register(Habilidad)
admin.site.register(Personaje)
admin.site.register(Tomo, TomoAdmin)