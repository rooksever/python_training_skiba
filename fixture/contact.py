from selenium.webdriver.support.select import Select
from model.сontact import Contact


class ContactHelper:

    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app

    def add(self, Contact):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
           wd.find_element_by_link_text("home").click()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # go to home page
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, Contact):
        wd = self.app.wd
        self.fill_contact(Contact)
        self.fill_addresses(Contact)
        self.add_phones(Contact)
        self.add_emails(Contact)
        self.add_homepade(Contact)
        self.birthday(Contact)
        self.anniversary(Contact)
        self.add_info(Contact)

    def edit(self, new_contact_data):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
           wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # open edit form
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        # fill edit info
        self.fill_contact_form(new_contact_data)
        # submit contact edit
        wd.find_element_by_name("update").click()
        # go to home page
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
           wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])[@type='button']").click()
        try:
            alert = wd.switch_to_alert()
            alert.accept()
        finally:
            pass

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.first_name)
        self.type("middlename", contact.middle_name)
        self.type("lastname", contact.last_name)

    def type(self, field_name,  text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_attributes(self, contact):
        wd = self.app.wd
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company)

    def fill_addresses(self, contact):
        wd = self.app.wd
        self.type("address", contact.address)
        self.type("home", contact.home)

    def add_phones(self, contact):
        wd = self.app.wd
        self.type("mobile", contact.mobile)
        self.type("work", contact.work)
        self.type("fax", contact.fax)

    def add_emails(self, contact):
        wd = self.app.wd
        self.type("email", contact.email)
        self.type("email2", contact.email2)
        self.type("email3", contact.email3)

    def add_homepade(self, contact):
        wd = self.app.wd
        self.type("homepage", contact.homepage)

    def birthday(self, contact):
        wd = self.app.wd
        if contact.birth_day is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[18]").click()
        if contact.birth_mon is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_mon)
        if contact.birth_year is not None:
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[46]").click()
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(contact.birth_year)

    def anniversary(self, contact):
        wd = self.app.wd
        if contact.anniversary_day is  not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[12]").click()
        if contact.anniversary_mon is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_mon)
            wd.find_element_by_xpath(
                "(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[41]").click()
        if contact.anniversary_year is not None:
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)

    def add_info(self, contact):
        wd = self.app.wd
        self.type("address2", contact.address2)
        self.type("phone2", contact.phone2)
        self.type("notes", contact.notes)

    def count_contacts(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
           wd.find_element_by_link_text("home").click()
        return len(wd.find_elements_by_name("selected[]"))




