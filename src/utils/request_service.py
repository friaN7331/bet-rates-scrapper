import time

import requests
from selenium import webdriver

from src.config.config_service import configuration

driver_path = configuration['configuration']['paths']['chrome_webdriver']
driver = webdriver.Chrome(driver_path)

headers = {
  'User-Agent': configuration['configuration']['requests']['user-agent']
}

def get_html_driver(url):
  driver.get(url)
  time.sleep(configuration['configuration']['requests']['sleep'])
  return driver.page_source

def get_html_requests(url):
  return requests.get(url, headers=headers).text

# response = requests.get(url)
# return response.text
