
import random

characterset = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789!"£$%^&*()_-+=@{[}]~#?/|\¬¦ .<>'

excluded_charcters = input("Any characters Not Allowed (Leave Blank For No)? ")

chars = characterset
for char in excluded_charcters:
    chars = characterset.replace(char, "") #remove excluded character from characterset

length = int(input('Password Length? '))

amountofpasswords = int(input('How Many Passwords? '))

for p in range(amountofpasswords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
