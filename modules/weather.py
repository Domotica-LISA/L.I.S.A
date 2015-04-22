# -*- coding: UTF-8 -*-
import re
import feedparser
import time

WORDS = ["WEER"]

def handle(text, speaker, mic, profile):
    entries = feedparser.parse("http://www.knmi.nl/rssfeeds/knmi-rssweer.cgi")['entries']

    for entry in entries:
        date_desc = entry['title'].split()[1].strip().lower()
        if date_desc == 'verwachting':
            speaker.say("Het weer voor vandaag is %s" % entry['summary'].replace('<br />','')[:-33])
            time.sleep(2)

def is_valid(text):
    return bool(re.search(r'\b(hoe is het weer vandaag|wat voor weer wordt het vandaag|wat voor weer wordt het|weer vandaag|wat voor weer is het)\b', text, re.IGNORECASE))