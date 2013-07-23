from django.db import models
from clientes.models import Cliente


class ToDo(models.Model):
    cliente = models.ForeignKey(Cliente,  null= True, blank=True)
    creado = models.DateTimeField(editable=False, auto_now=True)
    fecha = models.DateField(auto_now=False, verbose_name='Fecha')
    titulo = models.CharField(max_length=250, default='')
    description = models.TextField(null=True, blank=True, default='')
    finalizada = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Tareas'
        verbose_name = 'tarea'

    def __unicode__(self):
        return self.title


