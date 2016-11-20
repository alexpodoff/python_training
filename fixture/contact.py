from model.contact import Contact


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

    def delete_first_contact(self):
        wd = self.app.wd
        self.contact_page()
        # select 1st contact
        wd.find_element_by_name("selected[]").click()
        # submit delition
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def confirm(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_css_selector("div.msgbox").click()
        self.contact_page()

    def fill_conact_form(self, contact):
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("company", contact.company)

    def fill_additional_form(self, contact):
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.address)

    def fill_telephone_form(self, contact):
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

    def fill_other_form(self, contact):
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)

    def fill_secondary_form(self, contact):
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("notes", contact.notes)

    def additional(self, new_contact_data):
        self.fill_additional_form(new_contact_data)

    def telephone(self, new_contact_data):
        self.fill_telephone_form(new_contact_data)

    def other(self, new_contact_data):
        self.fill_other_form(new_contact_data)

    def secondary(self, new_contact_data):
        self.fill_secondary_form(new_contact_data)

    def modify(self, new_contact_data):
        wd = self.app.wd
        self.contact_page()
        # select 1st contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_conact_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()

    def modify_additional(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_additional_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()

    def modify_telephone(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_telephone_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()

    def modify_other(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_other_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()

    def modify_secondary(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_secondary_form(new_contact_data)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.contact_page()

    def count(self):
        wd = self.app.wd
        self.contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.contact_page()
        contacts = []
        rows = wd.find_elements_by_name("entry")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
           # name = cells[1].text
            contacts.append(Contact(id=id))
        return contacts
