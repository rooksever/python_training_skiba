from sys import maxsize

class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile_phone=None, work_phone=None, fax=None, email_1=None, email_2=None,
                 email_3=None, homepage=None, birth_day=None, birth_mon=None, birth_year=None, anniversary_day=None,
                 anniversary_mon=None, anniversary_year=None, address_2=None, phone_2=None, notes=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None, fullname=None, contact_id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile_phone
        self.work = work_phone
        self.fax = fax
        self.email = email_1
        self.email2 = email_2
        self.email3 = email_3
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_mon = birth_mon
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_mon = anniversary_mon
        self.anniversary_year = anniversary_year
        self.address2 = address_2
        self.phone2 = phone_2
        self.notes = notes
        self.id = contact_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.fullname = fullname

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize




