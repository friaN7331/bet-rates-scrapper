import requests
import time

from src.config import config_service
from selenium import webdriver


driver_path = config_service.configuration['configuration']['paths']['chrome_webdriver']
driver = webdriver.Chrome(driver_path)

def get_html(url):
  driver.get(url)
  time.sleep(3)
  return driver.page_source
# response = requests.get(url)
# return response.text
