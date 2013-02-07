from django.db import models
from django.utils import timezone

class Stock(models.Model):
	"""
	An individual stock.

	"""
	ticker = models.CharField(max_length=16)

	def get_company_name(self):
		"""
		Get full company name.

		"""
		pass

	def __unicode__(self):
		return self.ticker


class StockSnapshot(models.Model):
	"""
	Snapshot of a stock at a specified date.

	"""
	open_price = models.FloatField(blank=True)
	close_price = models.FloatField(blank=True)
	average_daily_volume = models.FloatField(blank=True)
	book_value = models.FloatField(blank=True)
	dividend = models.FloatField(blank=True)
	eps = models.FloatField(blank=True)
	eps_current_year = models.FloatField(blank=True)
	eps_next_year = models.FloatField(blank=True)
	eps_next_quarter = models.FloatField(blank=True)
	market_cap = models.FloatField(blank=True)
	ma_200 = models.FloatField(blank=True)
	pe = models.FloatField(blank=True)
	peg = models.FloatField(blank=True)

	stock = models.ForeignKey(Stock)
	created = models.DateTimeField(default=timezone.now)