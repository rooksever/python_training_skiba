# -*- coding: utf-8 -*-

from model.сontact import Contact
    
def test_add_contact(app):
    app.contact.add(Contact(first_name="jhk jhk hjk lh", middle_name="khj kgfkghj", last_name="hgj ghkhkj", nickname="jffgh", title="hjg hklk", company="hfghf",
                            address="f jghkjj jhj gh jj", home="ghjhg", mobile_phone="gfjgh", work_phone="gj", fax="ghj", email_1="gfjhgjhg kghfj", email_2="fdhjfg jgjk", email_3="fhj gh",
                            homepage="fhj gh", birth_day="16", birth_mon="December", birth_year="1990", anniversary_day="10", anniversary_mon="July", anniversary_year="2000", address_2="fgh jjhgjghjghhgj", phone_2="gjghhgj",
                            notes="ghjhgjghjh hgjghjghjjhg hgjhgjhgf"))
    app.session.logout()

