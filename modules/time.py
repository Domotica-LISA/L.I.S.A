import re
import datetime
import time
from client.app_utils import getTimezone

WORDS = ["TIJD", "HOE LAAT"]

def handle(text, mic, profile):
	tz = getTimezone(profile)
	now = datetime.datetime.now(tz=tz)

	minuten = now.strftime("%M")
	uur = now.strftime("%I")
	uur = uur.replace("O", "")

	response = minuten + " minuten over " + uur

	mic.say("Het is nu %s." % response)
	time.sleep(2)


def isValid(text):
	return bool(re.search(r'\b(hoe laat|tijd)\b', text, reIGNORECASE))


