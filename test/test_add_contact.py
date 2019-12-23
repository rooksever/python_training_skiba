# -*- coding: utf-8 -*-

from model.сontact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(first_name="jdfggggggggggg", middle_name="khjrrrrrrrr", last_name="hrrrrrrrrkj", nickname="jffgh",
                title="hjg hklk", company="hfghf",
                address="f jghkjj jhj gh jj", home="ghjhg", mobile_phone="gfjgh", work_phone="gj", fax="ghj",
                email_1="gfjhgjhg kghfj", email_2="fdhjfg jgjk", email_3="fhj gh",
                homepage="fhj gh", birth_day="16", birth_mon="December", birth_year="1990", anniversary_day="10",
                anniversary_mon="July", anniversary_year="2000", address_2="fgh jjhgjghjghhgj", phone_2="gjghhgj",
                notes="ghjhgjghjh hgjghjghjjhg hgjhgjhgf")
    app.contact.add(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
