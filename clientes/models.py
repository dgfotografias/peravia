from django.db import models
from django_countries import CountryField
from vehiculos.models import Neumatico, Bateria, Lubricante, Vehiculo
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey,GroupedForeignKey
from provincias.models import Ciudad, Sector, CodigoPostal
from idiomas.models import Idioma

TITULO = (('Sr.','Sr.'),('Sra.','Sra.'),('Srta.','Srta.'))
SEXO = (('Mujer','Mujer'),('Hombre','Hombre'))


class TipoCliente(models.Model):
    cliente = models.CharField(max_length=100, verbose_name='Tipo de cliente', unique=True)
    fecha   = models.DateTimeField(auto_now_add=True, editable=False, null=False,blank=False)

    def __unicode__(self):
        return unicode(self.cliente)


PAIS = (('Do','Republica Dominicana'),)
TIPO_DNI = (('Cedula','Cedula'),('Pasaporte','Pasaporte'))

class Observaciones(models.Model):
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.descripcion

class Cliente(models.Model):
    cliente = models.ForeignKey(TipoCliente, related_name='cliente_tipo')

    neumatico_cliente = models.ManyToManyField(Neumatico, verbose_name='Neumaticos', null=True, blank=True)
    lubricante_cliente = models.ManyToManyField(Lubricante, verbose_name='Lubricantes', null=True, blank=True)
    bateria_cliente = models.ManyToManyField(Bateria, verbose_name='Baterias', null=True, blank=True)


    titulo  = models.CharField(choices=TITULO, max_length=200)
    nombre  = models.CharField(max_length=75, verbose_name='Nombre(s)')
    apellidos = models.CharField(max_length=100, verbose_name='Apellido(s)')
    fnacimiento = models.CharField(max_length=10, verbose_name='Fecha de Nacimiento')
    sexo = models.CharField(choices=SEXO, max_length='6')
    tipo_dni = models.CharField(max_length=11, choices=TIPO_DNI, verbose_name='Tipo de Documento')
    dni = models.CharField(max_length=15, verbose_name='Documento de Identidad')
    idioma = models.ForeignKey(Idioma)
    telefono = models.CharField(max_length=15)
    ext = models.SmallIntegerField(max_length=4, null=True, blank=True)
    celular = models.CharField(max_length=15)
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=75, choices=PAIS)

    ciudad = models.ForeignKey(Ciudad)

    sector = ChainedForeignKey(Sector,
                                        chained_field="ciudad",
                                        chained_model_field="provincia",
                                        show_all=False,
                                        auto_choose=True)

    codigo_postal = ChainedForeignKey(CodigoPostal,
                                        chained_field="sector",
                                        chained_model_field="sector",
                                        show_all=False,
                                        auto_choose=True)




    email = models.EmailField(verbose_name='Correo Electronico')
    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    rnc = models.CharField(max_length=25, null=True, blank=True)
    fecha   = models.DateTimeField(auto_now_add=True, editable=False, null=False,blank=False)
    vehiculos = models.ManyToManyField(Vehiculo)

    observaciones = models.ForeignKey(Observaciones, null=True)

    def get_name(self):
        return unicode('%s %s' % (self.nombre, self.apellidos))

    def __unicode__(self):
        return unicode('%s %s' % (self.nombre, self.apellidos))

    def get_id(self):
            return (self.pk)
    get_id.short_description = 'ID'






"""
class ExtraInfoCliente(models.Model):
    #vehiculo = models.ForeignKey(Vehiculo, related_name='vehiculo_extra_info')
    cliente = models.ForeignKey(Cliente,blank=True,null=True, related_name='cliente_extra_info')
    #tipo_cliente = models.ForeignKey(TipoCliente, blank=True, null=True, related_name='tipo_de_cliente')
    neumatico_cliente = models.ManyToManyField(Neumatico, verbose_name='Neumaticos', null=True, blank=True)
    lubricante_cliente = models.ManyToManyField(Lubricante, verbose_name='Lubricantes', null=True, blank=True)
    bateria_cliente = models.ManyToManyField(Bateria, verbose_name='Baterias', null=True, blank=True)


    def __unicode__(self):
        return unicode('%s %s' %(self.cliente, self.tipo_cliente))
"""