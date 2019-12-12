from model.сontact import Contact


def test_edit_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(first_name="jjjjjjjjjjjjj"))
    app.contact.edit(
        Contact(first_name="wwwwwwwwwww", middle_name="sssssssssss", last_name="xxxxxxxxxx"))