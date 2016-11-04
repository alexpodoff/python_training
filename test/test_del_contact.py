

def test_delete_first_contact(app):
    app.session.login(username="admin", passwd="secret")
    app.contact.delete_first_contact()
    app.session.logout()
