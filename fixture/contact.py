from selenium.webdriver.support.select import Select

from model.сontact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.accept_next_alert = True
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # go to home page
        self.open_contacts_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.fill_contact(contact)
        self.fill_addresses(contact)
        self.add_phones(contact)
        self.add_emails(contact)
        self.add_homepade(contact)
        self.birthday(contact)
        self.anniversary(contact)
        self.add_info(contact)

    def edit(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index_edit(index)
        self.fill_contact_form(new_contact_data)
        # submit contact edit
        wd.find_element_by_name("update").click()
        # go to home page
        self.open_contacts_page()
        self.contact_cache = None

    def select_contact_by_index_edit(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("(//img[@alt='Edit'])")[index].click()

    def select_contact_by_index_delete(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index_delete(index)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])[@type='button']").click()
        try:
            alert = wd.switch_to_alert()
            alert.accept()
        finally:
            pass
        self.open_contacts_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.first_name)
        self.type("middlename", contact.middle_name)
        self.type("lastname", contact.last_name)

    def type(self, field_name, text):
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
        if contact.anniversary_day is not None:
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

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def count_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cell_value = element.find_elements_by_css_selector("td")
                last_name = cell_value[1].text
                first_name = cell_value[2].text
                all_phones = cell_value[5].text
                self.contact_cache.append(Contact(contact_id=int(id), last_name=last_name, first_name=first_name,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_css_selector("tr[name=entry]")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_css_selector("tr[name=entry]")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(first_name=first_name, last_name=last_name, contact_id=id,
                       home=home, mobile_phone=mobile, work_phone=work, phone_2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home=home, mobile_phone=mobile, work_phone=work, phone_2=phone2)