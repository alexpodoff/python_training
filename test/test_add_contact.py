# -*- coding: utf-8 -*-
from model.contact import Contact
from model.other import Other
from model.other_contact import Contacts
from model.secondary import Secondary
from model.tel import Telephone
from random_generator import mail_generator as mg
from random_generator import name_generator as ng
from random_generator import phone_generator as pg


# check mid condition
def test_addcontact(app):
    app.contact.create(Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng()))
    app.contact.confirm()


# chek min conditioin
def test_addcontact_empty(app):
    app.contact.create(Contact(name="", lastname="", nickname="", company=""))
    app.contact.confirm()


# check full condition
def test_addcontact_full(app):
    app.contact.create(Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng()))
    app.contact.additional(Contacts(middlename=ng(), title=ng(), address=ng()))
    app.contact.telephone(Telephone(home=pg(), mobile=pg(), work=pg(), fax=pg()))
    app.contact.other(Other(email=mg(), email2=mg(), email3=mg(), homepage=ng()))
    app.contact.secondary(Secondary(address=ng(), home=ng(), notes=ng()))
    app.contact.confirm()
