from model.contact import Contact
from random import randrange


def test_modify_some_contact_2(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jacob", middlename="Kanstantyn", lastname="Kolas", nickname="Lesavik",
                               company="New Land", title="Sir", adress="Minsk", mobilephone="+987654321", email="test@kolas.by"))
        app.contact.return_to_homepage()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="South", lastname="North")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index_2(index,contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
