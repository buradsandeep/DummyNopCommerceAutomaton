
class Admin_Locators:

    #Admin Page first Sign in page
    email_textbox_id = "Email"
    password_textbox_id = "Password"
    rememberme_checkbox_id = "RememberMe"
    login_button_xpath = "//input[@class='button-1 login-button']"

    #DashBoard
    customerexpand_xpath = "/html/body/div[3]/div[2]/div/ul/li[4]/a/i[2]"
    customer_link_xpath = "//span[@class='menu-item-title']"
    logout_link_text = "Logout"

    #Customers Page -> Customers -> Search Customer
    searchemail_textbox_id = "SearchEmail"
    searchcompany_texbox_id = "SearchCompany"
    searchfirstname_textbox_id = "SearchFirstName"
    searchidadd_texbox_id = "SearchIpAddress"
    searchlastname_textbox_id = "SearchLastName"
    searchrole_dropdown_id = "SelectedCustomerRoleIds_taglist"
    dob_month_dropdown_id = "SearchMonthOfBirth"
    dob_day_dropdown_id = "SearchDayOfBirth"
    search_button_id = "search-customers"
    addnew_button_xpath = "//a[@class='btn bg-blue']"
    expand_export_class = "btn btn-success dropdown-toggle"
    export_dropdown_xpath = "/html/body/div[3]/div[3]/div/form[1]/div[1]/div/div/button[2]"
    exportxml_all_link_xpath = "//button[@name='exportxml-all']"
    exportxml_selected_link_id = "exportxml-selected"
    exportexcel_all_link_xpath = "//button[@name='exportexcel-all']"
    exportexcel_selected_link_id = "exportexcel-selected"
    show_dropdown_name ="customers-grid_length"



    #Add New Customer
    add_email_textbox_id = "Email"
    add_password_textbox_id = "Password"
    add_firstname_textbox_id = "FirstName"
    add_lastname_textbox_id = "LastName"
    gender_male_radio_id = "Gender_Male"
    gender_female_radio_id = "Gender_Female"
    add_dob_calendar_id = "DateOfBirth"
    add_company_textbox_id = "Company"
    add_tax_exampt_id = "IsTaxExempt"
    add_newsletter_xpath="//*[@id='customer-info']/div[2]/div[1]/div[9]/div[2]/div/div[1]"
    add_role_dropdown_xpath = "//*[@id='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]"
    add_vendor_dropdown_id = "VendorId"
    add_activeornot_checkbox_id = "Active"
    add_admincomment_checkbox_id = "AdminComment"
    save_newcustomer_button_xpath = "//button[@name='save']"
    savecontinue_newcustomer_button_name = "save-continue"
    success_message_xpath = "/html/body/div[3]/div[3]/div[1]"
