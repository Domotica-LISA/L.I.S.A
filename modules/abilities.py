import time
from sys import maxint

WORDS = ['WAT KAN JE ALLEMAAL']


def handle(text, speaker, profile):
	for module in profile['modules']:
		if module == True:
			print module
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bwat kan je\b', text, re.IGNORECASE))