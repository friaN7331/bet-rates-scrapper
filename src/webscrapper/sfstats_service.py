import bs4 as bs

from src.config import config_service
from src.entities import matches
from src.utils import request_service


def get_matches():
  # Create the URL from the configuration
  url = config_service.configuration['urls']['sfstats']  # SFStats base url
  url += config_service.configuration['sfstats']['de1']  # Add DE_Bundesliga path

  # Get the HTML of the page and create the Soup
  response = request_service.get_html_driver(url)
  html_soup = bs.BeautifulSoup(response, 'lxml')

  next_matches_table = html_soup.select_one('#contentBlock > div > div.col1_big > table > tbody') # Table with the next matches

  next_matches = []

  for row in next_matches_table.find_all('tr', ['tsor1', 'tsor2']):
    tds = row.find_all('td')
    next_matches.append(matches.SfstatsMatch(tds))

  return next_matches