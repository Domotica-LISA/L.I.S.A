import os
import gtts
from pygame import mixer
import time
import requests

class Mp3TTSEngine(object):
	def play_mp3(self, filename):
		mixer.init(16000)
		mixer.music.load(filename)
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue
	def save(self, savefile, text):
		with open(savefile, 'wb') as f:
			for idx, part in enumerate(text):
				payload = { 'ie' : 'UTF-8','tl' : 'nl','q' : part,'total' : len(text),'idx' : idx,'textlen' : len(part) }
				try:
					r = requests.get('http://translate.google.com/translate_tts', params=payload)
					for chunk in r.iter_content(chunk_size=1024):
						f.write(chunk)
				except Exception as e:
					raise
		f.close()

class GoogleTTS(Mp3TTSEngine):
	def say(self, phrase):
		tts = gtts.gTTS(text=phrase, lang='nl')
		#print(phrase)
		self.save("output.mp3", tts.text_parts)
		self.play_mp3("output.mp3")
		#os.remove("output.mp3")