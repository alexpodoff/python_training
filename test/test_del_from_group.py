from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_remove_contact_from_group(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
        app.contact.confirm()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    groups = db.get_group_list()
    group = random.choice(groups)
    condition = base.get_contacts_in_group(Group(id=group.id))
    if contact not in condition:
        app.contact.add_contact_to_group(contact.id, group.id)
    app.contact.remove_contact_from_group(contact.id, group.id)
    new_condition = base.get_contacts_in_group(Group(id=group.id))
    assert contact not in new_condition


