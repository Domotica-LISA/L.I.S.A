# -*- coding: UTF-8 -*-
import time
import random
from sys import maxint

WORDS = []

PRIORITY = -(maxint + 1)

def handle(text, speaker, mic, profile):
	defanswer = ('Excuse me could you repeat that', 'I did not quit get that', 'What was your question exactly', 'I could not hear you, what did you say')
	speaker.say(random.choice(defanswer))
	time.sleep(2)

def is_valid(text):
	return True