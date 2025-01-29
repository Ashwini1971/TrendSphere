import configparser
config = configparser.RawConfigParser()
config.read(r'C:\Users\User\PycharmProjects\Demo\configuration\config.ini')

class ReadConfig:

    @staticmethod
    def get_url():
        url_ = config.get('google info', 'base_url')
        return url_

    @staticmethod
    def user_name():
        username = config.get('user login', 'user_name')
        return username

    @staticmethod
    def password_():
        password = config.get('user login', 'password')
        return password

