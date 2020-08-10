from selenium import webdriver
from Locators.Locators import Admin_Locators

class Dashboard_Page:

    def __init__(self, driver):
        self.driver = driver
        self.customer_expand_xpath = Admin_Locators.customerexpand_xpath
        self.customer_link_xpath = Admin_Locators.customer_link_xpath
        self.logout_link_text = Admin_Locators.logout_link_text

    def click_cust_expand(self):
        self.driver.find_element_by_xpath(self.customer_expand_xpath).click()

    def click_customer(self):
        self.driver.find_element_by_link_text(self.customer_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()

