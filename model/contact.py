# module for contacts
from sys import maxsize


class Contact:
    def __init__(self, lastname=None, name=None, nickname=None, company=None, id=None):
        self.name = name
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.id = id

    def __repr__(self):
        return '%s:"%s":"%s"' % (self.id, self.name, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
