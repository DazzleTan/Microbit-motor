# Microbit-motor
# Simple micro python script to control a hacked lego motor with a microbit and kiktronic motor board

from microbit import *

def motor1( command ):
    "Tell the motor 1 output to do command"
    
    if command == 'go':
        pin8.write_digital(1)
        pin12.write_digital(0)
    elif command == 'back':
        pin8.write_digital(0)
        pin12.write_digital(1)
    elif command == 'stop':
        pin8.write_digital(0)
        pin12.write_digital(0)      
    
    return

def forward():
    motor1('go')
    display.show(Image.ARROW_N)
    sleep(2000)
    motor1('stop')
    return

def reverse():
    motor1('back')
    display.show(Image.ARROW_S)
    sleep(2000)
    motor1('stop')
    return 
    
while True:
    display.show(Image.HEART)
    sleep(2000)
    while True:
        if button_a.was_pressed():
            forward()
        elif button_b.was_pressed():
            reverse()
        display.show(Image.HEART)
        sleep(100)
