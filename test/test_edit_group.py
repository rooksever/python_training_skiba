
from model.group import Group

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="qqqqqqqqqq", header="aaaaaaaaaa", footer="zzzzzzzz"))
    app.session.logout()


