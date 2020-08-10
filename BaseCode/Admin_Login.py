from BaseCode.ConfigFileReader import ConfigReader
from Pages.loginpage import Login_Page
from selenium import webdriver

class Base_Login:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.login = Login_Page(self.driver)
        self.driver.get(ConfigReader.get_URL())
        self.login.enter_email(ConfigReader.config_read('Valid Credentials', 'Username'))
        self.login.enter_password(ConfigReader.config_read('Valid Credentials', 'password'))
        self.login.click_login()