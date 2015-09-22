# -*- coding: UTF-8 -*-
import re

WORDS = ["TOILET"]

def handle(text, speaker, mic, profile):
	speaker.say("Just across the hall")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhere is the bathroom|where is the toilet|toilet\b', text, re.IGNORECASE))