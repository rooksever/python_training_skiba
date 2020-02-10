from model.сontact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    if app.contact.count_contacts() == 0:
        app.contact.add(Contact(first_name="jjjjjjjjjjjjj"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="fiiirst", middle_name="miiiddle", last_name="laaast")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_contacts()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(),
                                                                     key=Contact.id_or_max())



