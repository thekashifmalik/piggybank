# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fetch'
        db.create_table('fetcher_fetch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 26, 0, 0))),
        ))
        db.send_create_signal('fetcher', ['Fetch'])


    def backwards(self, orm):
        # Deleting model 'Fetch'
        db.delete_table('fetcher_fetch')


    models = {
        'fetcher.fetch': {
            'Meta': {'object_name': 'Fetch'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 26, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['fetcher']