import re
import time

WORDS = ["BETEKENT"]

def handle(text, speaker, profile):
	speaker.say(profile['name'] + ' staat voor Lokaal Interactive Servce Android')
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bwat betekent lisa\b', text, re.IGNORECASE))