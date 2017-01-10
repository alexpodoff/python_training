from model.contact import Contact
import random


def test_modify_first_contact(app, db, json_contacts, check_ui):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
        app.contact.confirm()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = -1
    for i in old_contacts:
        index = index + 1
        if i.id == contact.id:
            break
    app.contact.modify_by_id(contact.id, json_contacts)
    new_contacts = db.get_contact_list()
    json_contacts.id = contact.id
    old_contacts[index] = json_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(
            new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
