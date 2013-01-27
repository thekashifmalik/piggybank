from celery import task
from .models import FetchResult
from stocks.models import Stock
from django.core.cache import cache
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


# Put task here in place of foo.
@task
def foo():
	pass


@task
def save_fetch_results(fetch_id, result_key):
	"""
	Save results of a successful fetch.

	"""
	# Get result from cache
	results = cache.get(result_key)

	# Check for result existence
	if not results:
		logger.error('Result not found in cache.')
		return

	# Create fetch result and associate with fetch.
	fetch_result = FetchResult()
	fetch_result.fetch = fetch_id

	# Add stocks to result
	for stock_ticker in results:
		stock = Stock.objects.get_or_create(ticker=stock_ticker)[0]
		fetch_result.stocks.add(stock)

	fetch_result.save()
