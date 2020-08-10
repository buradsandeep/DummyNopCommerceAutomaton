from Locators.Locators import Admin_Locators

class Login_Page:


    def __init__(self, driver):
        self.driver = driver
        self.user_textbox = Admin_Locators.email_textbox_id
        self.password_textbox = Admin_Locators.password_textbox_id
        self.login_button = Admin_Locators.login_button_xpath

    def enter_email(self, email):
        self.driver.find_element_by_id(self.user_textbox).clear()
        self.driver.find_element_by_id(self.user_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox).clear()
        self.driver.find_element_by_id(self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

