import time
from sys import maxint

PRIORITY = -(maxint + 1)

def handle(text, speaker, profile):
	speaker.say("Sorry kan je dat herhalen")
	time.sleep(2)

def isValid(text):
	return True