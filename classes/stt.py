# -*- coding: utf-8-*-

import json
import requests

class WitAiSTT(object):
	def __init__(self, accessToken):
		self.token = accessToken
		self.header = {'Authorization': 'Bearer %s' % self.token, 'accept': 'application/json', 'Content-Type': 'audio/wav'}

	def transcribe(self, fp):
		data = fp.read()
		r = requests.post('https://api.wit.ai/speech?v=20150101', data=data, header=self.header)

		try:
			r.raise_for_status()
			text = r.json()['_text']
		except requests.exceptions.HTTPError:
			return []
		except requests.exceptions.RequestException:
			return []
		except ValueError as e:
			return []
		except KeyError:
			return []
		else:
			transcribed = [text.upper()]
			return transcribed