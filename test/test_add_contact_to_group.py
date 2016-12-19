from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random


base = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app, db):
    if db.get_contact_list() == 0:
        app.contact.create(Contact(name="test"))
        app.contact.confirm()
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    index = -1
    for i in contacts:
        index = index + 1
        if i.id == contact.id:
            break
    groups = db.get_group_list()
    group = random.choice(groups)
    condition = base.get_contacts_in_group(Group(id=group.id))
    if contact in condition:
        print("already there!")
        # app.contact.remove_contact_from_group(contact.id, group.id)
    print(index)
    print("group name = " + group.name)
    print("contact = " + contact.name)
    app.contact.add_contact_to_group(contact.id, group.id)
    new_condition = base.get_contacts_in_group(Group(id=group.id))
    assert contact in new_condition


