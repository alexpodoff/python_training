# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from random_generator import name_generator as ng


testdata = [Group(name="", header="", footer="")] + [
    Group(name=ng(10), header=ng(20), footer=ng(20))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
