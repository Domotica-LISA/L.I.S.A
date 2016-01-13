# -*- coding: UTF-8 -*-

import serial
import time

time.sleep(1)

serServo = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(1)

serLed = serial.Serial('/dev/ttyACM1', 9600)

serServo.write("4")

time.sleep(1)

serLed.write("55,38,0")

time.sleep(1)

serServo.write("3")