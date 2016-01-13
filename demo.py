# -*- coding: UTF-8 -*-

import serial

serServo = serial.Serial('/dev/ttyACM0', 9600)
serLed = serial.Serial('/dev/ttyACM1', 9600)

if __name__ == '__main__':
    try:
        serLed.write("55,38,0")
        serServo.write("3")
    except KeyboardInterrupt:
        print "Bye Bye!"