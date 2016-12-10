# -*- coding: utf-8 -*-
from model.contact import Contact


# check condition
def test_addcontact(app, json_contacts):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(json_contacts)
    app.contact.confirm()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(json_contacts)
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
