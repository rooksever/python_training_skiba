# -*- coding: utf-8 -*-

from model.сontact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbols = string.digits + " " * 3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=random_string("first_name", 15), middle_name=random_string("middle_name", 15),
                    last_name=random_string("last_name", 15), nickname=random_string("nickname", 20),
                    title=random_string("title", 20), company=random_string("company", 20),
                    address=random_string("address", 40), home=random_string("home", 40),
                    mobile_phone=random_number("mobile_phone", 10), work_phone=random_number("work_phone", 10),
                    fax=random_number("fax", 10), email_1=random_string("email_1", 15),
                    email_2=random_string("email_2", 15), email_3=random_string("email_3", 15),
                    homepage=random_string("homepage", 20), birth_day=random.randint(1, 12),
                    birth_mon=random.randint(1, 12),
                    birth_year=random.randint(1910, 2020), anniversary_day=random.randint(1, 30),
                    anniversary_mon=random.randint(1, 12), anniversary_year=random.randint(1910, 2020),
                    address_2=random_string("address_2", 40), phone_2=random_number("phone_2", 10),
                    notes=random_string("notes", 40))
            for i in range(2)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(contact)
    assert len(old_contacts) + 1 == app.contact.count_contacts()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
