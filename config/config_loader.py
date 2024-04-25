import configparser
import os

def load_config(config_file='config/settings.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file '{config_file}' not found.")
    return config
