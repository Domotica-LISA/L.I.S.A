# -*- coding: UTF-8 -*-

import re
import threading
import blocks

blocks.block

class ColorCodeThread(threading.Thread):
	def __init__(self, threadID, name, brain, fSM):#, serial):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.brain = brain
		self.fSM = fSM
		#self.serial = serial

	def run(self):
		#self.serial.write("0,90,90,90,90")
		print "hoi"

class VoiceThread(object):
	def __init__(self, threadID, name, brain, fSM):
		threading.Thread.__init__(self)
		self.thread = threading.Thread(target=self.run)
		self.threadID = threadID
		self.name = name
		self.brain = brain
		self.fSM = fSM

	def run(self):
		input = self.brain.mic.active_listen()
		print input
		if re.search(r'\b(power down|powerdown)\b', input, re.IGNORECASE):
			self.fSM.to_transition("toShutdown")
		elif re.search(r'\b(dankje|tot ziens)\b', input, re.IGNORECASE):
			self.fSM.to_transition("toScanning")
		else:
			self.brain.query(input)