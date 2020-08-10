from Locators.Locators import Admin_Locators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Add_Customer:

    def __init__(self,driver):
        self.driver = driver
        self.add_email_textbox_id = Admin_Locators.add_email_textbox_id
        self.add_password_textbox_id = Admin_Locators.add_password_textbox_id
        self.add_firstname_textbox_id = Admin_Locators.add_firstname_textbox_id
        self.add_lastname_textbox_id = Admin_Locators.add_lastname_textbox_id
        self.gender_male_radio_id = Admin_Locators.gender_male_radio_id
        self.gender_female_radio_id = Admin_Locators.gender_female_radio_id
        self.add_dob_calendar_id = Admin_Locators.add_dob_calendar_id
        self.add_company_textbox_id = Admin_Locators.add_company_textbox_id
        self.add_tax_exampt_id = Admin_Locators.add_tax_exampt_id
        self.add_newsletter_xpath = Admin_Locators.add_newsletter_xpath
        self.add_role_dropdown_xpath = Admin_Locators.add_role_dropdown_xpath
        self.add_vendor_dropdown_id = Admin_Locators.add_vendor_dropdown_id
        self.add_activeornot_checkbox_id = Admin_Locators.add_activeornot_checkbox_id
        self.add_admincomment_checkbox_id = Admin_Locators.add_admincomment_checkbox_id
        self.save_newcustomer_button_xpath = Admin_Locators.save_newcustomer_button_xpath
        self.savecontinue_newcustomer_button_name = Admin_Locators.savecontinue_newcustomer_button_name
        self.success_message_xpath = Admin_Locators.success_message_xpath

    def enter_add_email(self,email):
        self.driver.find_element_by_id(self.add_email_textbox_id).send_keys(email)

    def enter_add_password(self,password):
        self.driver.find_element_by_id(self.add_password_textbox_id).send_keys(password)

    def enter_add_firstname(self,firstname):
        self.driver.find_element_by_id(self.add_firstname_textbox_id).send_keys(firstname)

    def enter_add_lastname(self,lastname):
        self.driver.find_element_by_id(self.add_lastname_textbox_id).send_keys(lastname)

    def click_add_male(self):
        self.driver.find_element_by_id(self.gender_male_radio_id).click()

    def click_add_female(self):
        self.driver.find_element_by_id(self.gender_female_radio_id).click()

    def enter_add_dob(self,dob):
        self.driver.find_element_by_id(self.add_dob_calendar_id).send_keys(dob)

    def enter_add_company(self,company):
        self.driver.find_element_by_id(self.add_company_textbox_id).send_keys(company)

    def click_add_tax(self):
        self.driver.find_element_by_id(self.add_tax_exampt_id).click()

    def select_newsletter_1(self, newsletter):
        self.driver.find_element_by_xpath(self.add_newsletter_xpath).send_keys(newsletter).send_keys(Keys.RETURN)
        self.driver.build().perform()

    def select_manage_Vendor(self,vendor):
        manage_vendor = Select(self.driver.find_element_by_id(self.add_vendor_dropdown_id))
        manage_vendor.select_by_visible_text(vendor)

    def unclick_active(self):
        self.driver.find_element_by_id(self.add_activeornot_checkbox_id).click()

    def enter_add_comment(self,comment):
        self.driver.find_element_by_id(self.add_admincomment_checkbox_id).send_keys(comment)

    def click_save(self):
        save_button = self.driver.find_element_by_xpath(self.save_newcustomer_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", save_button)
        save_button.click()

    def success_message(self):
        if self.driver.find_element_by_xpath(self.success_message_xpath).text == "The new customer has been added successfully.":
            return True
        else:
            return False

