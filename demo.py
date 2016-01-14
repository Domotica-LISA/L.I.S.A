# -*- coding: UTF-8 -*-

import serial
from time import clock

serServo = serial.Serial('/dev/ttyACM0', 9600)
serLed = serial.Serial('/dev/ttyACM1', 9600)

startup = True

while True:
    starttime = clock()
    timeinterval = 1
    if startup:
        serServo.write("4")
        startup = False
    while starttime + timeinterval > clock():
        pass
    serLed.write("55,38,0")
    serServo.write("3")