import yaml


config_file_path = "../resource/config.yml"

configuration = {}


def init():
  load_configuration()


def load_configuration():
  with open(config_file_path, 'r') as file:
    try:
      global configuration
      configuration = yaml.load(file)
    except yaml.YAMLError as exc:
      print(exc)


def save_configuration():
  with open(config_file_path, 'w') as file:
    try:
      yaml.dump(configuration, file, default_flow_style=False)
    except yaml.YAMLError as exc:
      print(exc)


init()
