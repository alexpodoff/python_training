# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from random_generator import mail_generator as mg
from random_generator import name_generator as ng
from random_generator import phone_generator as pg

testdata = [Contact(name="", lastname="", nickname="")] + [
    Contact(name=ng(10), lastname=ng(20), nickname=ng(20), company=ng(30),
            home=pg(), work=pg(), mobile=pg(), phone2=pg(),
            email=mg(10, "@rbt.ru"), email2=mg(12, "@mail.ru"), email3=mg(15, "@gmail.com"), fax=pg(),
            middlename=ng(10), title=ng(10), address=ng(40))
    for i in range(5)
]
# check condition
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_addcontact(app, contact):
    old_contacts = app.contact.get_contact_list()
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
