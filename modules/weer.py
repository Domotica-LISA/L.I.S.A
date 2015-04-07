import re
import pywapi

WORDS = ["WAT VOOR WEER", "WAT IS HET WEER"]

def handle(text, speaker):
	yahoo_result = pywapi.get_weather_from_yahoo('NLXX0010')

	response = yahoo_result['condition']['text'] + ' en ' + yahoo_result['condition']['temp'] + ' C.'

	speaker.say("Het is nu %s." % response )
	time.sleep(2)


def isValid(text):
	print text
	return bool(re.search(r'\b(wat voor weer|wat is het weer)\b', text, re.IGNORECASE))
