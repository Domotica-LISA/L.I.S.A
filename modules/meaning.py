# -*- coding: UTF-8 -*-
import re
import time

WORDS = ["BETEKENT"]

def handle(text, speaker, mic, profile):
	speaker.say(profile['name'] + ' staat voor ' + profile['meaning'])
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwat betekent lisa\b', text, re.IGNORECASE))