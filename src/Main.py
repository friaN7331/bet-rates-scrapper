from src.config import config_service
from src.output import output_service
from src.utils import request_service, sql_service
from src.webscrapper import wdw_service


def procedure():
  base_url = config_service.configuration['urls']['wdw']

  html = ''

  for league_entry in config_service.configuration['leagues']:
    url = base_url + config_service.configuration['wdw'][league_entry]
    html = request_service.get_html_driver(url)

    output_service.create_and_write(league_entry, html)


if __name__ == "__main__":
  #procedure()

  row = sql_service.getVersion()
  print(row)

  for match in wdw_service.get_matches():
    print(match.__dict__)

  request_service.driver.quit()