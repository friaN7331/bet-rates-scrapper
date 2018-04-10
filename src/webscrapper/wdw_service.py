from src.config import config_service
from src.entities import matches
from src.utils import beautifulsoup_service


def get_matches():

  # Create the URL from the configuration
  url = config_service.configuration['urls']['wdw']  # SFStats base url
  url += config_service.configuration['wdw']['de1']  # Add DE_Bundesliga path

  # Get the HTML of the page and create the Soup
  html_soup = beautifulsoup_service.get_soup_by_url(url)

  # Create an array with the matches
  next_matches = [matches.WdwMatch(html_soup)]

  # Get all remaining urls
  remaining_urls = __extract_remaining_urls(html_soup)

  # Process the urls and extract the data
  for url in remaining_urls:
    html_soup = beautifulsoup_service.get_soup_by_url(url)
    next_matches.append(matches.WdwMatch(html_soup))

  return next_matches

def __extract_remaining_urls(soup):
  urls = []

  for match in soup.select_one('#headlinefull').find_all('div'):
    a = match.find('a')
    if a != None:
      urls.append(a['href'])

  return urls