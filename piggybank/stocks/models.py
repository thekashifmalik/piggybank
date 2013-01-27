from django.db import models


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