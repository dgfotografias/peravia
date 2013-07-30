# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tipo'
        db.create_table(u'vehiculos_tipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'vehiculos', ['Tipo'])

        # Adding model 'Color'
        db.create_table(u'vehiculos_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'vehiculos', ['Color'])

        # Adding model 'Modelo'
        db.create_table(u'vehiculos_modelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'vehiculos', ['Modelo'])

        # Adding model 'Marca'
        db.create_table(u'vehiculos_marca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('variacion', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'vehiculos', ['Marca'])

        # Adding model 'Neumatico'
        db.create_table(u'vehiculos_neumatico', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('neumatico', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'vehiculos', ['Neumatico'])

        # Adding model 'Lubricante'
        db.create_table(u'vehiculos_lubricante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lubricante', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'vehiculos', ['Lubricante'])

        # Adding model 'Bateria'
        db.create_table(u'vehiculos_bateria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bateria', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'vehiculos', ['Bateria'])

        # Adding model 'Vehiculo'
        db.create_table(u'vehiculos_vehiculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiculos.Marca'])),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiculos.Tipo'])),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiculos.Modelo'])),
            ('anio', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4)),
            ('color', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['vehiculos.Color'])),
            ('chassis', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('faquisicion', self.gf('django.db.models.fields.DateField')()),
            ('precio_cliente', self.gf('django.db.models.fields.FloatField')(max_length=9)),
            ('descuento', self.gf('django.db.models.fields.FloatField')(max_length=9, null=True, blank=True)),
        ))
        db.send_create_signal(u'vehiculos', ['Vehiculo'])


    def backwards(self, orm):
        # Deleting model 'Tipo'
        db.delete_table(u'vehiculos_tipo')

        # Deleting model 'Color'
        db.delete_table(u'vehiculos_color')

        # Deleting model 'Modelo'
        db.delete_table(u'vehiculos_modelo')

        # Deleting model 'Marca'
        db.delete_table(u'vehiculos_marca')

        # Deleting model 'Neumatico'
        db.delete_table(u'vehiculos_neumatico')

        # Deleting model 'Lubricante'
        db.delete_table(u'vehiculos_lubricante')

        # Deleting model 'Bateria'
        db.delete_table(u'vehiculos_bateria')

        # Deleting model 'Vehiculo'
        db.delete_table(u'vehiculos_vehiculo')


    models = {
        u'vehiculos.bateria': {
            'Meta': {'object_name': 'Bateria'},
            'bateria': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'vehiculos.color': {
            'Meta': {'object_name': 'Color'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'vehiculos.lubricante': {
            'Meta': {'object_name': 'Lubricante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lubricante': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'vehiculos.marca': {
            'Meta': {'object_name': 'Marca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'variacion': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'vehiculos.modelo': {
            'Meta': {'object_name': 'Modelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'vehiculos.neumatico': {
            'Meta': {'object_name': 'Neumatico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neumatico': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'vehiculos.tipo': {
            'Meta': {'object_name': 'Tipo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'vehiculos.vehiculo': {
            'Meta': {'object_name': 'Vehiculo'},
            'anio': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4'}),
            'chassis': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'color': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehiculos.Color']"}),
            'descuento': ('django.db.models.fields.FloatField', [], {'max_length': '9', 'null': 'True', 'blank': 'True'}),
            'faquisicion': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehiculos.Marca']"}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehiculos.Modelo']"}),
            'precio_cliente': ('django.db.models.fields.FloatField', [], {'max_length': '9'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['vehiculos.Tipo']"})
        }
    }

    complete_apps = ['vehiculos']