# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Respuesta.encuesta'
        db.add_column(u'polls_respuesta', 'encuesta',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Encuesta'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Respuesta.encuesta'
        db.delete_column(u'polls_respuesta', 'encuesta_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'observaciones': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Observaciones']", 'null': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'rnc': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'sector': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['provincias.Sector']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': "'6'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tipo_dni': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vehiculos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['vehiculos.Vehiculo']", 'symmetrical': 'False'})
        },
        u'clientes.observaciones': {
            'Meta': {'object_name': 'Observaciones'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'clientes.tipocliente': {
            'Meta': {'object_name': 'TipoCliente'},
            'cliente': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'idiomas.idioma': {
            'Meta': {'object_name': 'Idioma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idioma': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '75'})
        },
        u'polls.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'etiqueta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        u'polls.opcionelegida': {
            'Meta': {'object_name': 'OpcionElegida'},
            'elegida': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.PosibleRespuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'respuesta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'elegidas'", 'to': u"orm['polls.Respuesta']"})
        },
        u'polls.posiblerespuesta': {
            'Meta': {'object_name': 'PosibleRespuesta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posibles'", 'to': u"orm['polls.Pregunta']"}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'polls.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permite_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'simple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        u'polls.respuesta': {
            'Meta': {'object_name': 'Respuesta'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Cliente']", 'null': 'True'}),
            'creada': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 7, 19, 0, 0)', 'auto_now': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Encuesta']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'respuestas'", 'to': u"orm['polls.Pregunta']"}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['polls']