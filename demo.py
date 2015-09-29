# -*- coding: UTF-8 -*-

import serial

serServo = serial.Serial('/dev/ttyACM0', 9600)
serLed = serial.Serial('/dev/ttyACM1', 9600)

serLed.write("5,5,30")
serServo.write("1")