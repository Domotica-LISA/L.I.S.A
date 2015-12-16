# -*- coding: UTF-8 -*-
import re
import time
import urllib
import json

WORDS = ["WEATHER"]

def handle(text, speaker, mic, profile):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(profile['location']) + "&appid=" + str(profile['weather_api_key']) + "&units=metric"

    response = urllib.urlopen(url)
    data = json.loads(response.read())
    weather_description = str(data['weather'][0]['description'])
    temp = str(data['main']['temp'])
    speaker.say("The weather for today is " + weather_description + " and the temperature is " + temp)
    time.sleep(2)

def is_valid(text):
    return bool(re.search(r'\b(how is the weather today|what is the weather today|what is the weather|weather today|what is the weather like|weather)\b', text, re.IGNORECASE))