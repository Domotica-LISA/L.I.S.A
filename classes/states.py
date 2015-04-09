from time import clock
from random import randint
import wit
import config
import re
import time
import json

import pixy
import ctypes
#import serial

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
	def __init__(self, FSM, Brain):
		self.FSM = FSM
		self.startTime = 0
		self.timer = 0
		self.persona = r"\b" + config.config['name'] + "\\b"
		self.brain = Brain

	def Enter(self):
		self.startTime = int(clock())
		self.timer = randint(0, 5)

	def Execute(self):
		pass

	def Exit(self):
		pass

	def Handle_Response(self):
		return json.loads(wit.voice_query_auto(config.config['wit_ai_token']))

	def Handle_Camera(self):
		count = pixy_get_blocks(1, blocks)
		if count > 0:
			print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks.type, blocks.signature, blocks.x, blocks.y, blocks.width, blocks.height)

class Startup(State):
	def __init__(self, FSM, Brain):
		super(Startup, self).__init__(FSM, Brain)

	def Enter(self):
		print "Entering startup"
		super(Startup, self).Enter()

	def Execute(self):
		print "Starting up"
		self.FSM.ToTransition("toScanning")

	def Exit(self):
		print "Startup complete"

class Scanning(State):
	def __init__(self, FSM, Brain):
		super(Scanning, self).__init__(FSM, Brain)

	def Enter(self):
		print "Start Scanning"
		super(Scanning, self).Enter()

	def Execute(self):
		print "Scanning"
		self.FSM.ToTransition("toMove")

	def Exit(self):
		print "Exit Scanning"

class Move(State):
	def __init__(self, FSM, Brain):
		super(Move, self).__init__(FSM, Brain)

	def Enter(self):
		print "Start Moving"
		super(Move, self).Enter()

	def Execute(self):
		print "Moving to sound origin"
		#if self.startTime + self.timer <= clock():
		#	self.FSM.ToTransition("toTrack")
		super(Move, self).Handle_Camera()

	def Exit(self):
		print "Stop Moving"

class Track(State):
	def __init__(self, FSM, Brain):
		super(Track, self).__init__(FSM, Brain)

	def Enter(self):
		print "Start Tracking"
		super(Track, self).Enter()

	def Execute(self):
		print "Tracking"
		text = super(Track, self).Handle_Response()["_text"]
		if re.search(r'\b(shutdown|shut down)\b', text, re.IGNORECASE):
			self.FSM.ToTransition("toShutdown")
		else:
			self.brain.query(text)

	def Exit(self):
		print "Stop Tracking"

class Shutdown(State):
	def __init__(self, FSM, Brain):
		super(Shutdown, self).__init__(FSM, Brain)

	def Enter(self):
		print "Entering shutdown"
		super(Shutdown, self).Enter()

	def Execute(self):
		print "Shutting down"
		text = super(Shutdown, self).Handle_Response()["_text"]
		if re.search(r'\b(startup|start up)\b', text, re.IGNORECASE):
			self.FSM.ToTransition("toStartup")

	def Exit(self):
		print "Exit shutdown"
