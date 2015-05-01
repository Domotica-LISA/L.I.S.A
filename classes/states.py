# -*- coding: UTF-8 -*-

import config
import re
import time
import myprocess
from multiprocessing import Process
import serial
import blocks
import myservo

from pixy import *

#pixy_init()

#serServo = serial.Serial('/dev/ttyACM1', 9600)
#serLed = serial.Serial('/dev/ttyACM0', 9600)

class State(object):
	def __init__(self, fSM, brain):
		self.fSM = fSM
		self.persona = r"\b" + config.config['name'] + "\\b"
		self.brain = brain
		self.direction = 'right'

	def enter(self):
		pass

	def execute(self):
		pass

	def exit(self):
		pass

	def get_color_code(self):
		self.brain.ledRingColor['red'] = 5
		self.brain.ledRingColor['green'] = 5
		self.brain.ledRingColor['blue'] = 30

		count = pixy_get_blocks(1, blocks.block)
		if count > 0:
			#print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks.block.type, blocks.block.signature, blocks.block.x, blocks.block.y, blocks.block.width, blocks.block.height)
			return True
		else:
			#sweep left to right or right to left and up and down
			if myservo.servoPos['basePos'] > myservo.servoMaxPos['basePos']:
				self.direction = 'left'
			elif myservo.servoPos['basePos'] < myservo.servoMinPos['basePos']:
				myservo.servoPos['basePos'] = 90
				return False

			if self.direction is 'left':
				myservo.servoPos['basePos'] -= 1
			elif self.direction is 'right':
				myservo.servoPos['basePos'] += 1
		
		#serServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
		#serLed.write("%s, %s, %s" % (self.brain.ledRingColor['red'], self.brain.ledRingColor['green'], self.brain.ledRingColor['blue']))

class Startup(State):
	def __init__(self, fSM, brain):
		super(Startup, self).__init__(fSM, brain)

	def enter(self):
		print "Entering startup"

	def execute(self):
		print "Starting up"
		self.brain.speaker.say("Biep... ")
		time.sleep(1)
		self.brain.speaker.say("Biep... ")
		myservo.servoPos['basePos'] = 90
		#serServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
		time.sleep(0.5)
		self.brain.speaker.say("Bezig met het opstarten van mijn primaire functies.")
		myservo.servoPos['headPos'] = 45
		#serServo.write("0, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
		self.fSM.to_transition("toScanning")

	def exit(self):
		print "Startup complete"
		self.brain.speaker.say("Opstarten voltooid.")

class Scanning(State):
	def __init__(self, fSM, brain):
		super(Scanning, self).__init__(fSM, brain)

	def enter(self):
		print "Start Scanning"
		
		#serServo.write("1, %s, %s, %s" % (myservo.servoPos['basePos'], myservo.servoPos['rotationPos'], myservo.servoPos['headPos']))
		#serLed.write("%s, %s, %s" % (self.brain.ledRingColor['red'], self.brain.ledRingColor['green'], self.brain.ledRingColor['blue']))

	def execute(self):
		print "Scanning"
		input = self.brain.mic.active_listen()
		print input
		if input is not None:
			if re.search(self.persona, input, re.IGNORECASE):
				# send message to arduino to listen to serial data only
				#myservo.servoPos['basePos'] = serServo.readline()
				self.fSM.to_transition("toMove")

	def exit(self):
		print "Exit Scanning"

class Move(State):
	def __init__(self, fSM, brain):
		super(Move, self).__init__(fSM, brain)

	def enter(self):
		print "Start Moving"
		self.brain.speaker.say("Riep iemand mij?")
		self.direction = 'right'

	def execute(self):
		print "Moving to sound origin"
		self.fSM.to_transition("toTrack")
		"""
		ccDetected = super(Move, self).get_color_code()
		if ccDetected is True:
			self.fSM.to_transition("toTrack")
		elif ccDetected is False:
			self.fSM.to_transition("toScanning")
		"""

	def exit(self):
		print "Stop Moving"
		#self.brain.speaker.say("Ik heb je gevonden")

class Track(State):
	def __init__(self, fSM, brain):
		super(Track, self).__init__(fSM, brain)
		self.voiceProcess = Process(target=myprocess.run_voice_process, args=(self.brain, self.fSM)) #serServo, serLed))
		self.colorCodeProcess = Process(target=myprocess.run_color_code_process) #args=(serServo,))

	def enter(self):
		print "Start Tracking"

		global processs

		processs = []
		processs.append(self.voiceProcess)

		self.brain.speaker.say("Hoi, waarmee kan ik je helpen mark en ivar?")

	def execute(self):
		print "Tracking"

		self.voiceProcess.start()
		self.colorCodeProcess.start()

		time.sleep(10)

		#for p in processs:
			#p.join()

	def exit(self):
		print "Stop Tracking"

		for p in processs:
			p.terminate()
			processs.remove(p)

class Shutdown(State):
	def __init__(self, fSM, brain):
		super(Shutdown, self).__init__(fSM, brain)

	def enter(self):
		print "Entering shutdown"
		self.brain.speaker.say("Bezig met afsluiten.")
		self.brain.ledRingColor['red'] = 0
		self.brain.ledRingColor['green'] = 0
		self.brain.ledRingColor['blue'] = 0

		# set servo's to transport position
		#serServo.write("0, %s, %s, %s" % (myservo.servoStoragePos['basePos'], myservo.servoStoragePos['rotationPos'], myservo.servoStoragePos['headPos']))
		#serLed.write("%s, %s, %s" % (self.brain.ledRingColor['red'], self.brain.ledRingColor['green'], self.brain.ledRingColor['blue']))

	def execute(self):
		print "Shutting down"

		input = self.brain.mic.active_listen()
		print input
		if re.search(r'\b(opstarten|start up)\b', input, re.IGNORECASE):
			self.fSM.to_transition("toStartup")

	def exit(self):
		print "Exit shutdown"
