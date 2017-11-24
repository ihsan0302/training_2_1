from model.contact import Contact


def test_modify_first_contact_nickname(app):
    app.contact.modify_first_contact_2(Contact(nickname="33"))
    app.contact.return_to_homepage()
