# -*- coding: utf-8 -*-
from model.group import Group


def test_add_second_group(app):
    app.group.create(Group(name="second ", header="qwe", footer="asd"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
