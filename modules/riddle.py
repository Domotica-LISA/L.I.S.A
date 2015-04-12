import re
import time

WORDS = ["RAADSEL"]

def handle(text, speaker, profile):
	speaker.say("Hidiho")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\braadsel\b', text, re.IGNORECASE))