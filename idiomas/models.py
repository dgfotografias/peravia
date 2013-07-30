from django.db import models


class Idioma(models.Model):
    idioma = models.CharField(max_length=75, unique=True)


    def __unicode__(self):
        return unicode(self.idioma)


