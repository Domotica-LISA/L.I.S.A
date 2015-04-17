# -*- coding: utf-8-*-

import json
import urllib2

class WitAiSTT(object):
	def __init__(self, accessToken):
		self.headers = {'Authorization': 'Bearer %s' % accessToken, 'accept': 'application/json', 'Content-Type': 'audio/wav'}

	def transcribe(self, fp):
		data = fp.read()
		requests = urllib2.Request('https://api.wit.ai/speech?v=20150101', data=data, headers=self.headers)
		r = urllib2.urlopen(requests)

		#print r
		text = json.loads(r)
		transcribed = [text.upper()]
		return transcribed['_text']