import re


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.email, contact.email2, contact.email3]))))


def merge_name_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.first_name, contact.middle_name,
                                                            contact.last_name]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home, contact.mobile, contact.work,
                                                            contact.phone2]))))


def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_db = db.get_contact_list()
    assert contact_from_home_page == contact_from_db

    emails = contact_from_home_page.all_emails_from_home_page
    e = clear(emails)
    assert e == merge_emails_like_on_home_page(contact_from_db)
    assert contact_from_home_page(2) == contact_from_db(2)
    assert contact_from_home_page.last_name == contact_from_db.last_name
    assert contact_from_home_page.address == contact_from_db.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)



