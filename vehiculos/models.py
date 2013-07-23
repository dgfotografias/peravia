from django.db import models


from datetime import date
year = date.today().year + 1

anio_rango = range(1998, year, 1)

ANIO = ((a,a) for a in anio_rango)

class Tipo(models.Model):
    tipo = models.CharField(max_length=50)


    def __unicode__(self):
        return self.tipo


class Color(models.Model):
    color = models.CharField(max_length=75)


    class Meta:
        verbose_name_plural = 'Colores'

    def __unicode__(self):
        return self.color


class Modelo(models.Model):
    modelo = models.CharField(max_length=75)


    def __unicode__(self):
        return self.modelo

class Marca(models.Model):
    marca = models.CharField(max_length=75)
    variacion = models.CharField(max_length=50, null=True, blank=True)


    def __unicode__(self):
        return self.marca


class Neumatico(models.Model):
    neumatico = models.CharField(max_length=25)


    def __unicode__(self):
        return self.neumatico



class Lubricante(models.Model):
    lubricante = models.CharField(max_length=75)


    def __unicode__(self):
        return self.lubricante


class Bateria(models.Model):
    bateria = models.CharField(max_length=75)

    def __unicode__(self):
        return self.bateria


class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca)
    tipo = models.ForeignKey(Tipo)
    modelo = models.ForeignKey(Modelo)
    anio = models.SmallIntegerField(max_length=4, choices=ANIO)
    color = models.ForeignKey(Color)
    chassis = models.CharField(max_length=150)
    faquisicion = models.DateField(auto_now_add=False, auto_now=False,auto_created=False, verbose_name='Fecha de adquisicion del vehiculo')
    precio_cliente = models.FloatField(max_length=9, verbose_name='Precio otorgado al cliente')
    descuento = models.FloatField(max_length=9,verbose_name='Descuento aplicado (si aplica)', null=True, blank=True)
    #neumatico = models.ManyToManyField(Neumatico, null=True, blank=True, verbose_name='Neumaticos')
    #lubricante = models.ManyToManyField(Lubricante, null=True, blank=True, verbose_name='Lubricantes')
    #bateria = models.ManyToManyField(Bateria, null=True, blank=True, verbose_name='Baterias')
    #tipo_cliente = models.ForeignKey(TipoCliente)

    def __unicode__(self):
        return unicode(self.marca)+' '+unicode(self.modelo)
