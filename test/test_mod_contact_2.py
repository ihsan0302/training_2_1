from model.contact import Contact
import random


def test_modify_some_contact_2(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="RRR222"))
        app.contact.return_to_homepage()
    old_contacts = db.get_contact_list()
    contact_modify = random.choice(old_contacts)
    contact = Contact(firstname="South", lastname="North")
    contact.id = contact_modify.id
    app.contact.modify_contact_by_id_2(contact_modify.id, contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact_modify)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)