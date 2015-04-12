from time import clock
from random import randint
import wit
import config
import re
import time
import json
#import RPi.GPIO as gpio

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

#ser = serial.Serial('/dev/tty', 9600)
blocks = Block()

class State(object):
	def __init__(self, fSM, brain):
		self.fSM = fSM
		self.persona = r"\b" + config.config['name'] + "\\b"
		self.brain = brain
		self.servoPos = ['0','0','0','0']
		self.arduinoActive = False
		self.ccDetected = False

	def enter(self):
		pass

	def execute(self):
		pass

	def exit(self):
		pass

	def handle_response(self):
		return json.loads(wit.voice_query_auto(config.config['wit_ai_token']))

	def handle_async_response(self, response):
		text = json.loads(response)
		if re.search(r'\b(shutdown|shut down)\b', text['_text'], re.IGNORECASE):
			self.fSM.to_transition("toShutdown")
		else:
			self.brain.query(text['_text'])
		#return json.loads(response)

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
		self.brain.speaker.say("Biep... Biep... Booting up mijn primaire functies")

	def execute(self):
		print "Starting up"
		# set servo's to idle position
		self.fSM.to_transition("toScanning")

	def exit(self):
		print "Startup complete"
		self.brain.speaker.say("Bootup voltooid")

class Scanning(State):
	def __init__(self, fSM, brain):
		super(Scanning, self).__init__(fSM, brain)

	def enter(self):
		print "Start Scanning"
		self.arduinoActive = True

	def execute(self):
		print "Scanning"
		if re.search(self.persona, super(Scanning, self).handle_response()['_text'], re.IGNORECASE):
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
		self.brain.speaker.say("Riep iemand mij")

	def execute(self):
		print "Moving to sound origin"
		self.fSM.to_transition("toTrack")
		super(Move, self).get_color_code()
		#if self.ccDetected:
			#self.fSM.to_transition("toTrack")

	def exit(self):
		print "Stop Moving"
		self.brain.speaker.say("Ik heb je gevonden")

class Track(State):
	def __init__(self, fSM, brain):
		super(Track, self).__init__(fSM, brain)

	def enter(self):
		print "Start Tracking"
		self.brain.speaker.say("Hoi, waarmee kan ik je helpen?")

	def execute(self):
		print "Tracking"
		super(Track, self).get_color_code()
		
		wit.voice_query_auto_async(config.config['wit_ai_token'], super(Track, self).handle_async_response)

	def exit(self):
		print "Stop Tracking"

class Shutdown(State):
	def __init__(self, fSM, brain):
		super(Shutdown, self).__init__(fSM, brain)

	def enter(self):
		print "Entering shutdown"
		self.brain.speaker.say("Nee niet doen. Ik kan je nog zooooooooooo veeeeel wijz..........")
		# set servo's to transport position

	def execute(self):
		print "Shutting down"
		text = super(Shutdown, self).handle_response()["_text"]
		if re.search(r'\b(startup|start up)\b', text, re.IGNORECASE):
			self.fSM.to_transition("toStartup")

	def exit(self):
		print "Exit shutdown"
