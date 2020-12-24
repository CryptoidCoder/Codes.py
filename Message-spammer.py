# This file lets you input how many times,you want to send something, and what to send.
# Go onto the command line (Windows: search cmd in start menu)(Linux: ctrl+alt+t)
# and type the following command: 2pip install keyboard"


import keyboard # pip install keyboard
import time

how_many_messages = int(input("How many messages do you want me to spam? "))
message_to_send = input("What message should I send? ")

for i in range (how_many_messages):
    keyboard.write(message_to_send)
    time.sleep(0.1)
    keyboard.press_and_release('enter')
