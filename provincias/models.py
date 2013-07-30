from django.db import models

class Ciudad(models.Model):
    ciudad = models.CharField(max_length=75, unique=True)


    class Meta:
        verbose_name_plural = 'Ciudades'


    def __unicode__(self):
        return unicode(self.ciudad)



class Sector(models.Model):
    provincia = models.ForeignKey(Ciudad)
    sector = models.CharField(max_length=150)

    class Meta:
        unique_together = (('provincia','sector')
        )

    def __unicode__(self):
        return unicode(self.sector)


class CodigoPostal(models.Model):
    sector = models.ForeignKey(Sector)
    codigo_postal = models.CharField(max_length=10)


    class Meta:
        verbose_name_plural = 'Codigo Postales'


    def __unicode__(self):
        return unicode(self.codigo_postal)
