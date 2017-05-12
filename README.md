# Microbit-motor
Micro python script to control a hacked lego motor with a microbit and kiktronic motor board, powered through a 4 AA battery pack (or through a hacked mobile phone USB charger cable)

Kiktronic motor board details here https://www.kitronik.co.uk/pdf/5620%20Motor%20Driver%20Board%20V1.1-2.pdf

How to hack lego motor wires here https://scuttlebots.com/2014/03/02/lego-pf-hacking-wiring/

How to hack USB cable here http://www.instructables.com/id/Hack-that-holy-USB-cable/?ALLSTEPS

2dances.py is a script for 2 motors including pre-set dance routines for the robot
robot_car.py is a script for a single motor, to go forward and back if buttons A or B are pressed

radio_motor.py is a script that takes a step towards one microbit controlling the other as a remote control, but first just to test how to send messages via radio. While the motor is powered, it doesn't receive the strings via the chloe_radio script.
chloe_radio.py is the attempt to use the second microbit (the name is because it is currently attached to [Chloe the doll...)](paulmaltby3/Microbit-wearable) as a remote control, but first just to test by sending messages. Again it doesn't work with radio_motor.py

radio_motor2.py is a way to send messages that does work taken from http://www.suppertime.co.uk/blogmywiki/2016/11/microbit-radio/
chloe_radio2.py is a script that successfuly receives messages, taken from the same site.

![pic](/IMG_7250.JPG)
![pic2](/IMG_7251.JPG)
![pic3](/IMG_7248.JPG)
![pic4](/IMG_7249.JPG)
