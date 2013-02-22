# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Choice'
        db.create_table('poll_choice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Poll'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('poll', ['Choice'])


    def backwards(self, orm):
        # Deleting model 'Choice'
        db.delete_table('poll_choice')


    models = {
        'poll.choice': {
            'Meta': {'object_name': 'Choice'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['poll.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        'poll.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['poll']