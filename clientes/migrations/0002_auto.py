# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field vehiculos on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_vehiculos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('vehiculo', models.ForeignKey(orm[u'vehiculos.vehiculo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'vehiculo_id'])


    def backwards(self, orm):
        # Removing M2M table for field vehiculos on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_vehiculos'))


    models = {
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bateria_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vehiculos.Bateria']", 'null': 'True', 'blank': 'True'}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'celular': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['provincias.Ciudad']"}),
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cliente_tipo'", 'to': u"orm['clientes.TipoCliente']"}),
            'codigo_postal': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['provincias.CodigoPostal']"}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'dni': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empresa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ext': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fnacimiento': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['idiomas.Idioma']"}),
            'lubricante_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vehiculos.Lubricante']", 'null': 'True', 'blank': 'True'}),
            'neumatico_cliente': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['vehiculos.Neumatico']", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'rnc': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'sector': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['provincias.Sector']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': "'6'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipo_dni': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vehiculos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['vehiculos.Vehiculo']", 'symmetrical': 'False'})
        },
        u'clientes.tipocliente': {
            'Meta': {'object_name': 'TipoCliente'},
            'cliente': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'idiomas.idioma': {
            'Meta': {'object_name': 'Idioma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
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
        },
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

    complete_apps = ['clientes']