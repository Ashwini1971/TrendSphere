import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\User\PycharmProjects\SwagLabs\configuration\config.ini')

class ReadConfig:

    @staticmethod
    def get_page_url():
        url = config.get('user login info', 'base_url')
        return url

    @staticmethod
    def get_email_address():
        email = config.get('user login info', 'email_address')
        return email

    @staticmethod
    def get_password():
        password = config.get('user login info', 'password')
        return password

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('user login info', 'invalid_password')
        return invalid_password

    @staticmethod
    def get_admin_username():
        username = config.get('admin login info', 'user_name')
        return username

    @staticmethod
    def get_admin_password():
        password_ = config.get('admin login info', 'password')
        return password_








