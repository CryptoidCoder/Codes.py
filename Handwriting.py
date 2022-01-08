import pywhatkit
text = input("What text would you like to turn into handwriting? ")
fileoutput = input("Where would you like the handwriting image to be saved to? ")
pywhatkit.text_to_handwriting(text, fileoutput)
