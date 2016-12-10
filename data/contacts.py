from model.contact import Contact
from random_generator import mail_generator as mg
from random_generator import name_generator as ng
from random_generator import phone_generator as pg


testdata = [
    Contact(name="name1", lastname="lastname1", nickname="nickname1", company=ng(30),
             home=pg(), work=pg(), mobile=pg(), phone2=pg(),
             email=mg(10, "@rbt.ru"), email2=mg(12, "@mail.ru"), email3=mg(15, "@gmail.com"), fax=pg(),
            middlename=ng(10), title=ng(10), address=ng(40)),
    Contact(name="name2", lastname="lastname2", nickname="nickname2", company=ng(30),
             home=pg(), work=pg(), mobile=pg(), phone2=pg(),
             email=mg(10, "@rbt.ru"), email2=mg(12, "@mail.ru"), email3=mg(15, "@gmail.com"), fax=pg(),
            middlename=ng(10), title=ng(10), address=ng(40))
]


# testdata = [Contact(name="", lastname="", nickname="")] + [
#     Contact(name=ng(10), lastname=ng(20), nickname=ng(20), company=ng(30),
#             home=pg(), work=pg(), mobile=pg(), phone2=pg(),
#             email=mg(10, "@rbt.ru"), email2=mg(12, "@mail.ru"), email3=mg(15, "@gmail.com"), fax=pg(),
#             middlename=ng(10), title=ng(10), address=ng(40))
#     for i in range(5)
# ]
