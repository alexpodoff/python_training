# -*- coding: utf-8 -*-
from application import Application
import pytest
from other_contact import More_contacts
from contact import Contact
from tel import Telephone
from other import Other
from secondary import Secondary
from random_generator import name_generator as ng
from random_generator import phone_generator as pg
from random_generator import mail_generator as mg


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# check mid condition
def test_addcontact(app):
    app.login(username="admin", passwd="secret")
    app.create_new_contact(Contact(name=ng(), lastname=ng(), nickname=ng(),
                                   company=ng()))
    app.confirm()
    app.logout()


# chek min conditioin
def test_addcontact_empty(app):
    app.login(username="admin", passwd="secret")
    app.create_new_contact(Contact(name="", lastname="", nickname="", company=""))
    app.confirm()
    app.logout()


# check full condition
def test_addcontact_full(app):
    app.login(username="admin", passwd="secret")
    app.create_new_contact(Contact(name=ng(), lastname=ng(), nickname=ng(),
                                   company=ng()))
    app.more_contacts(More_contacts(middlename=ng(), title=ng(),
                                    address=ng()))
    app.telephone(Telephone(home=pg(), mobile=pg(), work=pg(),
                            fax=pg()))
    app.other(Other(email1=mg(), email2=mg(), email3=mg(),
                    homepage=ng()))
    app.secondary(Secondary(address=ng(), home=ng(), notes=ng()))
    app.confirm()
    app.logout()
