# -*- coding: UTF-8 -*-
import re
import time

WORDS = ['WHAT CAN YOU DO']

def handle(text, speaker, mic, profile):
	response = ""
	for moduleName in profile['modules']:
		if profile['modules'][moduleName] == True:
			if moduleName == 'train':
				response += " I can tell you something about when trains leave from %s." % profile['location']
			if moduleName == "weather":
				response += " If you would like to know what the weather will be like, I am your lady'."
			if moduleName == "time":
				response += " I am a precision machine. I can tell you what time it is up to the minute."
	response += " Beside that I can also explain what my name means."
	time.sleep(2)

def is_valid(text):
	return bool(re.search(r'\bwhat can you do\b', text, re.IGNORECASE))