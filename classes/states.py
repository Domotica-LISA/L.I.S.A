from time import clock
from random import randint
import wit
import config
import re
import time
import json
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
		("height", c_uint),
		("angle", c_uint) ]

ser = serial.Serial('/dev/tty', 9600)
blocks = Blocks()

class State(object):
	def __init__(self, FSM):
		self.FSM = FSM
		self.startTime = 0
		self.timer = 0
		self.persona = r"\b" + config.config['naam'] + "\\b"

	def Enter(self):
		self.startTime = int(clock())
		self.timer = randint(0, 5)

	def Execute(self):
		pass

	def Exit(self):
		pass

	def Handle_Response(self):
		return wit.voice_query_auto(config.config['wit_ai_token'])

	def Handle_Camera(self):
		count = pixy_get_blocks(1, blocks)
		if count > 0:
			print '[BLOCK_TYPE=%d SIG=%d X=%3d Y=%3d WIDTH=%3d HEIGHT=%3d]' % (blocks.type, blocks.signature, blocks.x, blocks.y, blocks.width, blocks.height)

class Wait(State):
	def __init__(self, FSM):
		super(Wait, self).__init__(FSM)

	def Enter(self):
		print "Waiting for Keyword"
		super(Wait, self).Enter()

	def Execute(self):
		print "Waiting"

		if re.search(self.persona, super(Wait, self).Handle_Response(), re.IGNORECASE):
				self.FSM.ToTransition("toMove")
		if self.startTime + 30 <= clock():
			self.FSM.ToTransition("toScanning")

	def Exit(self):
		print "Exit Waiting"

class Scanning(State):
	def __init__(self, FSM):
		super(Scanning, self).__init__(FSM)

	def Enter(self):
		print "Start Scanning"
		super(Scanning, self).Enter()

	def Execute(self):
		print "Scanning"

		if re.search(self.persona, super(Scanning, self).Handle_Response(), re.IGNORECASE):
				self.FSM.ToTransition("toMove")
		if self.startTime + 10 <= clock():
			self.FSM.ToTransition("toWait")

	def Exit(self):
		print "Exit Scanning"

class Move(State):
	def __init__(self, FSM):
		super(Move, self).__init__(FSM)

	def Enter(self):
		print "Start Moving"
		super(Move, self).Enter()

	def Execute(self):
		print "Moving to sound origin"
		#if self.startTime + self.timer <= clock():
			#self.FSM.ToTransition("toTrack")
		super(Move, self).Handle_Camera()

	def Exit(self):
		print "Stop Moving"

class Track(State):
	def __init__(self, FSM):
		super(Track, self).__init__(FSM)

	def Enter(self):
		print "Start Tracking"
		super(Track, self).Enter()

	def Execute(self):
		print "Tracking"
		if self.startTime + self.timer <= clock():
			self.FSM.ToTransition("toWait")

	def Exit(self):
		print "Stop Tracking"