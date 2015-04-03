import re
from math import random

WORDS = ["RAADSEL"]

def handle(text, speaker):
	speaker.say("Hidiho")
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bweet je een raadsel\b', text, re.IGNORECASE))