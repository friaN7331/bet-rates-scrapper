from src.config import config_service


__output_path = config_service.configuration['configuration']['paths']['output_path']


def create_and_write(name, content):
  with open(__output_path + name, 'w', encoding='utf-8') as file:
    file.write(content)
    file.close()
