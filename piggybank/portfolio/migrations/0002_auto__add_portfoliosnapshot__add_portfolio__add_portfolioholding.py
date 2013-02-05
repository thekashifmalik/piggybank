# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PortfolioSnapshot'
        db.create_table('portfolio_portfoliosnapshot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Portfolio'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 4, 0, 0))),
        ))
        db.send_create_signal('portfolio', ['PortfolioSnapshot'])

        # Adding model 'Portfolio'
        db.create_table('portfolio_portfolio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 4, 0, 0))),
        ))
        db.send_create_signal('portfolio', ['Portfolio'])

        # Adding model 'PortfolioHolding'
        db.create_table('portfolio_portfolioholding', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('snapshot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.PortfolioSnapshot'])),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.StockSnapshot'])),
            ('shares', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('portfolio', ['PortfolioHolding'])


    def backwards(self, orm):
        # Deleting model 'PortfolioSnapshot'
        db.delete_table('portfolio_portfoliosnapshot')

        # Deleting model 'Portfolio'
        db.delete_table('portfolio_portfolio')

        # Deleting model 'PortfolioHolding'
        db.delete_table('portfolio_portfolioholding')


    models = {
        'portfolio.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 4, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'portfolio.portfolioholding': {
            'Meta': {'object_name': 'PortfolioHolding'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shares': ('django.db.models.fields.FloatField', [], {}),
            'snapshot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.PortfolioSnapshot']"}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.StockSnapshot']"})
        },
        'portfolio.portfoliosnapshot': {
            'Meta': {'object_name': 'PortfolioSnapshot'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Portfolio']"})
        },
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

    complete_apps = ['portfolio']