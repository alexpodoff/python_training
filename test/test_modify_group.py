# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", passwd="secret")
    app.group.modify(Group(name="new", header="mdamd", footer="oodod"))
    app.session.logout()


def test_modify_empty_group(app):
    app.session.login(username="admin", passwd="secret")
    app.group.modify(Group(name="", header="", footer=""))
    app.session.logout()
