# -*- coding: UTF-8 -*-

import config
import re
import time
import mic
import stt

from pixy import *
from ctypes import *
import serial

pixy_init()

class Blocks(Structure):
	_fields_ = [ ("type", c_uint),
		("signature", c_uint),
		("x", c_uint),
		("y", c_uint),
		("width", c_uint),
		("height", c_uint)]

#ser = serial.Serial('/dev/ttyACM0', 9600)
blocks = Block()

class State(object):
	def __init__(self, fSM, brain):
		self.fSM = fSM
		self.persona = r"\b" + config.config['name'] + "\\b"
		self.brain = brain
		self.servoPos = {
			"basePos": 25,
			"armPos": 60,
			"rotationPos": 90,
			"headPos": 25}
		self.arduinoActive = 0
		self.ccDetected = False
		self.ledRingColor = {
			"red": 30,
			"green": 30,
			"blue": 30}
		self.mic = mic.Mic(stt.WitAiSTT)

	def enter(self):
		pass

	def execute(self):
		pass

	def exit(self):
		pass

	def get_color_code(self):
		count = pixy_get_blocks(1, blocks)
		if count > 0:
			print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks.type, blocks.signature, blocks.x, blocks.y, blocks.width, blocks.height)
			self.ccDetected = True
		else:
			self.ccDetected = False

class Startup(State):
	def __init__(self, fSM, brain):
		super(Startup, self).__init__(fSM, brain)

	def enter(self):
		print "Entering startup"

	def execute(self):
		print "Starting up"
		self.brain.speaker.say("Biep... ")
		#ser.write("0, %s" % str(self.servoPos['basePos']))
		time.sleep(1)
		self.brain.speaker.say("Biep... ")
		#ser.write("0, %s, %s" % str(self.servoPos['basePos']), str(self.servoPos['armPos']))
		time.sleep(0.5)
		self.brain.speaker.say("Bezig met het opstarten van mijn primaire functies.")
		#ser.write("0, %s, %s, %s" % str(self.servoPos['basePos']), str(self.servoPos['armPos']), str(self.servoPos['rotationPos']), str(self.servoPos['headPos']))
		self.fSM.to_transition("toScanning")

	def exit(self):
		print "Startup complete"
		self.brain.speaker.say("Opstarten voltooid.")
		#ser.write("%s, %s, %s, %s, %s, %sself.arduinoActive, str(self.servoPos['basePos']), self.ledRingColor['red'], self.ledRingColor['green'], self.ledRingColor['blue'])

class Scanning(State):
	def __init__(self, fSM, brain):
		super(Scanning, self).__init__(fSM, brain)

	def enter(self):
		print "Start Scanning"
		self.arduinoActive = True

	def execute(self):
		print "Scanning"
		if re.search(self.persona, self.mic.active_listen(), re.IGNORECASE):
			# send message to arduino to listen to serial data only
			# get baseservo pos from arduino
			self.fSM.to_transition("toMove")

	def exit(self):
		print "Exit Scanning"
		self.arduinoActive = False

class Move(State):
	def __init__(self, fSM, brain):
		super(Move, self).__init__(fSM, brain)

	def enter(self):
		print "Start Moving"
		self.brain.speaker.say("Riep iemand mij?")

	def execute(self):
		print "Moving to sound origin"
		self.fSM.to_transition("toTrack")
		super(Move, self).get_color_code()
		#if self.ccDetected:
			#self.fSM.to_transition("toTrack")

	def exit(self):
		print "Stop Moving"
		#self.brain.speaker.say("Ik heb je gevonden")

class Track(State):
	def __init__(self, fSM, brain):
		super(Track, self).__init__(fSM, brain)

	def enter(self):
		print "Start Tracking"
		self.brain.speaker.say("Hoi, waarmee kan ik je helpen?")

	def execute(self):
		print "Tracking"
		super(Track, self).get_color_code()
		
		input = self.mic.active_listen()
		if re.search(r'\b(power down|powerdown)\b', input, re.IGNORECASE):
			self.fSM.to_transition("toShutdown")
		else:
			self.brain.query(input)

	def exit(self):
		print "Stop Tracking"

class Shutdown(State):
	def __init__(self, fSM, brain):
		super(Shutdown, self).__init__(fSM, brain)

	def enter(self):
		print "Entering shutdown"
		self.brain.speaker.say("Bezig met afsluiten.")
		# set servo's to transport position

	def execute(self):
		print "Shutting down"

		if re.search(r'\b(opstarten|start up)\b', self.mic.active_listen(), re.IGNORECASE):
			self.fSM.to_transition("toStartup")

	def exit(self):
		print "Exit shutdown"
