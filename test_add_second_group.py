# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_second_group(app):
    app.login(username="admin", password="secret")
    app.greate_group(Group(name="second ", header="qwe", footer="asd"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.greate_group(Group(name="", header="", footer=""))
    app.logout()
