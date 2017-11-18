from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Tomas", middlename="25", lastname="Muller", nickname="13",
                               company="Bayern", title="Herr", adress="Munchen", mobile="+444455555", email="test2@test2.test"))
    app.contact.return_to_homepage()
    app.session.logout()
