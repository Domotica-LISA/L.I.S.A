# -*- coding: UTF-8 -*-
import re
import datetime
import time

WORDS = ["TIJD", "HOE LAAT", "HOELAAT" "IS", "HET", "WAT", "IS", "DE"]

def set_prefix(minuten):
	if minuten == 1:
		prefix = " minuut "
	else:
		prefix = " minuten "
	return prefix

def convert_time():
	now = datetime.datetime.now()
	if now.hour > 12:
		uur = now.hour - 12
	else:
		uur = now.hour
		if uur + 1 == 13:
			uur = 0

	if now.minute == 0:
		response = str(uur) + " uur"
	elif now.minute == 15:
		response = "kwart over " + str(uur)
	elif now.minute == 30:
		response = "half " + str(uur + 1)
	elif now.minute == 45:
		response = "kwart voor " + str(uur + 1)
	elif now.minute > 15 and now.minute < 30:
		minuten = 30 - now.minute
		response = str(minuten) + set_prefix(minuten) +  "voor half " + str(uur + 1)
	elif now.minute > 30 and now.minute < 45:
		minuten = now.minute - 30
		response = str(minuten) + set_prefix(minuten) + "over half " + str(uur + 1)
	elif now.minute > 45 and now.minute < 60:
		minuten = 60 - now.minute
		response = str(minuten) + set_prefix(minuten) + "voor " + str(uur + 1)
	else:
		response = str(now.minute) + set_prefix(now.minute) + "over " + str(uur)
	return response

def handle(text, speaker, mic, profile):
	now = datetime.datetime.now()
	speaker.say("Het is nu %s" % convert_time())
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\b(hoe laat is het|wat is de tijd|hoelaat is het)\b', text, re.IGNORECASE))