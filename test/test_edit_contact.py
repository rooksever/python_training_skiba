from model.сontact import Contact

def test_add_contact(app):
    app.contact.edit(Contact(first_name="wwwwwwwwwww", middle_name="sssssssssss", last_name="xxxxxxxxxx", nickname="", title="", company="",
                            address="", home="", mobile_phone="", work_phone="", fax="", email_1="", email_2="", email_3="",
                            homepage="", birth_day="", birth_mon="", birth_year="", anniversary_day="", anniversary_mon="", anniversary_year="", address_2="", phone_2="",
                            notes=""))
    app.session.logout()





