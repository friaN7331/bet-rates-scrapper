import bs4 as bs

from src.config import config_service
from src.entities import matches
from src.utils import request_service


def get_matches():
  # Create the URL from the configuration
  url = config_service.configuration['urls']['vitisport']  # SFStats base url
  url += config_service.configuration['vitisport']['de1']  # Add DE_Bundesliga path

  # Get the HTML of the page and create the Soup
  response = request_service.get_html_driver(url)
  html_soup = bs.BeautifulSoup(response, 'lxml')

  next_matches_table = html_soup.select_one('#quicktips tbody')  # Table with the next matches

  next_matches = []

  for row in next_matches_table.select('tr'):
    if row.select_one('td.standardbunkaobr') != None:
      tds = row.find_all('td')
      next_matches.append(matches.VitisportMatch(tds))

  return next_matches