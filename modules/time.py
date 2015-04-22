# -*- coding: UTF-8 -*-
import re
import datetime
import time

WORDS = ["TIJD", "HOE LAAT", "HOELAAT" "IS", "HET", "WAT", "IS", "DE"]

def handle(text, speaker, mic, profile):
	now = datetime.time.now()
	response = now.time.hour() + now.time.minute()
	speaker.say("Het is nu %s" % response)
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\b(hoe laat is het|wat is de tijd|hoelaat is het)\b', text, re.IGNORECASE))