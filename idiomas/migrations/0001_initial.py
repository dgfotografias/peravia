# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Idioma'
        db.create_table(u'idiomas_idioma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idioma', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'idiomas', ['Idioma'])


    def backwards(self, orm):
        # Deleting model 'Idioma'
        db.delete_table(u'idiomas_idioma')


    models = {
        u'idiomas.idioma': {
            'Meta': {'object_name': 'Idioma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        }
    }

    complete_apps = ['idiomas']