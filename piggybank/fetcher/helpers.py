import time
import os
import csv
from selenium.webdriver.support.wait import WebDriverWait

def populate_filters_reuters_ford(browser):
  populate_criteria(browser, 'Thomson Reuters')
  populate_value(browser, 0, 0, 'Is')
  populate_value(browser, 0, 1, 'Buy')
  time.sleep(1)
  populate_criteria(browser, 'Ford')
  populate_value(browser, 1, 0, 'Is')
  populate_value(browser, 1, 1, 'Strong Buy')
  # time.sleep(1)
  # populate_criteria(browser, 'Dividend', 1)
  # populate_value(browser, 2, 0, 'Is in the range')
  # populate_value(browser, 2, 1, '1', 0)
  # populate_value(browser, 2, 1, '2', 1)

# index is the index of the typeahead dropdown that should be selected after it types in the criteria
def populate_criteria(browser, criteria, index=0):
  print "Populating criteria " + criteria
  browser.execute_script("$('.div-criteria-lookup:last input').val('')")
  elem = browser.find_elements_by_css_selector('.div-criteria-lookup input')[-1]
  elem.send_keys(criteria)
  elem = browser.find_elements_by_css_selector('.result-list a')[index]
  elem.click()
  time.sleep(1)

# row and col are 0 based
# some values (like dividend range) have 2 text inputs that are children of the same secondary-control div
# sub_col indicates which input within the secondary-control div to populate. It is also 0 based
def populate_value(browser, row, col, val, sub_col=0):
  elem = browser.find_element_by_xpath("//table[@class='table-screener-criteria']//tr[" + str((row + 1)) + "]//div[contains(concat(' ',@class,' '),' secondary-control ')][" + str(col + 1) + "]")
  children = elem.find_elements_by_xpath("div")
  klass = children[sub_col].get_attribute("class")
  if klass == 'expander':
    children[sub_col].click()
    time.sleep(0.1)
    choice = find_element_by_xpath_and_wait(elem, "./div[@class='popup']//ul[@class='option-list']//a[text()='" + val + "']")
    choice.click()
  elif klass.find('numeric-input') != -1:
    text_box = children[sub_col].find_element_by_xpath(".//input")
    text_box.send_keys(val)


def process_result():
  # find the most recent download
  files = [os.path.join(os.environ['HOME'], "Downloads", fname) for fname in os.listdir(os.path.join(os.environ['HOME'], "Downloads"))]
  screens = []
  for f in files:
    if f.find("screen_results") != -1:
      screens.append(f)
  last_screen = max(screens, key=os.path.getmtime)
  tickers = []
  with open(last_screen, 'rb') as csvfile:
    screen_reader = csv.reader(csvfile)
    for row in screen_reader:
      try:
        tickers.append(row[1])
      except IndexError:
        break
  # remove first row (which is the title)
  del tickers[0]
  return tickers

def find_element_by_xpath_and_wait(driver, xpath):
  WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element_by_xpath(xpath)
    )
  return driver.find_element_by_xpath(xpath)

def find_elements_by_xpath_and_wait(driver, xpath):
  WebDriverWait(driver, 10).until(
            lambda driver : driver.find_elements_by_xpath(xpath)
    )
  return driver.find_elements_by_xpath(xpath)