# -*- coding: UTF-8 -*-
import re
import feedparser
import time

WORDS = ["WHEATER"]

def handle(text, speaker, mic, profile):
    entries = feedparser.parse("http://rss.wunderground.com/auto/rss_full/%s"%profile['weather_location'])['entries']

    for entry in entries:
        date_desc = entry['title'].split()[1].strip().lower()
        if date_desc == 'forcast':
        	print entry['summary']
            speaker.say("The weather for today is %s" % entry['summary'])
            time.sleep(2)

def is_valid(text):
    return bool(re.search(r'\b(how is the weather today|what is the weather today|what is the weather|weather today|what is the weather like|weather)\b', text, re.IGNORECASE))