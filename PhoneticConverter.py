# To run this use the command `playmessage("your message") in the shell

# imports
from time import sleep # import waiting modules

# The dictionary of pheonetic letters
Alphabet = {
    ' ': '',
    'a': 'alpha',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliet',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu'}

#get the pheonetic for a letter
def letterlookup(stringvalue):
    for k in Alphabet:
        if Alphabet[k] == stringvalue:
            return k
    return " "

# 
def doletter(letter):

    if letter != "": # if letter is actually a letter make currnetletter equal to the pheonetic letter
        currentletter = Alphabet[letter]
        
    if letter == " ": # if letter equals space print ' '
        print("  ")
        return
    
    print(letter + " : " + currentletter) #print letter : morsecode e.g A : sl
        
        
    sleep(0.3)
    
#output the message
def playmessage(message):           
    for c in message:
        doletter(str.lower(c))

while True:
    message = input('What message do you want me to convert into pheoentics? ')
    playmessage(message)

    again = input('Do you want me to convert another message y/n? ')
    if 'n' in again.lower(): #end the program if 'n' or 'N' is given as an input
        break

    if again.lower() == ' ': #end the program if nothing is entered as an input
        break


