import pywhatkit
inputfile = input("What is the path of the input image file? ")
outputfile = input("What is the path of the output image file? ")

pywhatkit.image_to_ascii_art(fr"{inputfile}", fr"{outputfile}")
