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
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 27, 0, 0))),
            ('successful', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('result', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fetcher.FetchResult'], unique=True, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fetcher.FetchType'])),
        ))
        db.send_create_signal('fetcher', ['Fetch'])

        # Adding model 'FetchType'
        db.create_table('fetcher_fetchtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 27, 0, 0))),
        ))
        db.send_create_signal('fetcher', ['FetchType'])

        # Adding model 'FetchResult'
        db.create_table('fetcher_fetchresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('fetcher', ['FetchResult'])

        # Adding M2M table for field stocks on 'FetchResult'
        db.create_table('fetcher_fetchresult_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('fetchresult', models.ForeignKey(orm['fetcher.fetchresult'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('fetcher_fetchresult_stocks', ['fetchresult_id', 'stock_id'])


    def backwards(self, orm):
        # Deleting model 'Fetch'
        db.delete_table('fetcher_fetch')

        # Deleting model 'FetchType'
        db.delete_table('fetcher_fetchtype')

        # Deleting model 'FetchResult'
        db.delete_table('fetcher_fetchresult')

        # Removing M2M table for field stocks on 'FetchResult'
        db.delete_table('fetcher_fetchresult_stocks')


    models = {
        'fetcher.fetch': {
            'Meta': {'object_name': 'Fetch'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 27, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fetcher.FetchResult']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'successful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fetcher.FetchType']"})
        },
        'fetcher.fetchresult': {
            'Meta': {'object_name': 'FetchResult'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stocks.Stock']", 'symmetrical': 'False'})
        },
        'fetcher.fetchtype': {
            'Meta': {'object_name': 'FetchType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 27, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['fetcher']