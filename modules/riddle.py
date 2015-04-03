import re
import time

WORDS = ["RAADSEL"]

def handle(text, speaker, profile):
	speaker.say("Hidiho")
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\braadsel\b', text, re.IGNORECASE))