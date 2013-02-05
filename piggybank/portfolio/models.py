from django.db import models
from django.utils import timezone
from stocks.models import StockSnapshot

# Create your models here.
class Portfolio(models.Model):
  """
  A generic container for a stock Portfolio
  """
  name = models.CharField(max_length=128)
  description = models.TextField(blank=True)
  created = models.DateTimeField(default=timezone.now)

class PortfolioSnapshot(models.Model):
  """
  All of a portfolio's holdings on a given day
  """
  portfolio = models.ForeignKey(Portfolio)
  created = models.DateTimeField(default=timezone.now)

class PortfolioHolding(models.Model):
  """
  The number of shares owned of a given stock for a given portfolio
  on a given day
  """
  snapshot = models.ForeignKey(PortfolioSnapshot)
  stock = models.ForeignKey(StockSnapshot)
  shares = models.FloatField()