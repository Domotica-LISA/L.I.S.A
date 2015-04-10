import re
import time

WORDS = ['WAT KAN JE ALLEMAAL']

def handle(text, speaker, profile):
	for module in profile['modules']:
		for value in module:
			if value == True:
				print module
			print value
		print module
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bwat kan je\b', text, re.IGNORECASE))