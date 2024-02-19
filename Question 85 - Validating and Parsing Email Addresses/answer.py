import email.utils
import re

n = int(input())
for _ in range(n):
    name, login = email.utils.parseaddr(input())
    if bool(re.match(r"^[a-zA-Z0-9]+[a-zA-Z0-9\-_.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$", login)):
        print(email.utils.formataddr((name, login)))
