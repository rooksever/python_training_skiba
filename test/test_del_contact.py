from model.сontact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(first_name="jjjjjjjjjjjjj"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
