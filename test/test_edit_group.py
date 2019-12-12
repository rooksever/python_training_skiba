from model.group import Group

def test_edit_first_contact(app):
    if app.group.count_groups() == 0:
        app.group.create(Group(name = "test", header="test", footer="test"))
    app.group.edit_first_group(Group(name="qqqqqqqqqq", header="aaaaaaaaaa", footer="zzzzzzzz"))

