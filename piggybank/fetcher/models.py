from django.db import models
from django.utils import timezone

# Create your models here.
class Fetch(models.Model):
	"""
	An attempt to fetch a stock screen.

	"""
	created = models.DateTimeField(default=timezone.now())
	successful = models.BooleanField()

	def __unicode__(self):
		return 'Fetch on ' + str(self.created)


class Stock(models.Model):
	"""
	An individual stock.
	
	"""
	ticker = models.CharField(max_length=16)

	def get_company_name(self):
		pass