# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="new name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="new header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(footer="new footer"))


def test_modify_empty_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="", header="", footer=""))
