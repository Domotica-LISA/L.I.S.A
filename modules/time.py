import re
import datetime
import time

WORDS = ["TIJD", "HOE LAAT", "HOELAAT"]

def handle(text, speaker):
	now = datetime.datetime.now()

	minuten = now.strftime("%M")
	uur = now.strftime("%I")
	uur = uur.replace("0", "")

	response = minuten + " minuten over " + uur

	speaker.say("Het is nu %s" % response)
	time.sleep(2)

def isValid(text):
	return bool(re.search(r'\b(hoe laat|tijd|hoelaat)\b', text, re.IGNORECASE))