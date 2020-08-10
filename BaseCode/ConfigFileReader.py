import configparser
config = configparser.RawConfigParser()
config.read("../Configurations/Config.cfg")


class ConfigReader:
    @staticmethod
    def config_read(section, key):
        return config.get(section, key)

    @staticmethod
    def get_URL():
        URL = config.get('Details', 'URL')
        return URL


