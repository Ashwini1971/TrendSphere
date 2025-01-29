import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\User\PycharmProjects\POMbasedProject\configration\config.ini')

class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('admin login info', 'base_url')
        return url

    @staticmethod
    def get_username():
        user_name = config.get('admin login info', 'user_name')
        return user_name

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'password')
        return password
