# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Encuesta'
        db.create_table(u'polls_encuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('etiqueta', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'polls', ['Encuesta'])

        # Adding model 'Pregunta'
        db.create_table(u'polls_pregunta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
            ('simple', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('permite_add', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Encuesta'])),
        ))
        db.send_create_signal(u'polls', ['Pregunta'])

        # Adding model 'PosibleRespuesta'
        db.create_table(u'polls_posiblerespuesta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('texto', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['polls.Pregunta'])),
        ))
        db.send_create_signal(u'polls', ['PosibleRespuesta'])


    def backwards(self, orm):
        # Deleting model 'Encuesta'
        db.delete_table(u'polls_encuesta')

        # Deleting model 'Pregunta'
        db.delete_table(u'polls_pregunta')

        # Deleting model 'PosibleRespuesta'
        db.delete_table(u'polls_posiblerespuesta')


    models = {
        u'polls.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'etiqueta': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        u'polls.posiblerespuesta': {
            'Meta': {'object_name': 'PosibleRespuesta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Pregunta']"}),
            'texto': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'polls.pregunta': {
            'Meta': {'object_name': 'Pregunta'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Encuesta']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permite_add': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'simple': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['polls']