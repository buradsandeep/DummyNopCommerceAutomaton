from BaseCode.ConfigFileReader import ConfigReader
from BaseCode.Admin_Login import Base_Login
from Pages.dashboard import Dashboard_Page
#from Pages.loginpage import Login_Page
from Pages.searchcustomer import Search_Customer
from selenium import webdriver
import pytest
import time


class Test_Search_Customer:
    driver = webdriver.Chrome(executable_path="../Drivers/chromedriver.exe")
    driver.maximize_window()
    search_cust = Search_Customer(driver)

    def test01_valid_email(self):
        self.login1 = Base_Login(self.driver)
        self.login1.login()
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        email_id = "admin@yourStore.com"
        self.search_cust.enter_email(email_id)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[2]').text == email_id

    def test02_invalid_email(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        email_id = "admin123@yourStore.com"
        self.search_cust.enter_email(email_id)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[1]').text == 'No data available in table'

    def test03_valid_company(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        company_name = "Gadha Electronics"
        self.search_cust.enter_company(company_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[5]').text == company_name


    def test04_invalid_company(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        company_name = "Gada Electronics"
        self.search_cust.enter_company(company_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[1]').text == 'No data available in table'

    def test05_valid_firstname(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        first_name = "Victoria"
        self.search_cust.enter_firstname(first_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[3]').text == "Victoria Terces"

    def test06_invalid_firstname(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        first_name = "Victoria12"
        self.search_cust.enter_firstname(first_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[1]').text == 'No data available in table'

    def test07_valid_lastname(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        last_name = "Terces"
        self.search_cust.enter_lastname(last_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[3]').text == "Victoria Terces"

    def test08_invalid_lastname(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        last_name = "Terces12"
        self.search_cust.enter_lastname(last_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[1]').text == 'No data available in table'

    def test09_fullname(self):
        self.driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")
        first_name = "Victoria"
        last_name = "Terces"
        self.search_cust.enter_firstname(first_name)
        self.search_cust.enter_lastname(last_name)
        self.search_cust.click_search()
        time.sleep(2)
        assert self.driver.find_element_by_xpath('//*[@id="customers-grid"]/tbody/tr[1]/td[3]').text == "Victoria Terces"

    def test10_export_xmlall(self):
        self.search_cust.expand_export()
        time.sleep(2)
        self.search_cust.click_allfound_xml()

    def test11_export_excelall(self):
        self.search_cust.expand_export()
        time.sleep(2)
        self.search_cust.click_allfound_xml()



