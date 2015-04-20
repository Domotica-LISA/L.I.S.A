# -*- coding: UTF-8 -*-

import re
import threading
import blocks

blocks.block

class ColorCodeThread(threading.Thread):
	def __init__(self, threadID, name, brain, fSM):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.brain = brain
		self.fSM = fSM

	def run(self):


class VoiceThread(threading.Thread):
	def __init__(self, threadID, name, brain, fSM):
		threading.Thread.__init__(self)
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