import helpers
import os
import time
from celery import task
from .models import Fetch, FetchType, FetchResult
from stocks.models import Stock
from django.conf import settings
from django.core.cache import cache
from celery.utils.log import get_task_logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

logger = get_task_logger(__name__)


# Put task here in place of foo.
@task
def run_screen(fetch_type_id):
	fetch_type = FetchType.objects.get(id=fetch_type_id)
	logger.info("Starting screen for " + str(fetch_type))
	fetch = Fetch.objects.create(type=fetch_type)

	browser = webdriver.Chrome()

	browser.get("https://login.fidelity.com/ftgw/Fas/Fidelity/RtlCust/Login/Init?AuthRedUrl=https://oltx.fidelity.com/ftgw/fbc/ofsummary/defaultPage")
	logger.info("Waiting for login")
	elem = helpers.find_element_by_id_and_wait(browser, "ssnt")
	elem.send_keys(settings.FIDELITY_USERNAME)
	elem = helpers.find_element_by_id_and_wait(browser, "PIN")
	elem.send_keys(settings.FIDELITY_PASSWORD)
	elem.send_keys(Keys.RETURN)
	logger.info("Logging in")
	helpers.find_element_by_id_and_wait(browser, "serviceMessage")
	browser.get("https://research2.fidelity.com/fidelity/screeners/commonstock/main.asp")
	logger.info("Going to screen page")

	helpers.populate_filters_reuters_ford(browser)

	helpers.delete_old_results()

	# download csv
	# click the download button to bring up the popup
	helpers.find_element_by_xpath_and_wait(browser, "//a[text()='Download']").click()
	# click the traders radio button
	helpers.find_element_by_xpath_and_wait(browser, "//input[@id='radio-Traders']").click()
	# click ok to download
	helpers.find_element_by_xpath_and_wait(browser, "//div[@class='popup-contents']//a[@title='Ok']").click()
	# wait for the download - TODO - MAKE SMARTER
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
