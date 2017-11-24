class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_fields_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_fields_value("firstname", contact.firstname)
        self.change_fields_value("middlename", contact.middlename)
        self.change_fields_value("lastname", contact.lastname)
        self.change_fields_value("nickname", contact.nickname)
        self.change_fields_value("company", contact.company)
        self.change_fields_value("title", contact.title)
        self.change_fields_value("address", contact.adress)
        self.change_fields_value("mobile", contact.mobile)
        self.change_fields_value("email", contact.email)

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # edit contact form
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_name("update").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact_2(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # show first contact details
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        # edit contact form
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_name("update").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
