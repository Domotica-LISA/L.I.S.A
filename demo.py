# -*- coding: UTF-8 -*-

import serial
import time

serServo = serial.Serial('/dev/ttyACM0', 9600)
serLed = serial.Serial('/dev/ttyACM1', 9600)

serServo.write("4")
time.sleep(2)
serLed.write("55,38,0")
serServo.write("3")