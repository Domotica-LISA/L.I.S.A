import os
import gtts

class Mp3TTSEngine():
	def play_mp3(self, filename):
		cmd = ['omxplayer', str(filename)]
		with tempfile.TemporaryFile() as f:
			subprocess.cal(cmd, stdout=f, strerr=f)

class GoogleTTS(Mp3TTSEngine):
	def __init__(self, language='nl'):
		self.language = language

	def say(self, phrase):
		tts = gtts.gTTS(text=phrase, lang=self.language)
		print(phrase)
		tts.save("output.mp3")
		self.play_mp3("output.mp3")
		os.remove("output.mp3")
