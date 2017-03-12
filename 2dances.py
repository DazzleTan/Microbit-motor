from microbit import *

def motor1( command ):
    "Tell the motor 1 output to do command"
    
    if command == 'forward':
        pin8.write_digital(1)
        pin12.write_digital(0)
    elif command == 'reverse':
        pin8.write_digital(0)
        pin12.write_digital(1)
    elif command == 'stop':
        pin8.write_digital(0)
        pin12.write_digital(0)      
    
    return

def motor2( command ):
    "Tell the motor 2 output to do command"
    
    if command == 'forward':
        pin0.write_digital(1)
        pin16.write_digital(0)
    elif command == 'reverse':
        pin0.write_digital(0)
        pin16.write_digital(1)
    elif command == 'stop':
        pin0.write_digital(0)
        pin16.write_digital(0)      
    
    return


def forwards():
    "Tell both motors to go forwards"
    
    display.show('F')
    motor1('forward')
    motor2('reverse')
    
    return


def left():
    "Turn Left"
    display.show('L')
    motor1('forward')
    motor2('forward')
    
    return

def right():
    "Turn Right"
    display.show('R')
    motor1('reverse')
    motor2('reverse')
    
    return



def stop():
    "Stop"
    
    display.show('S')
    motor1('stop')
    motor2('stop')
    
    return


def dance1():
    "Dance 1"
    
    forwards()
    sleep(1000)
    left()
    sleep(500)
    right()
    sleep(500)
    stop()
    display.show(Image.XMAS)
    sleep(1000)
    right()
    sleep(300)

    return


def dance2():
    forwards()
    display.show(Image.TARGET)
    sleep(1000)
    left()
    display.show(Image.ARROW_W)
    sleep(3000)
    stop()
    display.show(Image.TARGET)
    sleep(250)
    right()
    display.show(Image.ARROW_E)
    sleep(300)
    return


while True:
    display.show(Image.HEART)
    sleep(500)
    dance = 0
    while True:
        if button_a.was_pressed():
            dance = 1
        elif button_b.was_pressed():
            dance = 2
        if dance == 1:
            dance1()
        elif dance == 2:
            dance2()
        sleep(100)
