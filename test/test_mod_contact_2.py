from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact_2(Contact(firstname="First", middlename="1", lastname="Last", nickname="33",
                               company="SSD", title="Mr", adress="Gomel", mobile="+5555555555", email="test3@test3.test"))
    app.contact.return_to_homepage()
    app.session.logout()
