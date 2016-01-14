# -*- coding: UTF-8 -*-

import serial
from time import clock

startTime = clock()
timeInterval = 5

serServo = serial.Serial('/dev/ttyACM0', 19200)
serLed = serial.Serial('/dev/ttyACM1', 19200)

serServo.write("4")
while startTime + timeInterval > clock():
    pass

serLed.write("55,38,0")
while startTime + timeInterval > clock():
    pass

serServo.write("3")
while startTime + timeInterval > clock():
    pass
