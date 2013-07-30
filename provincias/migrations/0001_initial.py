# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciudad'
        db.create_table(u'provincias_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciudad', self.gf('django.db.models.fields.CharField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'provincias', ['Ciudad'])

        # Adding model 'Sector'
        db.create_table(u'provincias_sector', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['provincias.Ciudad'])),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'provincias', ['Sector'])

        # Adding unique constraint on 'Sector', fields ['provincia', 'sector']
        db.create_unique(u'provincias_sector', ['provincia_id', 'sector'])

        # Adding model 'CodigoPostal'
        db.create_table(u'provincias_codigopostal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['provincias.Sector'])),
            ('codigo_postal', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'provincias', ['CodigoPostal'])


    def backwards(self, orm):
        # Removing unique constraint on 'Sector', fields ['provincia', 'sector']
        db.delete_unique(u'provincias_sector', ['provincia_id', 'sector'])

        # Deleting model 'Ciudad'
        db.delete_table(u'provincias_ciudad')

        # Deleting model 'Sector'
        db.delete_table(u'provincias_sector')

        # Deleting model 'CodigoPostal'
        db.delete_table(u'provincias_codigopostal')


    models = {
        u'provincias.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'ciudad': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'provincias.codigopostal': {
            'Meta': {'object_name': 'CodigoPostal'},
            'codigo_postal': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['provincias.Sector']"})
        },
        u'provincias.sector': {
            'Meta': {'unique_together': "(('provincia', 'sector'),)", 'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['provincias.Ciudad']"}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['provincias']