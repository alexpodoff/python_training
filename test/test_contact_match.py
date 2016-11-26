import re
from random import randrange


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
