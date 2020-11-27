#a script for a raspberry pi to be used as bicycle indicators

import time # so we can wait between LED on and off
import RPi.GPIO as GPIO #so we can use GPIO's

#ledpin variable enter what pin the LED is in below
leftledpin = 2 #pin number for right LED
rightledpin = 3 #pin number for left LED
leftswitchinputpin = 15 #pin number for switch (in left position)
rightswitchinputpin = 14 #pin number for switch (in right position)
buttoninputpin = 18 #pin number for button
ledflashtime = 0.5 #the time between each led flash (seconds)

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(leftledpin, GPIO.OUT) # set leftledpin as an output pin
GPIO.setup(rightledpin, GPIO.OUT) # set rightledpin as an output pin
GPIO.setup(buttoninputpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set buttoninputpin to be an input pin and set initial value to be pulled low (off)
GPIO.setup(leftswitchinputpin, GPIO.IN) #set leftswitchinputpin to be an input
GPIO.setup(rightswitchinputpin, GPIO.IN) #set rightswitchinputpin to be an input

def flashonce(text):
    GPIO.output(text, GPIO.HIGH)
    time.sleep(ledflashtime)
    GPIO.output(text, GPIO.LOW)
    time.sleep(ledflashtime) #definition for the named pin to turn on then wait then turn off then wait

def flashtwice(text):
    GPIO.output(text, GPIO.HIGH)
    time.sleep(ledflashtime)
    GPIO.output(text, GPIO.LOW)
    time.sleep(ledflashtime)
    GPIO.output(text, GPIO.HIGH)
    time.sleep(ledflashtime)
    GPIO.output(text, GPIO.LOW)
    time.sleep(ledflashtime)#definition for the named pin to turn on then wait then turn off then wait then turn on then wait then turn off then wait

def flashalways(text):
    try:
        GPIO.output(text, GPIO.HIGH)
        time.sleep(ledflashtime)
        GPIO.output(text, GPIO.LOW)
        time.sleep(ledflashtime)
    except GPIO.input(buttoninputpin) == GPIO.HIGH:
        GPIO.output(rightledpin, GPIO.LOW)
        GPIO.output(leftledpin, GPIO.LOW) #definition for the named pin to flash on and off until the button is pressed again

while True: 
    if GPIO.input(buttoninputpin) == GPIO.HIGH: #detect when button is pressed
        if GPIO.input(leftswitchinputpin) == GPIO.HIGH: #detect if switch is to left
            flashalways(leftledpin) #flash left led until button is pressed again
            time.sleep(ledflashtime)
        elif GPIO.input(rightswitchinputpin) == GPIO.HIGH: #detect if switch is to right
            flashalways(rightledpin) # flash righ tled until button is pressed again
            time.sleep(ledflashtime) #definition to always look for the button input then depending on which way the switch is flash either the Left or Right LED
