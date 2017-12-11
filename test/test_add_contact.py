# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones(prefix, maxlen):
    symbols = string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="",title="", address="", email="",
                    email2="", email3="", homephone="", mobile="", workphone="", secondaryphone="")] + [
    Contact(firstname=random_string("Fname", 15), middlename=random_string("Mname", 15), lastname=random_string("Lname", 15),
            nickname=random_string("nick", 10), company=random_string("company", 20),title=random_string("title", 15),
            address=random_string("address", 30), email=random_string("email", 30), email2=random_string("email2", 30),
            email3=random_string("email3", 30), homephone=random_string_for_phones("+",15), mobile=random_string_for_phones("+",15),
            workphone=random_string_for_phones("+",15), secondaryphone=random_string_for_phones("+",15))
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

