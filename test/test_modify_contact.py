from model.contact import Contact
from model.other import Other
from model.other_contact import Contacts
from model.secondary import Secondary
from model.tel import Telephone
from random_generator import mail_generator as mg
from random_generator import name_generator as ng
from random_generator import phone_generator as pg


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
        app.contact.confirm()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng())
    contact.id = old_contacts[0].id
    app.contact.modify(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_empty_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="test"))
#         app.contact.confirm()
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify(Contact(name="", lastname="", nickname="", company=""))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)

# def test_modify_full_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(name="test"))
#         app.contact.confirm()
#     app.contact.modify(Contact(name=ng(), lastname=ng(), nickname=ng(), company=ng()))
#     app.contact.modify_additional(Contacts(middlename=ng(), title=ng(), address=ng()))
#     app.contact.modify_telephone(Telephone(home=pg(), mobile=pg(), work=pg(), fax=pg()))
#     app.contact.modify_other(Other(email=mg(), email2=mg(), email3=mg(), homepage=ng()))
#     app.contact.modify_secondary(Secondary(address=ng(), home=ng(), notes=ng()))
