import configparser


def get_config():
    config = configparser.ConfigParser()
    config.read('PATH_TO\\resources.ini')
    return config
