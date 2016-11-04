# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", passwd="secret")
    app.group_creation(Group(name="new", header="mdamd", footer="oodod"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", passwd="secret")
    app.group_creation(Group(name="", header="", footer=""))
    app.logout()
