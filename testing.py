import winsound
import time
import sys, termios, tty, os
# import modules

pitch = int(input('What is the pitch you want all the Morse code to be in? {between 300 and 1000}'))
soundvisual = int(input('Sound will always play, do you want visuals aswell? 1 if yes 0 if no'))
if soundvisual == 1:
    visualtype = int(input('Do you want the visuals to be as words(dot + dash) or as characters (* + -). 1 if words 0 if characters.'))
    if visualtype == 1:
        def visualdot():
            print ('dot')

        def visualdash():
            print('dash')

    if visualtype == 0:
        def visualdot():
            print(' *')

        def visualdash():  
            print(' -')
    
def dot():
    winsound.Beep(pitch,100)
    time.sleep(0.7)
    if soundvisual == 1:
        visualdot()

def dash():
    winsound.Beep(pitch,1000)
    time.sleep(0.7)
    if soundvisual == 1:
        visualdash()
# determine definitions to make it easier

print('definitions of sound complete')

dot()
dash()
print('sound test complete')


def a():
    dot()
    dash()

def b():
    dash()
    dot()
    dot()
    dash()

def c():
    dash()
    dot()
    dash()
    dot()

def d():
    dash()
    dot()
    dash()

def e():
    dot()

def f():
    dot()
    dot()
    dash()
    dot()

def g():
    dash()
    dash()
    dot()

def h():
    dot()
    dot()
    dot()
    dot()

def i():
    dot()
    dot()

def j():
    dot()
    dash()
    dash()
    dash()
    
def k():
    dash()
    dot()
    dash()

def l():
    dot()
    dash()
    dot()
    dot()

def m():
    dash()
    dash()

def n():
    dash()
    dot()

def o():
    dash()
    dash()
    dash()

def p():
    dot()
    dash()
    dash()
    dot()

def q():
    dash()
    dash()
    dot()
    dash()

def r():
    dot()
    dash()
    dot()

def s():
    dot()
    dot()
    dot()

def t():
    dash()

def u():
    dot()
    dot()
    dash()

def v():
    dot()
    dot()
    dot()
    dash()

def w():
    dot()
    dash()
    dash()

def x():
    dash()
    dot()
    dot()
    dash()

def y():
    dash()
    dot()
    dash()
    dash()

def z():
    dash()
    dash()
    dot()
    dot()

def num1():
    dot()
    dash()
    dash()
    dash()
    dash()

def num2():
    dot()
    dot()
    dash()
    dash()
    dash()

def num3():
    dot()
    dot()
    dot()
    dash()
    dash()

def num4():
    dot()
    dot()
    dot()
    dot()
    dash()

def num5():
    dot()
    dot()
    dot()
    dot()
    dot()

def num6():
    dash()
    dot()
    dot()
    dot()
    dot()

def num7():
    dash()
    dash()
    dot()
    dot()
    dot()

def num8():
    dash()
    dash()
    dash()
    dot()
    dot()

def num9():
    dash()
    dash()
    dash()
    dash()
    dot()

def num0():
    dash()
    dash()
    dash()
    dash()
    dash()

    
# defining the numers 1-9-0 and the letters a-z
# if you want to add punctuation then add it here using the same technique

print('definitions of letters done')

def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
        
while true:
        char = getch()
        if (char == "q"):
                exit(0)
        if (char == "a"):
                a()


