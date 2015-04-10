import re
import time

WORDS = ['WAT KAN JE ALLEMAAL']

def handle(text, speaker, profile):
	response = ""
	for moduleName in profile['modules']:
		if profile['modules'][moduleName] == True:
			if moduleName == 'train':
				response += "Ik kan wat vertellen over hoelaat de treinen vertrekken vanaf %s." % profile['location']
			if moduleName == "weather":
				response += "Voor als je wil weten wat voor weer het wordt, ik ben je Dame."
			if moduleName == "time":
				response += "Tijd, Tijd, ik ben een precisie machine. Ik kan je tot op de minuut vertellen hoelaat het is."
	response += "Daarnaast kan ik je zeggen waar mijn naam voor staat. En gezien we hier op een congres staan, weet ik ook waar de toiletten zijn en waar je een hapje kan eten."
	speaker.say("%s En voor een workshop in 3d printen, kan ik je ook wijzer maken waar ze die geven" % response)
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\bwat kan je\b', text, re.IGNORECASE))