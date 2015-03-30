import os
import tempfile
import subprocess
import platform
import gtts

class Mp3TTSEngine():
	def play_mp3(self, filename):
		cmd = ['omxplayer', str(filename)]
		with tempfile.TemporaryFile() as f:
			subprocess.call(cmd, stdout=f, strerr=f)
			f.seek(0)
			output = f.read()

class GoogleTTS(Mp3TTSEngine):
	def __init__(self, language='nl'):
		self.language = language

	def say(self, phrase):
		tts = gtts.gTTS(text=phrase, lang='nl')
		print(tts)
		tts.save(phrase + ".mp3")
		self.play_mp3(phrase + ".mp3")
		#os.remove("output.mp3")
