__author__ = 'Yusdenis'

from django.contrib import  admin

from polls.models import  Encuesta, Pregunta, PosibleRespuesta

class EncuestaAdmin(admin.ModelAdmin):
    list_display = ['etiqueta','texto']
    search_fields = ['etiqueta','texto']
    list_filter = ['etiqueta']

class PosibleRespuestaInline(admin.StackedInline):
    model = PosibleRespuesta
    extra = 1

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ['encuesta','texto','simple','permite_add']
    search_fields = ['encuesta','texto']
    list_filter = ['encuesta','simple','permite_add']
    inlines = [PosibleRespuestaInline]



admin.site.register(Encuesta,EncuestaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)