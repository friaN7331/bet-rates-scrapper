import bs4 as bs

from src.utils import request_service


def get_soup_by_url(url):
  response = request_service.get_html_driver(url)
  return bs.BeautifulSoup(response, 'lxml')
