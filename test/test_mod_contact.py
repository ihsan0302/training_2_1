from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="RRR"))
        app.contact.return_to_homepage()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="West", lastname="East")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # def test_modify_first_contact_lastname_middlename(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.modify_first_contact(Contact(middlename="25", lastname="Muller"))
#     app.contact.return_to_homepage()
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)