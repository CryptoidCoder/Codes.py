#This script is to play a sound using python

from playsound import playsound
import os

currentdirectorypath = os.path.dirname(os.path.abspath(__file__))
playsound(f"{currentdirectorypath}\\bombsound-explosion.wav")