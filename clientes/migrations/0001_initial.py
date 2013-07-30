# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoCliente'
        db.create_table(u'clientes_tipocliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['TipoCliente'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cliente_tipo', to=orm['clientes.TipoCliente'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fnacimiento', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length='6')),
            ('tipo_dni', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('dni', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('idioma', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['idiomas.Idioma'])),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('ext', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4, null=True, blank=True)),
            ('celular', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pais', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('ciudad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['provincias.Ciudad'])),
            ('sector', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['provincias.Sector'])),
            ('codigo_postal', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['provincias.CodigoPostal'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('empresa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('rnc', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding M2M table for field neumatico_cliente on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_neumatico_cliente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('neumatico', models.ForeignKey(orm[u'vehiculos.neumatico'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'neumatico_id'])

        # Adding M2M table for field lubricante_cliente on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_lubricante_cliente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('lubricante', models.ForeignKey(orm[u'vehiculos.lubricante'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'lubricante_id'])

        # Adding M2M table for field bateria_cliente on 'Cliente'
        m2m_table_name = db.shorten_name(u'clientes_cliente_bateria_cliente')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('bateria', models.ForeignKey(orm[u'vehiculos.bateria'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cliente_id', 'bateria_id'])


    def backwards(self, orm):
        # Deleting model 'TipoCliente'
        db.delete_table(u'clientes_tipocliente')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Removing M2M table for field neumatico_cliente on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_neumatico_cliente'))

        # Removing M2M table for field lubricante_cliente on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_lubricante_cliente'))

        # Removing M2M table for field bateria_cliente on 'Cliente'
        db.delete_table(db.shorten_name(u'clientes_cliente_bateria_cliente'))


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
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'vehiculos.lubricante': {
            'Meta': {'object_name': 'Lubricante'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lubricante': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'vehiculos.neumatico': {
            'Meta': {'object_name': 'Neumatico'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'neumatico': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['clientes']