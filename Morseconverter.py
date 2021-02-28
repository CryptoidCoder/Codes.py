# To run this use the command `playmessage("your message") in the shell

# imports
from time import sleep # import waiting modules

# Create a dictionary of Morse Code. s is for Short (or dots), l is for Long (or dashes)
MorseCodes = {
    ' ': '',
    'a': 'sl',
    'b': 'lsss',
    'c': 'lsls',
    'd': 'lss',
    'e': 's',
    'f': 'ssls',
    'g': 'lls',
    'h': 'ssss',
    'i': 'ss',
    'j': 'slll',
    'k': 'lsl',
    'l': 'slss',
    'm': 'll',
    'n': 'ls',
    'o': 'lll',
    'p': 'slls',
    'q': 'llsl',
    'r': 'sls',
    's': 'sss',
    't': 'l',
    'u': 'ssl',
    'v': 'sssl',
    'w': 'sll',
    'x': 'lssl',
    'y': 'lsll',
    'z': 'llss',
    '1': 'sllll',
    '2': 'sslll',
    '3': 'sssll',
    '4': 'ssssl',
    '5': 'sssss',
    '6': 'lssss',
    '7': 'llsss',
    '8': 'lllss',
    '9': 'lllls',
    '0': 'lllll'}


#get the morse for a letter
def letterlookup(stringvalue):
    for k in MorseCodes:
        if MorseCodes[k] == stringvalue:
            return k
    return " "

# output the morse to the leds
def doletter(letter):

    if letter != "": # if letter is actually a letter make currnetletter equal to the morse code
        currentletter = MorseCodes[letter]
        
    if letter == " ": # if letter equals space print '//'
        print(" // ")
        return
    
    print(letter + " : " + currentletter) #print letter : morsecode e.g A : sl
        
        
    sleep(0.6)

#output the message
def playmessage(message):           
    for c in message:
        doletter(str.lower(c))
