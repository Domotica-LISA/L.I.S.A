# -*- coding: utf-8-*-

import tempfile
import wave
import audioop
import alsaaudio

class Mic:
	def __init__(self, sttEngine):
		self.sttEngine = sttEngine
		self._audio = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

	def __del__(self):
		self._audio.terminate()

	def get_score(self, data):
		rms = audioop.max(data, 2)
		score = rms / 3
		return score

	def fetch_threshold(self):
		thresholdMultiplier = 1.8
		rate = 8000
		chunk = 1024

		thresholdTime = 1

		self._audio.setchannels(1)
		self._audio.setrate(rate)
		self._audio.setformat(alsaaudio.PCM_FORMAT_S16_LE)
		self._audio.setperiodsize(160)

		frames = []

		lastN = [i for i in range(20)]

		for i in range(0, rate / chunk * thresholdTime):
			l, data = self._audio.read()
			frames.append(data)

			lastN.pop(0)
			lastN.append(self.get_score(data))
			average = sum(lastN) / len(lastN)

		threshold = average * thresholdMultiplier

		return threshold

	def active_listen(self):
		rate = 8000
		chunk = 1024
		listenTime = 12

		threshold = self.fetch_threshold()

		self._audio.setchannels(1)
		self._audio.setrate(rate)
		self._audio.setformat(alsaaudio.PCM_FORMAT_S16_LE)
		self._audio.setperiodsize(160)

		frames = []

		lastN = [threshold * 1.2 for i in range(30)]

		for i in range(0, rate / chunk * listenTime):
			l, data = self._audio.read()
			frames.append(data)
			score = self.get_score(data)

			lastN.pop(0)
			lastN.append(score)

			average = sum(lastN) / float(len(lastN))

			if average < threshold * 0.8:
				break

		with tempfile.SpooledTemporaryFile(mode='w+b') as f:
			wav_fp = wave.open(f, 'wb')
			wav_fp.setnchannels(1)
			wav_fp.setsampwidth(2)
			wav_fp.setframerate(rate)
			wav_fp.writeframes(''.join(frames))
			wav_fp.close()
			f.seek(0)
			return self.sttEngine.transcribe(f)
