from django.db import models
from django.utils import  timezone
from django.contrib.auth.models import User
from clientes.models import Cliente

class Encuesta(models.Model):
    etiqueta = models.CharField(max_length=100)
    texto = models.TextField(blank=False)
    def __unicode__(self):
        return self.etiqueta
    class Meta:
        verbose_name= 'Encuesta'
        verbose_name_plural = 'Encuestas'

class Pregunta(models.Model):
    texto = models.TextField(blank=False)
    # Una pregunta es simple cuando la seleccion es de una sola respuesta
    simple = models.BooleanField(default=True)
    # Permite_add es para si en la parte de abajo de la pregunta se puede escribir
    permite_add = models.BooleanField(default=False)
    encuesta = models.ForeignKey(Encuesta, related_name='preguntas')

    def __unicode__(self):
        return  unicode(self.encuesta)+' - '+ self.texto

    class Meta:
        verbose_name= 'Pregunta'
        verbose_name_plural = 'Preguntas'


class PosibleRespuesta(models.Model):
    texto = models.CharField(max_length=250, blank=False, null= False)
    pregunta = models.ForeignKey(Pregunta, related_name='posibles')
    def __unicode__(self):
        return self.texto

class Respuesta(models.Model):
    texto = models.TextField(blank=True, null=True)
    pregunta = models.ForeignKey(Pregunta, related_name='respuestas')
    encuesta = models.ForeignKey(Encuesta, null=True)
    user = models.ForeignKey(User, null= True, blank=True)
    cliente = models.ForeignKey(Cliente, null= True)
    creada = models.DateTimeField(auto_now=True, default = timezone.now())


class OpcionElegida(models.Model):
    elegida = models.ForeignKey(PosibleRespuesta)
    respuesta = models.ForeignKey(Respuesta, related_name='elegidas')






