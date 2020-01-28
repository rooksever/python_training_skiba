from model.сontact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptErrors as err:
    getopt.usage
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))