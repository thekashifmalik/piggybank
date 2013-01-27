# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table('fetcher_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticker', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('fetcher', ['Stock'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('fetcher_stock')


    models = {
        'fetcher.fetch': {
            'Meta': {'object_name': 'Fetch'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 27, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'successful': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'fetcher.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['fetcher']