# -*- coding: UTF-8 -*-
import re

WORDS = ["FOOD"]

def handle(text, speaker, mic, profile):
	speaker.say("I like food")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhere can i get something to eat|eating|food\b', text, re.IGNORECASE))