# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from other_contact import More_contacts
from contact import Contact
from tel import Telephone
from other import Other
from secondary import Secondary

import random
import string

# generates random name
def name_generator():
    name = ""
    lenght = random.choice(string.digits)
    for i in range(int(lenght)):
        n = random.choice(string.ascii_letters)
        name += n
    return name

# generates random phone
def phone_generator():
    phone = "8"
    for i in range(10):
        n = random.choice(string.ascii_letters)
        phone += n
    return phone

# generates random mail
def mail_generator():
    left = ""
    right = "rbt.ru"
    lenght = random.choice(string.digits)
    for item in range(int(lenght)):
        n = random.choice(string.ascii_letters)
        left += n
    mail = left + "@" + right
    return mail


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd, username, passwd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(passwd)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, wd, contact):
        # name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        # lastname
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # nickname
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)

    def confirm(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_css_selector("div.msgbox").click()

    def more_contacts(self, wd, contact):
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

    def telephone(self, wd, contact):
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)

    def other(self, wd, contacts):
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)

    def secondary(self, wd, contact):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

   # check mid condition
    def test_addcontact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwd="secret")
        self.contact_page(wd)
        self.create_new_contact(wd, Contact(name=name_generator(), lastname=name_generator(), nickname=name_generator(),
                                company=name_generator()))
        self.confirm(wd)
        self.return_home_page(wd)
        self.logout(wd)

    # chek min conditioin
    def test_addcontact_empty(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwd="secret")
        self.contact_page(wd)
        self.create_new_contact(wd, Contact(name="", lastname="", nickname="", company=""))
        self.confirm(wd)
        self.return_home_page(wd)
        self.logout(wd)

    # check full condition
    def test_addcontact_full(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", passwd="secret")
        self.contact_page(wd)
        self.create_new_contact(wd, Contact(name=name_generator(), lastname=name_generator(), nickname=name_generator(),
                                company=name_generator()))
        self.more_contacts(wd, More_contacts(middlename=name_generator(), title=name_generator(),
                                             address=name_generator()))
        self.telephone(wd, Telephone(home= phone_generator(), mobile= phone_generator(), work= phone_generator(),
                                     fax= phone_generator()))
        self.other(wd, Other(email1=mail_generator(), email2=mail_generator(), email3=mail_generator(),
                             homepage=name_generator()))
        self.secondary(wd, Secondary(address=name_generator(), home=name_generator(), notes=name_generator()))
        self.confirm(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
