from model.contact import Contact


def test_modify_first_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jacob", middlename="Kanstantyn", lastname="Kolas", nickname="Lesavik",
                               company="New Land", title="Sir", adress="Minsk", mobile="+987654321", email="test@kolas.by"))
        app.contact.return_to_homepage()
    app.contact.modify_first_contact_2(Contact(nickname="  "))
    app.contact.return_to_homepage()
