# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phones(prefix, maxlen):
    symbols = string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", company="",title="", address="", email="",
                    email2="", email3="", homephone="", mobile="", workphone="", secondaryphone="")] + [
    Contact(firstname=random_string("Fname", 15), middlename=random_string("Mname", 15), lastname=random_string("Lname", 15),
            nickname=random_string("nick", 10), company=random_string("company", 20),title=random_string("title", 15),
            address=random_string("address", 30), email=random_string("email", 30), email2=random_string("email2", 30),
            email3=random_string("email3", 30), homephone=random_string_for_phones("+",15), mobile=random_string_for_phones("+",15),
            workphone=random_string_for_phones("+",15), secondaryphone=random_string_for_phones("+",15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

