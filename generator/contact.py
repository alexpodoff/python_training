from model.contact import Contact
from random_generator import mail_generator as mg
from random_generator import name_generator as ng
from random_generator import phone_generator as pg
import jsonpickle
import os.path
import getopt
import sys


try:
   opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contact", "file"])
except getopt.GetoptError as arr:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Contact(name="", lastname="", nickname="")] + [
    Contact(name=ng(10), lastname=ng(20), nickname=ng(20), company=ng(30),
            home=pg(), work=pg(), mobile=pg(), phone2=pg(),
            email=mg(10, "@rbt.ru"), email2=mg(12, "@mail.ru"), email3=mg(15, "@gmail.com"), fax=pg(),
            middlename=ng(10), title=ng(10), address=ng(40))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
