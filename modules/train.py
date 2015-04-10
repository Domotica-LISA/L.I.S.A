import httplib2
import re
from xml.dom import minidom

WORDS = ['TREIN']

def handle(text, speaker, profile):
	http = httplib2.Http(disable_ssl_certificate_validation=True)
	http.follow_redirects = False
	http.add_credentials('skievar@gmail.com', '9zMZBc_mLFpII0OMTQct-OMPtf93EEvammhfuDUzQMfLG-NSE1QFDw')

	resp, content = http.request("https://webservices.ns.nl/ns-api-avt?station=" + profile['location'])

	xmldoc = minidom.parseString(content);

	for node in xmldoc.getElementsByTagName('VertrekkendeTrein'):
	    VertrekTijd = node.getElementsByTagName("VertrekTijd")[0].firstChild.data
	    EindBestemming = node.getElementsByTagName("EindBestemming")[0].firstChild.data
	    VertrekSpoor = node.getElementsByTagName("VertrekSpoor")[0].firstChild.data
	    
	    speaker.say("De trein naar " + EindBestemming + " op spoor " + VertrekSpoor + " vertrekt om " + VertrekTijd[11] + VertrekTijd[12] + VertrekTijd[13] + VertrekTijd[14] + VertrekTijd[15])

def isValid(text):
    return bool(re.search(r'\b(hoelaat vertrekt de trein|hoe laat vertrekt de trein|rijden er nog treinen|hoelaat gaat de trein|hoe laat gaat de trein)\b', text, re.IGNORECASE))    