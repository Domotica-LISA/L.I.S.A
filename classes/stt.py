# -*- coding: utf-8-*-

import urllib2, json

class WitAiSTT(object):
	def __init__(self, accessToken):
		self.headers = {'Authorization': 'Bearer %s' % accessToken, 'accept': 'application/json', 'Content-Type': 'audio/wav'}

	def transcribe(self, fp):
		data = fp.read()
		req = urllib2.Request('https://api.wit.ai/speech?v=20150101', data, self.headers)
		r = urllib2.urlopen(req)

		text = json.loads(r.read())
		transcribed = [text['_text'].upper()]
		return transcribed