# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Alex", lastname="Samaryn", nickname="Vano",
                               company="ZPI", title="Sir", adress="Minsk", mobile="123456789", email="test@test.test")
    app.contact.create(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_second_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Jacob", middlename="Kanstantyn", lastname="Kolas", nickname="Lesavik",
#                                company="New Land", title="Sir", adress="Minsk", mobile="+987654321", email="test@kolas.by")
#     app.contact.create(contact)
#     app.contact.return_to_homepage()
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
