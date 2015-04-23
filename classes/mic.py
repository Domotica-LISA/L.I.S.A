# -*- coding: utf-8-*-

import tempfile
import wave
import audioop
import pyaudio

class Mic:
	def __init__(self, sttEngine):
		self.sttEngine = sttEngine
		self._audio = pyaudio.PyAudio()

	def __del__(self):
		self._audio.terminate()

	def get_score(self, data):
		rms = audioop.rms(data, 2)
		score = rms / 3
		return score

	def fetch_threshold(self):
		thresholdMultiplier = 1.5
		rate = 16000
		chunk = 1024

		thresholdTime = 1

		stream = self._audio.open(
			format=pyaudio.paInt16,
			channels=1,
			rate=rate,
			input=True,
			frames_per_buffer=chunk)

		frames = []

		lastN = [i for i in range(20)]

		for i in range(0, rate / chunk * thresholdTime):
			data = stream.read(chunk)
			frames.append(data)

			lastN.pop(0)
			lastN.append(self.get_score(data))
			average = sum(lastN) / len(lastN)

		stream.stop_stream()
		stream.close()

		threshold = average * thresholdMultiplier

		return threshold

	def active_listen(self):
		rate = 16000
		chunk = 1024
		listenTime = 10

		threshold = self.fetch_threshold()

		stream = self._audio.open(
			format=pyaudio.paInt16,
			channels=1,
			rate=rate,
			input=True,
			frames_per_buffer=chunk)

		frames = []

		lastN = [threshold * 1.2 for i in range(30)]

		for i in range(0, rate / chunk * listenTime):
			data = stream.read(chunk)
			frames.append(data)
			score = self.get_score(data)

			lastN.pop(0)
			lastN.append(score)

			average = sum(lastN) / float(len(lastN))	

		stream.stop_stream()
		stream.close()

		with tempfile.SpooledTemporaryFile(mode='w+b') as f:
			wav_fp = wave.open(f, 'wb')
			wav_fp.setnchannels(1)
			wav_fp.setsampwidth(pyaudio.get_sample_size(pyaudio.paInt16))
			wav_fp.setframerate(rate)
			wav_fp.writeframes(''.join(frames))
			wav_fp.close()
			f.seek(0)
			return self.sttEngine.transcribe(f)
