# -*- coding: UTF-8 -*-

import re
import threading
import myservo
import time
from pixy import *

block = Block()

class ColorCodeThread(threading.Thread):
	def __init__(self, serialServo, servoPos):
		threading.Thread.__init__(self)
		self.serialServo = serialServo
		self.servoPos = servoPos

	def run(self):
		
		while 1:
			center = {'x': 0, 'y': 0}

			count = pixy_get_blocks(1, block)
			if count > 0:
				center['x'] = block.x + (block.width / 2)
				center['y'] = block.y + (block.height / 2)

				if center['x'] > 200 and center['x'] < 285: 
					print "rotate left"
					self.servoPos['rotationPos'] = self.servoPos['rotationPos'] - 1
				elif center['x'] > 0 and center['x'] < 200: 
					print "base left"
					self.servoPos['basePos'] = self.servoPos['basePos'] - 1
				elif center['x'] > 355 and center['x'] < 440:
					print "rotate right"
					self.servoPos['rotationPos'] = self.servoPos['rotationPos'] + 1
				elif center['x'] > 440 and center['x'] < 640:
					print "base right"
					self.servoPos['basePos'] = self.servoPos['basePos'] + 1
				else:
					#print "deadzone x"
					pass

				if center['y'] > 0 and center['y'] < 175:
					print "head up"
					self.servoPos['headPos'] = self.servoPos['headPos'] - 1
				elif center['y'] > 225 and center['y'] < 400:
					print "head down"
					self.servoPos['headPos'] = self.servoPos['headPos'] + 1
				else:
					#print "deadzone y"
					pass
				

			#print "hoi"

				self.serialServo.write("0, %s, %s, %s" % (self.servoPos['basePos'], self.servoPos['rotationPos'], self.servoPos['headPos']))

class VoiceThread(threading.Thread):
	def __init__(self, brain, fSM, serialLed, serialServo):
		threading.Thread.__init__(self)
		self.brain = brain
		self.fSM = fSM
		self.serialServo = serialServo
		self.serialLed = serialLed

	def run(self):
		"""
		while 1:

			self.setRingColor(5, 30, 5)

			input = self.brain.mic.active_listen()
			print input

			if input is not None:
				if re.search(r'\b(power down|powerdown)\b', input, re.IGNORECASE):
					self.fSM.to_transition("toShutdown")
					break
				elif re.search(r'\b(dankje|tot ziens)\b', input, re.IGNORECASE):
					self.brain.speaker.say("graag gedaan. Bye Bye")
					self.fSM.to_transition("toScanning")
					break
				else:
					#self.serialServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
					self.setRingColor(30, 5, 5)
					self.brain.query(input)
					"""
		print "hoi"

	def setRingColor(self, red, green, blue):
		self.serialLed.write("%s, %s, %s" % (red, green, blue))
		time.sleep(1)