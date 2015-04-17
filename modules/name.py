# -*- coding: UTF-8 -*-
import re
import time

WORDS = ["NAAM"]

def handle(text, speaker, profile):
	speaker.say("Hoi mijn naam is " + profile['name'])
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwat is je naam\b', text, re.IGNORECASE))