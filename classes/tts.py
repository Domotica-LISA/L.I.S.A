import os
import gtts
from pygame import mixer
import time

class Mp3TTSEngine(object):
	def play_mp3(self, filename):
		mixer.init(16000)
		mixer.music.load(filename)
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue

class GoogleTTS(Mp3TTSEngine):
	def say(self, phrase):
		tts = gtts.gTTS(text=phrase, lang='nl')
		#print(phrase)
		print tts.save("output.mp3")
		time.sleep(12)
		self.play_mp3("output.mp3")
		#os.remove("output.mp3")