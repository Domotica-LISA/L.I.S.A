# -*- coding: UTF-8 -*-

import serial

serServo = serial.Serial('/dev/ttyACM0', 19200)
serLed = serial.Serial('/dev/ttyACM1', 19200)

serServo.write("4")
serLed.write("55,38,0")
serServo.write("3")
