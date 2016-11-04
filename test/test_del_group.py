

def test_delete_first_group(app):
    app.session.login(username="admin", passwd="secret")
    app.group.delete_first_group()
    app.session.logout()
