from model.сontact import Contact


def test_edit_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(first_name="jjjjjjjjjjjjj"))
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="wwwwwwwwwww", middle_name="sssssssssss", last_name="xxxxxxxxxx")
    app.contact.edit(contact)
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

