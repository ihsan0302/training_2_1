from model.contact import Contact

def test_add_new_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Empty"))
        app.contact.return_to_homepage()
    app.contact.delete_first_contact()