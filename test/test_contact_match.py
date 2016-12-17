import re
from random import randrange
from model.contact import Contact


def test_all_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_mail_from_home_page == merge_mail_like_on_home_page(contact_from_edit_page)
    assert merge_names(contact_from_home_page.name, contact_from_home_page.lastname) == \
           merge_names(contact_from_edit_page.name, contact_from_edit_page.lastname)


def test_phones_on_contact_view_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_phones_like_on_home_page(contact_from_view_page) == \
           merge_phones_like_on_home_page(contact_from_edit_page)


def test_match_with_db(app, db):
    contacts_from_db = db.get_contact_list()
    phone_list_from_db = db.phones_from_db()
    email_liset_from_db = db.emails_from_db()
    phone_list = []
    for phone in phone_list_from_db:
        phone_list.append(merge_phones_like_on_home_page(phone))
    email_list = []
    for email in email_liset_from_db:
        email_list.append(merge_mail_like_on_home_page(email))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    phones_from_home_page = [con.all_phones_from_home_page for con in contacts_from_home_page]
    emails_from_home_page = [con.all_mail_from_home_page for con in contacts_from_home_page]
    assert phone_list == phones_from_home_page
    assert email_list == emails_from_home_page
    assert contacts_from_db == contacts_from_home_page


def merge_names(name, lastname):
    return "%s%s" % (name, lastname)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_mail_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email, contact.email2, contact.email3])))
