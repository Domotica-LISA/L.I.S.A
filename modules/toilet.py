# -*- coding: UTF-8 -*-
import re

WORDS = ["TOILET"]

def handle(text, speaker, mic, profile):
	speaker.say("Het toilet is hier rechts tegenover")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwaar is de wc|waar is het toilet|toilet\b', text, re.IGNORECASE))