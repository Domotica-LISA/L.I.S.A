import re
import datetime
import time

WORDS = ["TIJD", "HOE LAAT"]

def handle(text, mic):
	now = datetime.datetime.now()

	minuten = now.strftime("%M")
	uur = now.strftime("%I")
	uur = uur.replace("O", "")

	response = minuten + " minuten over " + uur

	#mic.say("Het is nu %s." % response)
	time.sleep(2)


def isValid(text):
	return bool(re.search(r'\b(hoe laat|tijd)\b', text, reIGNORECASE))