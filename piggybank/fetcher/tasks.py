import helpers
import os
import time
from celery import task
from .models import Fetch, FetchType, FetchResult
from stocks.models import Stock
from django.core.cache import cache
from celery.utils.log import get_task_logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


logger = get_task_logger(__name__)


# Put task here in place of foo.
@task
def run_screen(fetch_type_id):
	fetch_type = FetchType.objects.get(id=fetch_type_id)
	fetch = Fetch.objects.create(type=fetch_type)

	browser = webdriver.Chrome()
	browser.get("https://login.fidelity.com/ftgw/Fas/Fidelity/RtlCust/Login/Init?AuthRedUrl=https://oltx.fidelity.com/ftgw/fbc/ofsummary/defaultPage")
	elem = browser.find_element_by_id("ssnt")
	elem.send_keys(os.environ['FUN'])
	elem = browser.find_element_by_id("PIN")
	elem.send_keys(os.environ['FPW'] + Keys.RETURN)
	browser.get("https://research2.fidelity.com/fidelity/screeners/commonstock/main.asp")


	helpers.populate_filters_reuters_ford(browser)

	# download csv
	# click the download button to bring up the popup
	helpers.find_element_by_xpath_and_wait(browser, "//a[text()='Download']").click()
	# click the traders radio button
	helpers.find_element_by_xpath_and_wait(browser, "//input[@id='radio-Traders']").click()
	# click ok to download
	browser.find_element_by_xpath("//div[@class='popup-contents']//a[@title='Ok']").click()
	# wait for the download
	time.sleep(2)
	tickers = helpers.process_result()
	browser.quit()

	fetch.successful = True
	fetch.save()
	tickers_key = hash(str(tickers))
	cache.set(tickers_key, tickers)
	save_fetch_results.delay(fetch.id, tickers_key)

	return tickers


@task
def save_fetch_results(fetch_id, result_key):
	"""
	Save results of a successful fetch.

	"""
	# Get result from cache
	results = cache.get(result_key)
	cache.delete(result_key)

	# Check for result existence
	if not results:
		logger.error('Result not found in cache.')
		return

	# Create fetch result and associate with fetch.
	fetch = Fetch.objects.get(id=fetch_id)
	fetch_result = FetchResult.objects.create()
	fetch.result = fetch_result
	fetch.save()

	# Add stocks to result
	for stock_ticker in results:
		stock = Stock.objects.get_or_create(ticker=stock_ticker)[0]
		fetch_result.stocks.add(stock)

	fetch_result.save()
