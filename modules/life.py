# -*- coding: UTF-8 -*-
import re
import time

WORDS = ["MEANING OF LIFE"]

def handle(text, speaker, mic, profile):
	speaker.say("The meaning of life is 42")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhat is the meaning of life | meaning life\b', text, re.IGNORECASE))