# -*- coding: UTF-8 -*-
import time
from sys import maxint

WORDS = []

PRIORITY = -(maxint + 1)

def handle(text, speaker, mic, profile):
	speaker.say("Sorry kan je dat herhalen")
	time.sleep(2)

def is_valid(text):
	return True