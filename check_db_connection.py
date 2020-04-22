import pymysql.cursors
import pymysql.connections
from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group

'''db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_not_in_group(Group(id="212"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass

try:
    groups = db.get_group_list()
    for group in groups:
        print(group)
    print(len(groups))
finally:
    pass'''

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()