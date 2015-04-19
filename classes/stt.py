# -*- coding: utf-8-*-

import requests

class WitAiSTT(object):
	def __init__(self, accessToken):
		self.headers = {'Authorization': 'Bearer %s' % accessToken, 'accept': 'application/json', 'Content-Type': 'audio/wav'}

	def transcribe(self, fp):
		data = fp.read()
		r = requests.post('https://api.wit.ai/speech?v=20150101', data=data, headers=self.headers)

		try:
			r.raise_for_status()
			text = r.json()['_text']
		except requests.exceptions.HTTPError:
			print ('Request failed with response: %r' % r.text)
			return []
		except requests.exceptions.RequestException:
			return []
		except ValueError as e:
			print ('Cannot parse response: %s' % e.args[0])
			return []
		except KeyError:
			return []
		else:
			transcribed = [text.upper()]
			return transcribed