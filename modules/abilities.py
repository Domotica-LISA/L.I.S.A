import re
import time

WORDS = ['WAT KAN JE ALLEMAAL']

def handle(text, speaker, profile):
	for moduleName in profile['modules']:
		if profile['modules'][moduleName] == True:
			print moduleName
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bwat kan je\b', text, re.IGNORECASE))