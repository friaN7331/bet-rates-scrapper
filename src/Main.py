from src.config import config_service
from src.output import output_service
from src.web import request_service


def procedure():
  base_url = config_service.configuration['urls']['vitisport']

  html = ''

  for league_entry in config_service.configuration['leagues']:
    url = base_url + config_service.configuration['vitisport'][league_entry]
    html = request_service.get_html(url)

    output_service.create_and_write(league_entry, html)


if __name__ == "__main__":
  procedure()
