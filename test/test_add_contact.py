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
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng())
    app.contact.create(contact)
    app.contact.confirm()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# # chek min conditioin
# def test_addcontact_empty(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(name="", lastname="", nickname="", company="")
#     app.contact.create(contact)
#     app.contact.confirm()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#
# # check full condition
# def test_addcontact_full(app):
#     app.contact.create(Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng()))
#     app.contact.additional(Contacts(middlename=ng(), title=ng(), address=ng()))
#     app.contact.telephone(Telephone(home=pg(), mobile=pg(), work=pg(), fax=pg()))
#     app.contact.other(Other(email=mg(), email2=mg(), email3=mg(), homepage=ng()))
#     app.contact.secondary(Secondary(address=ng(), home=ng(), notes=ng()))
#     app.contact.confirm()
