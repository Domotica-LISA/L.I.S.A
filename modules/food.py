# -*- coding: UTF-8 -*-
import re

WORDS = ["ETEN"]

def handle(text, speaker, mic, profile):
	speaker.say("Vrijdag middag is er een lunch op de derde etage")
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwaar kan ik iets eten|eten\b', text, re.IGNORECASE))