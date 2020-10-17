
import random

chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789!"£$%^&*()_-+=@{[}]~#?/|\¬¦ .<>'

length = int(input('password length?'))

amountofpasswords = int(input('how many passwords?'))

for p in range(amountofpasswords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
