from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.contact_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_conact_form(contact)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.contact_page()
        # select 1st contact
        self.select_contact_by_index(index)
        # submit delition
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.contact_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.contact_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        self.contact_page()

    def remove_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.contact_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//form[@id='right']/select//option[@value='%s']" % group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.contact_page()
        wd.find_element_by_xpath("//select[@name='group']/option[text()='[all]']").click()

    def confirm(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_css_selector("div.msgbox").click()
        self.contact_page()
        self.contact_cache = None

    def fill_conact_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.address)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("notes", contact.notes)

    def modify_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.contact_page()
        self.open_contact_edit_page_by_index(index)
        self.fill_conact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()
        self.contact_cache = None

    def modify_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.contact_page()
        self.open_contact_edit_page_by_id(id)
        self.fill_conact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None
    tel_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_page()
            self.contact_cache = []
            self.tel_cache = []
            rows = wd.find_elements_by_name("entry")
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                name = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                all_mail = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(id=id, name=name, lastname=lastname, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_mail_from_home_page=all_mail))
        return list(self.contact_cache)

    def open_contact_edit_page_by_id(self, id):
        wd = self.app.wd
        self.contact_page()
        rows = wd.find_elements_by_name("entry")
        index = -1
        for element in rows:
            index = index + 1
            if element == id:
                break
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_edit_page_by_index(self, index):
        wd = self.app.wd
        self.contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_page_by_index(index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(name=name, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       address=address, email=email, email2=email2, email3=email3)

    def is_there(self, part, s):
        if part in s:
            return re.search(part + " (.*)", s).group(1)
        else:
            return None

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        home = self.is_there("H:", text)
        mobile = self.is_there("M:", text)
        work = self.is_there("W:", text)
        phone2 = self.is_there("P:", text)
        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)
