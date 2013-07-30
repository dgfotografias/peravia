# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OpcionElegida'
        db.create_table(u'polls_opcionelegida', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('elegida', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.PosibleRespuesta'])),
            ('respuesta', self.gf('django.db.models.fields.related.ForeignKey')(related_name='elegidas', to=orm['polls.Respuesta'])),
        ))
        db.send_create_signal(u'polls', ['OpcionElegida'])

        # Adding model 'Respuesta'
        db.create_table(u'polls_respuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(related_name='respuestas', to=orm['polls.Pregunta'])),
        ))
        db.send_create_signal(u'polls', ['Respuesta'])


    def backwards(self, orm):
        # Deleting model 'OpcionElegida'
        db.delete_table(u'polls_opcionelegida')

        # Deleting model 'Respuesta'
        db.delete_table(u'polls_respuesta')


    models = {
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'respuestas'", 'to': u"orm['polls.Pregunta']"}),
            'texto': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['polls']