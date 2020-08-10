from Locators.Locators import Admin_Locators
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Search_Customer:

    def __init__(self,driver):
        self.driver = driver
        self.searchemail_textbox_id = Admin_Locators.searchemail_textbox_id
        self.searchcompany_texbox_id = Admin_Locators.searchcompany_texbox_id
        self.searchfirstname_textbox_id = Admin_Locators.searchfirstname_textbox_id
        self.searchidadd_texbox_id = Admin_Locators.searchidadd_texbox_id
        self.searchlastname_textbox_id = Admin_Locators.searchlastname_textbox_id
        self.searchrole_dropdown_id = Admin_Locators.searchrole_dropdown_id
        self.dob_month_dropdown_id  = Admin_Locators.dob_month_dropdown_id
        self.dob_day_dropdown_id  = Admin_Locators.dob_day_dropdown_id
        self.search_button_id = Admin_Locators.search_button_id
        self.addnew_button_xpath = Admin_Locators.addnew_button_xpath
        self.expand_export_class = Admin_Locators.expand_export_class
        self.export_dropdown_xpath = Admin_Locators.export_dropdown_xpath
        self.exportxml_all_link_xpath = Admin_Locators.exportxml_all_link_xpath
        self.exportxml_selected_link_id = Admin_Locators.exportxml_selected_link_id
        self.exportexcel_all_link_xpath = Admin_Locators.exportexcel_all_link_xpath
        self.exportexcel_selected_link_id = Admin_Locators.exportexcel_selected_link_id
        self.show_dropdown_name = Admin_Locators.show_dropdown_name


    def enter_email(self,email):
        self.driver.find_element_by_id(self.searchemail_textbox_id).send_keys(email)

    def enter_company(self,company):
        self.driver.find_element_by_id(self.searchcompany_texbox_id).send_keys(company)

    def enter_firstname(self,firstname):
        self.driver.find_element_by_id(self.searchfirstname_textbox_id).send_keys(firstname)

    def enter_ipaddress(self,ipaddress):
        self.driver.find_element_by_id(self.searchidadd_texbox_id).send_keys(ipaddress)

    def enter_lastname(self,lastname):
        self.driver.find_element_by_id(self.searchlastname_textbox_id).send_keys(lastname)

    def select_role(self, select_role):
        role = Select(self.driver.find_element_by_id(self.searchrole_dropdown_id))
        role.select_by_visible_text(select_role)

    def select_month(self,select_month):
        month = Select(self.driver.find_element_by_id(self.dob_month_dropdown_id))
        month.select_by_visible_text(select_month)

    def select_day(self,select_day):
        day = Select(self.driver.find_element_by_id(self.dob_day_dropdown_id))
        day.select_by_visible_text(select_day)

    def click_search(self):
        self.driver.find_element_by_id(self.search_button_id).click()

    def expand_export(self):
        self.driver.find_element_by_xpath(self.export_dropdown_xpath).click()

    def click_allfound_xml(self):
        self.driver.find_element_by_xpath(self.exportxml_all_link_xpath).click()

    def click_selected_xml(self):
        self.driver.find_element_by_id(self.exportxml_selected_link_id).click()

    def click_all_excel(self):
        self.driver.find_element_by_xpath(self.exportexcel_all_link_xpath).click()

    def click_selected_excel(self):
        self.driver.find_element_by_id(self.exportexcel_selected_link_id).click()

    def show_items(self,number):
        showitems = Select(self.driver.find_element_by_name(self.show_dropdown_name))
        showitems.select_by_visible_text(number)

    def click_addnew(self):
        self.driver.find_element_by_xpath(self.addnew_button_xpath).click()