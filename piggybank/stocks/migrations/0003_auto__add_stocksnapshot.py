# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StockSnapshot'
        db.create_table('stocks_stocksnapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('open_price', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('close_price', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('average_daily_volume', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('book_value', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('dividend', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('eps', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('eps_current_year', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('eps_next_year', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('eps_next_quarter', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('market_cap', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('ma_200', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('pe', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('peg', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Stock'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 4, 0, 0))),
        ))
        db.send_create_signal('stocks', ['StockSnapshot'])


    def backwards(self, orm):
        # Deleting model 'StockSnapshot'
        db.delete_table('stocks_stocksnapshot')


    models = {
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'stocks.stocksnapshot': {
            'Meta': {'object_name': 'StockSnapshot'},
            'average_daily_volume': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'book_value': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'close_price': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 4, 0, 0)'}),
            'dividend': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'eps': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'eps_current_year': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'eps_next_quarter': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'eps_next_year': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ma_200': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'market_cap': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'open_price': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'pe': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'peg': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Stock']"})
        }
    }

    complete_apps = ['stocks']