import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\User\PycharmProjects\MyProjectTrendSphere\configration\config.ini')

class ReadConfig:

    @staticmethod
    def get_url():
        url_ =config.get('user register info', 'base_url')
        return url_



