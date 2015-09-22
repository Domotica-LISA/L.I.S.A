# -*- coding: UTF-8 -*-
import re
import time

WORDS = ["NAME"]

def handle(text, speaker, mic, profile):
	speaker.say("Hi my name is " + profile['name'])
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhat is your name\b', text, re.IGNORECASE))