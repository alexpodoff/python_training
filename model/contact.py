# module for contacts
from sys import maxsize


class Contact:
    def __init__(self, lastname=None, name=None, nickname=None, company=None, id=None,
                 home=None, mobile=None, work=None, phone2=None, email=None, email2=None, email3=None, fax=None,
                 middlename=None, title=None, address=None, address2=None, notes=None,
                 all_phones_from_home_page=None, all_mail_from_home_page=None):
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.id = id
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.fax = fax
        self.middlename = middlename
        self.title = title
        self.address = address
        self.address2 = address2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mail_from_home_page = all_mail_from_home_page

    def __repr__(self):
        return '%s:"%s":"%s":%s:%s:%s' % (self.id, self.name, self.lastname, self.email, self.email2, self.email3)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
