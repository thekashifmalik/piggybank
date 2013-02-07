# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'StockSnapshot.close_price'
        db.alter_column('stocks_stocksnapshot', 'close_price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.eps_next_quarter'
        db.alter_column('stocks_stocksnapshot', 'eps_next_quarter', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.average_daily_volume'
        db.alter_column('stocks_stocksnapshot', 'average_daily_volume', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.eps_current_year'
        db.alter_column('stocks_stocksnapshot', 'eps_current_year', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.eps'
        db.alter_column('stocks_stocksnapshot', 'eps', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.eps_next_year'
        db.alter_column('stocks_stocksnapshot', 'eps_next_year', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.book_value'
        db.alter_column('stocks_stocksnapshot', 'book_value', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.market_cap'
        db.alter_column('stocks_stocksnapshot', 'market_cap', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.open_price'
        db.alter_column('stocks_stocksnapshot', 'open_price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.ma_200'
        db.alter_column('stocks_stocksnapshot', 'ma_200', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.pe'
        db.alter_column('stocks_stocksnapshot', 'pe', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.dividend'
        db.alter_column('stocks_stocksnapshot', 'dividend', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'StockSnapshot.peg'
        db.alter_column('stocks_stocksnapshot', 'peg', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # Changing field 'StockSnapshot.close_price'
        db.alter_column('stocks_stocksnapshot', 'close_price', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.eps_next_quarter'
        db.alter_column('stocks_stocksnapshot', 'eps_next_quarter', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.average_daily_volume'
        db.alter_column('stocks_stocksnapshot', 'average_daily_volume', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.eps_current_year'
        db.alter_column('stocks_stocksnapshot', 'eps_current_year', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.eps'
        db.alter_column('stocks_stocksnapshot', 'eps', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.eps_next_year'
        db.alter_column('stocks_stocksnapshot', 'eps_next_year', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.book_value'
        db.alter_column('stocks_stocksnapshot', 'book_value', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.market_cap'
        db.alter_column('stocks_stocksnapshot', 'market_cap', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.open_price'
        db.alter_column('stocks_stocksnapshot', 'open_price', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.ma_200'
        db.alter_column('stocks_stocksnapshot', 'ma_200', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.pe'
        db.alter_column('stocks_stocksnapshot', 'pe', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.dividend'
        db.alter_column('stocks_stocksnapshot', 'dividend', self.gf('django.db.models.fields.FloatField')(default=0.0))

        # Changing field 'StockSnapshot.peg'
        db.alter_column('stocks_stocksnapshot', 'peg', self.gf('django.db.models.fields.FloatField')(default=0.0))

    models = {
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ticker': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'stocks.stocksnapshot': {
            'Meta': {'object_name': 'StockSnapshot'},
            'average_daily_volume': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'book_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'close_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dividend': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eps': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eps_current_year': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eps_next_quarter': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'eps_next_year': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ma_200': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'market_cap': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'open_price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'pe': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'peg': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Stock']"})
        }
    }

    complete_apps = ['stocks']