# -*- coding: UTF-8 -*-
import re
import time

WORDS = ["MEANING"]

def handle(text, speaker, mic, profile):
	speaker.say(profile['name'] + ' stands for ' + profile['meaning'])
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhat does lisa mean\b', text, re.IGNORECASE))