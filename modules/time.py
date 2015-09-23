# -*- coding: UTF-8 -*-
import re
import datetime
import time

WORDS = ["TIME", "WHAT TIME", "WHAT TIME IS"]

def set_prefix(minuten):
	if minuten == 1:
		prefix = " minute "
	else:
		prefix = " minutes "
	return prefix

def convert_time():
	now = datetime.datetime.now()
	if now.hour > 12:
		uur = now.hour - 12
		adfix = " pm"
	else:
		uur = now.hour
		adfix = " am"
		if uur + 1 == 13:
			uur = 0

	if now.minute == 0:
		response = str(uur) + " o'clock"
	elif now.minute == 15:
		response = "a quarter past " + str(uur)
	elif now.minute == 30:
		response = "half past " + str(uur)
	elif now.minute == 45:
		response = "a quarter to " + str(uur + 1)
	elif now.minute > 30:
		minuten = now.minute - 30
		response = str(minuten) + set_prefix(minuten) + "to " + str(uur + 1)
	else:
		response = str(now.minute) + set_prefix(now.minute) + "past " + str(uur)
	response += adfix

	return response

def handle(text, speaker, mic, profile):
	speaker.say("The time is %s" % convert_time())
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\b(what time is it)\b', text, re.IGNORECASE))