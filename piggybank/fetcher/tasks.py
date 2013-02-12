from __future__ import absolute_import

from helpers.mail import send_mail
import time

from . import helpers
from celery import task
from celery.task import periodic_task
from .models import Fetch, FetchType, FetchResult
from stocks.models import Stock
from django.conf import settings
from django.core.cache import cache
from celery.utils.log import get_task_logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display; display = Display(visible=0, size=(1024, 768)); display.start()

logger = get_task_logger(__name__)


# Put task here in place of foo.
@periodic_task(run_every=24*60*60)
def run_screen(fetch_type_id=2):
	try:
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

		# TODO: make this less explicit
		if str(fetch_type) == "Thomson and Ford Buy Buy":
			helpers.populate_filters_reuters_ford_buy_buy(browser)
		elif str(fetch_type) == "Thomson and Ford Sell Sell":
			helpers.populate_filters_reuters_ford_sell_sell(browser)
		elif str(fetch_type) == "Thomson and Ford Hold Hold":
			helpers.populate_filters_reuters_ford_hold_hold(browser)
		else:
			return []
			logger.error("No populate filter function found for fetch type " + str(fetch_type))


		helpers.delete_old_results()

		# download csv
		# click the download button to bring up the popup
		helpers.find_element_by_xpath_and_wait(browser, "//a[text()='Download']").click()
		# click the traders radio button
		helpers.find_element_by_xpath_and_wait(browser, "//input[@id='radio-Traders']").click()
		# click ok to download
		logger.info("Clicking Download")
		helpers.find_element_by_xpath_and_wait(browser, "//div[@class='popup-contents']//a[@title='Ok']").click()
		# wait for the download - TODO - MAKE SMARTER
		tickers = helpers.process_result()
		browser.quit()

		fetch.successful = True
		fetch.save()
		tickers_key = hash(str(tickers))
		cache.set(tickers_key, tickers)
		save_fetch_results.delay(fetch.id, tickers_key)
		send_fetch_email.delay(fetch.id)

		return tickers
	except Exception, e:
		raise run_screen.retry(exc=e)


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

@task
def send_fetch_email(fetch_id):
	# Delay email sending to save incoming data
	time.sleep(10)
	# Get admin emails from settings
	admin_emails = [email[1] for email in settings.ADMINS]
	# Get stocks retrieved
	fetch = Fetch.objects.get(id=fetch_id)
	fetch_type = fetch.type
	fetches = fetch_type.fetch_set.all()
	new_fetch = fetches[len(fetches) - 1]
	logger.info("New Fetch has id " + str(new_fetch.id))
	# if the previous fetch was unsuccessful, go back until there is a successful one
	i = 2
	while True:
		old_fetch = fetches[len(fetches) - i]
		i -= 1
		if old_fetch.result.__class__.__name__ != 'NoneType':
			if old_fetch.successful == True:
				break
			else:
				logger.info("Fetch " + str(old_fetch.id) + " was unsuccessful")
		else:
			logger.info("Fetch " + str(old_fetch.id) + " did not save a result")
	logger.info("Old Fetch has id " + str(old_fetch.id))

	new_tickers = [str(stock) for stock in new_fetch.result.stocks.all()]
	old_tickers = [str(stock) for stock in old_fetch.result.stocks.all()]

	buy = [ticker for ticker in new_tickers if ticker not in old_tickers]
	sell = [ticker for ticker in old_tickers if ticker not in new_tickers]

	# Send unsuccessful fetch email
	if not new_fetch.successful:
		send_mail('Daily Fetch Update', 'Fetch was unsuccesful.', admin_emails)
		return
	# Send succesful fetch email
	email_content = 'Completed Fetch: ' + str(fetch.type) + '\nBuy: ' + str(buy) + '\nSell: ' + str(sell) + '\nPortfolio: ' + str(new_tickers)
	logger.info("Email Contents: " + email_content)
	send_mail('Daily Fetch Update', email_content, admin_emails)