import os
import gtts
from pygame import mixer

class Mp3TTSEngine():
	def play_mp3(self, filename):
		mixer.init(16000)
		mixer.music.load(filename)
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue

class GoogleTTS(Mp3TTSEngine):
	def __init__(self, language='nl'):
		self.language = language

	def say(self, phrase):
		tts = gtts.gTTS(text=phrase, lang='nl')
		print(tts)
		tts.save("output.mp3")
		self.play_mp3("output.mp3")
		os.remove("output.mp3")
