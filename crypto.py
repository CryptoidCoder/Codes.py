#functions
def encrypt(message, key):#Encrypt message with key.
    result = '' #blank result

    for letter in message: # Iterate letters in message and encrypt each individually.
        if letter.isalpha():
            num = ord(letter)
            if letter.isupper():
                base = ord('A')
            elif letter.islower():
                base = ord('a')

            num = (num - base + key) % 26 + base # The encryption equation:
            result += chr(num)
        elif letter.isdigit():
            result += letter # TODO: Encrypt digits.
        else:
            result += letter
    return result

def decrypt(message, key): #Decrypt message with key.
    return encrypt(message, -key)

def decode(message): #brute force a message
    pass  # TODO

def get_key():
    try:
        text = input('Enter a key (1 - 25): ')
        key = int(text)
        return key
    except:
        print('Invalid key. Using key: 0.')
        return 0

print('Do you wish to encrypt or decrypt a message?')
choice = input()

if choice == 'encrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Encrypted message:', encrypt(phrase, code))
elif choice == 'decrypt':
    phrase = input('Message: ')
    code = get_key()
    print('Decrypted message:', decrypt(phrase, code))
elif choice == 'decode':
    phrase = input('Message: ')
    print('Decoding message:')
    decode(phrase)
else:
    print('Error: Unrecognized Command')
