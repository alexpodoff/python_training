
import random
import string

# generates random name
def name_generator(maxlen):
    symbols = string.ascii_letters + string.digits #+ " "*10 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


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
def mail_generator(maxlen, dom):
    symbols = string.ascii_letters + string.digits #+ " "*10 + string.punctuation
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + dom
