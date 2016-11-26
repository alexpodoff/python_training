
import random
import string

# generates random name
def name_generator():
    name = ""
    lenght = random.choice(string.digits)
    for i in range(int(lenght)):
        n = random.choice(string.ascii_letters)
        name += n
    return name


# generates random phone
def phone_generator():
    phone = random.choice("8+(")
    for i in range(10):
        n = random.choice(string.digits)
        phone += n
    if phone[0] == "(":
        phone = phone[0:4] + ")" + phone[4:]
    if phone[0] == "+":
        phone = phone[0] + "7495" + phone[5:]
    return phone


# generates random mail
def mail_generator():
    left = ""
    right = "rbt.ru"
    lenght = random.choice(string.digits)
    for item in range(int(lenght)):
        n = random.choice(string.ascii_letters)
        left += n
    mail = left + "@" + right
    return mail
