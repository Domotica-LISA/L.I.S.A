# -*- coding: UTF-8 -*-
import httplib2
import re
from xml.dom import minidom

WORDS = ['TRAIN']

def handle(text, speaker, mic, profile):
	teller = 0
	http = httplib2.Http(disable_ssl_certificate_validation=True)
	http.follow_redirects = False
	http.add_credentials('skievar@gmail.com', profile['ns_api_key'])

	resp, content = http.request("https://webservices.ns.nl/ns-api-avt?station=" + profile['location'])

	xmldoc = minidom.parseString(content);

	for node in xmldoc.getElementsByTagName('VertrekkendeTrein'):
	    if teller == 5:
	    	break

	    vertrekTijd = node.getElementsByTagName("VertrekTijd")[0].firstChild.data
	    eindBestemming = node.getElementsByTagName("EindBestemming")[0].firstChild.data
	    vertrekSpoor = node.getElementsByTagName("VertrekSpoor")[0].firstChild.data
	    
	    speaker.say("De trein naar " + eindBestemming + " op spoor " + vertrekSpoor + " vertrekt om " + vertrekTijd[11] + vertrekTijd[12] + vertrekTijd[13] + vertrekTijd[14] + vertrekTijd[15])
	    teller = teller + 1

def is_valid(text):
    return bool(re.search(r'\b(what time does the train leave|what time will the train|trains|train)\b', text, re.IGNORECASE))    