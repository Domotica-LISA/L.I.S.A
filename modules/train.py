# -*- coding: UTF-8 -*-
import httplib2
import re
from xml.dom import minidom

WORDS = ['TREIN']

def handle(text, speaker, mic, profile):
	teller = 0
	http = httplib2.Http(disable_ssl_certificate_validation=True)
	http.follow_redirects = False
	http.add_credentials('skievar@gmail.com', profile['ns_api_key'])

	resp, content = http.request("https://webservices.ns.nl/ns-api-avt?station=" + profile['location'])

	xmldoc = minidom.parseString(content);

	for node in xmldoc.getElementsByTagName('VertrekkendeTrein'):
	    vertrekTijd = node.getElementsByTagName("VertrekTijd")[0].firstChild.data
	    eindBestemming = node.getElementsByTagName("EindBestemming")[0].firstChild.data
	    vertrekSpoor = node.getElementsByTagName("VertrekSpoor")[0].firstChild.data
	    teller = teller + 1
	    if teller > 5:
	    	break
	    
	    speaker.say("De trein naar " + eindBestemming + " op spoor " + vertrekSpoor + " vertrekt om " + vertrekTijd[11] + vertrekTijd[12] + vertrekTijd[13] + vertrekTijd[14] + vertrekTijd[15])

def is_valid(text):
    return bool(re.search(r'\b(hoelaat vertrekt de trein|hoe laat vertrekt de trein|rijden er nog treinen|hoelaat gaat de trein|hoe laat gaat de trein|rijden er treinen|treinen)\b', text, re.IGNORECASE))    