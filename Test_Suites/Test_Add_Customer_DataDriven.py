from BaseCode.Add_Customer_ExcelReader import Xlutils
from BaseCode.Admin_Login import Base_Login
from Pages.addcustomer import Add_Customer
from Pages.dashboard import Dashboard_Page
from selenium import webdriver

class Test_Add_Customer:

    def test_add_customer(self):
        driver = webdriver.Chrome(executable_path="C:/PycharmProjects/Driver/chromedriver.exe")
        driver.maximize_window()
        xl_utility = Xlutils("../TestData/Add_Customer.xlsx", "Sheet1")
        total_rows = xl_utility.getExcelrows()
        addcustomer1 = Add_Customer(driver)
        #screenshot_counter = 1
        for r in range(2,total_rows+1):
            email, password, firstname, lastname, gender, dob, company_name, tax_exemption, newsletter, manage_vendor, active, admin_comment = xl_utility.readExcel(r)
            self.login1 = Base_Login(driver)
            self.login1.login()
            driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/Create")
            addcustomer1.enter_add_email(email)
            addcustomer1.enter_add_password(password)
            addcustomer1.enter_add_firstname(firstname)
            addcustomer1.enter_add_lastname(lastname)
            if gender.upper() == "MALE":
                addcustomer1.click_add_male()
            elif gender.upper() == "FEMALE":
                addcustomer1.click_add_female()
            else:
                raise Exception("Incorrect gender value")
            addcustomer1.enter_add_dob(dob)
            addcustomer1.enter_add_company(company_name)
            if tax_exemption.upper() == "YES":
                addcustomer1.click_add_tax()
            elif tax_exemption.upper() == "NO":
                continue
            else:
                raise Exception("Incorrect Tax Value")
            print(newsletter)
            #addcustomer1.select_newsletter_1(newsletter)
            addcustomer1.select_manage_Vendor(manage_vendor)
            driver.execute_script("window.scrollBy(0,800)")
            if active.upper() == "NO":
                addcustomer1.unclick_active()
            else:
                continue
            addcustomer1.enter_add_comment(admin_comment)
            addcustomer1.click_save()
            if addcustomer1.success_message is True:
                xl_utility.writeExcel(r, "Pass")
            else:
                xl_utility.writeExcel(r, "Fail")
            xl_utility.closeExcel()
            logout = Dashboard_Page(driver)
            logout.click_logout()



            #driver.save_screenshot("C:/PycharmProjects/Practice/DDT/ScreenShots/" + "Iteration" +  str(screenshot_counter) + ".png")
            #screenshot_counter += 1

            #submit_button = driver.find_element_by_id("submit")
            #driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            #submit_button.click()
