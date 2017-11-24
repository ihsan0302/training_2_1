from model.contact import Contact


def test_modify_first_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="RRR"))
        app.contact.return_to_homepage()
    app.contact.modify_first_contact(Contact(firstname="James"))
    app.contact.return_to_homepage()

def test_modify_first_contact_lastname_middlename(app):
    app.contact.modify_first_contact(Contact(middlename="25", lastname="Muller"))
    app.contact.return_to_homepage()
