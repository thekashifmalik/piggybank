from django.db import models
from django.utils import timezone
from stocks.models import Stock


class FetchType(models.Model):
	"""
	A type of fetch.

	"""
	name = models.CharField(max_length=128)
	created = models.DateTimeField(default=timezone.now())
	
	def __unicode__(self):
		return self.name


class FetchResult(models.Model):
	stocks = models.ManyToManyField(Stock)

	def __unicode__(self):
		return str(self.fetch) + ' results'


class Fetch(models.Model):
	"""
	An attempt to fetch some stock data.

	"""
	created = models.DateTimeField(default=timezone.now())
	successful = models.BooleanField(default=False)
	result = models.OneToOneField(FetchResult, null=True, blank=True)
	type = models.ForeignKey(FetchType)

	def __unicode__(self):
		return 'Fetch on ' + str(self.created)
