# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="Ivan", middlename="Alex", lastname="Samaryn", nickname="Vano",
                               company="ZPI", title="Sir", adress="Minsk", mobile="+123456789", email="test@test.test"))
    app.contact.return_to_homepage()

def test_add_second_contact(app):
    app.contact.create(Contact(firstname="Jacob", middlename="Kanstantyn", lastname="Kolas", nickname="Lesavik",
                               company="New Land", title="Sir", adress="Minsk", mobile="+987654321", email="test@kolas.by"))
    app.contact.return_to_homepage()
