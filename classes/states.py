# -*- coding: UTF-8 -*-

import config
import re
import time
import mythread
import serial
import myservo

from pixy import *

pixy_init()
block = Block()

servoPos = [25, 110, 30]

serServo = serial.Serial('/dev/ttyACM0', 9600)
serLed = serial.Serial('/dev/ttyACM1', 9600)

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
		count = pixy_get_blocks(1, block)
		if count > 0:
			#print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (block.type, block.signature, block.x, block.y, block.width, block.height)
			return True
		else:
			#sweep left to right or right to left and up and down
			if servoPos[0] > myservo.servoMaxPos['basePos']:
				self.direction = 'left'
			elif servoPos[0] < myservo.servoMinPos['basePos']:
				servoPos[0] = 90
				return False

			if self.direction is 'left':
				servoPos[0] = servoPos[0] - 2
			elif self.direction is 'right':
				servoPos[0] = servoPos[0] + 2

class Startup(State):
	def __init__(self, fSM, brain):
		super(Startup, self).__init__(fSM, brain)

	def enter(self):
		print "Entering startup"

	def execute(self):
		print "Starting up"
		self.brain.speaker.say("Biep... ")
		time.sleep(1)
		self.brain.speaker.say("Boep... ")
		servoPos[0] = 90
		serServo.write("0, %s, %s, %s" % (servoPos[0], servoPos[1], servoPos[2]))
		print servoPos
		time.sleep(0.5)
		self.brain.speaker.say("Wie durft mij wakker te maken!?")
		servoPos[2] = 45
		serServo.write("0, %s, %s, %s" % (servoPos[0], servoPos[1], servoPos[2]))
		print servoPos
		self.fSM.to_transition("toTrack")

	def exit(self):
		print "Startup complete"
		self.brain.speaker.say("Buig voor jullie heerser")  
		self.brain.speaker.say("muahahaha.")

class Scanning(State):
	def __init__(self, fSM, brain):
		super(Scanning, self).__init__(fSM, brain)

	def enter(self):
		print "Start Scanning"
		
		serServo.write("1, %s, %s, %s" % (servoPos[0], servoPos[1], servoPos[2]))
		print servoPos
		serLed.write("30, 0, 30")

	def execute(self):
		print "Scanning"
		input = self.brain.mic.active_listen()
		print input
		if input is not None:
			if re.search(self.persona, input, re.IGNORECASE):
				# send message to arduino to listen to serial data only
				#myservo.servoPos['basePos'] = int(serServo.readline())
				self.fSM.to_transition("toMove")

	def exit(self):
		print "Exit Scanning"

class Move(State):
	def __init__(self, fSM, brain):
		super(Move, self).__init__(fSM, brain)

	def enter(self):
		print "Start Moving"
		self.brain.speaker.say("Wat moet je van me?")
		self.direction = 'right'

	def execute(self):
		print "Moving to sound origin"
		#self.fSM.to_transition("toTrack")
		#super(Move, self).get_color_code()
		
		ccDetected = super(Move, self).get_color_code()
		if ccDetected is True:
			self.fSM.to_transition("toTrack")
		elif ccDetected is False:
			self.fSM.to_transition("toScanning")

		serServo.write("0, %s, %s, %s" % (servoPos[0], servoPos[1], servoPos[2]))
		serLed.write("5,5,30")
		time.sleep(1.1)

	def exit(self):
		print "Stop Moving"
		#self.brain.speaker.say("Ik heb je gevonden")

class Track(State):
	def __init__(self, fSM, brain):
		super(Track, self).__init__(fSM, brain)
		
	def enter(self):
		print "Start Tracking"
		self.brain.speaker.say("Hey onderdaan, wat wil je van mij?")

	def execute(self):
		print "Tracking"
		self.voiceThread = mythread.VoiceThread(self.brain, self.fSM, serLed, serServo)
		self.colorCodeThread = mythread.ColorCodeThread(serServo, servoPos)

		#threads = []
		#threads.append(self.voiceThread)

		self.voiceThread.start()
		self.colorCodeThread.start()

		time.sleep(10)
		#for t in threads:
			#t.join()

	def exit(self):
		print "Stop Tracking"

class Shutdown(State):
	def __init__(self, fSM, brain):
		super(Shutdown, self).__init__(fSM, brain)

	def enter(self):
		print "Entering shutdown"
		self.brain.speaker.say("Bezig met afsluiten.")

		# set servo's to transport position
		serServo.write("0, %s, %s, %s" % (myservo.servoStoragePos['basePos'], myservo.servoStoragePos['rotationPos'], myservo.servoStoragePos['headPos']))
		serLed.write("0,0,0")

	def execute(self):
		print "Shutting down"

		input = self.brain.mic.active_listen()
		print input
		if re.search(r'\b(opstarten|start up)\b', input, re.IGNORECASE):
			self.fSM.to_transition("toStartup")

	def exit(self):
		print "Exit shutdown"







