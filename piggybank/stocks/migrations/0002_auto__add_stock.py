# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table('stocks_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ticker', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('stocks', ['Stock'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('stocks_stock')


    models = {
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['stocks']