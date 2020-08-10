from selenium import webdriver
import pytest
from BaseCode.ConfigFileReader import ConfigReader
from Pages.loginpage import Login_Page

class Test_Admin_Login:

    @pytest.fixture()
    def initiate(self):
        self.driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_URL())
        self.login = Login_Page(self.driver)
        yield
        self.driver.quit()

    def test01_valid_titlepage(self, initiate):
        expected_titlepage = "Your store. Login"
        actual_titlepage = self.driver.title
        assert expected_titlepage == actual_titlepage

    def test02_invalid_user(self,initiate):
        self.login.enter_email(ConfigReader.config_read('Invalid User', 'Username'))
        self.login.enter_password(ConfigReader.config_read('Invalid User', 'password'))
        self.login.click_login()
        expected_err_msg = "No customer account found"
        actual_err_msg = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li').text
        assert expected_err_msg == actual_err_msg

    def test03_invalid_password(self,initiate):
        self.login.enter_email(ConfigReader.config_read('Invalid Password', 'Username'))
        self.login.enter_password(ConfigReader.config_read('Invalid Password', 'password'))
        self.login.click_login()
        expected_err_msg = "The credentials provided are incorrect"
        actual_err_msg = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[1]/ul/li').text
        assert expected_err_msg == actual_err_msg

    def test04_valid_credentials(self,initiate):
        self.login.enter_email(ConfigReader.config_read('Valid Credentials', 'Username'))
        self.login.enter_password(ConfigReader.config_read('Valid Credentials', 'password'))
        self.login.click_login()
        assert self.driver.title == "Dashboard / nopCommerce administration"


if __name__ == '__main__':
    pytest.main()


