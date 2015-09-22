# -*- coding: UTF-8 -*-
import os
from pygame import mixer
import re
import argparse
import time
import urllib, urllib2

class Mp3TTSEngine(object):
	def play_mp3(self, filename):
		mixer.init(16000)
		mixer.music.load(filename)
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue

	def split_text(self, input_text, max_length=100):
		def split_text_rec(input_text, regexps, max_length=max_length):
			if(len(input_text) <= max_length): return [input_text]
			#mistakenly passed a string instead of a list
			if isinstance(regexps, basestring): regexps = [regexps]
			regexp = regexps.pop(0) if regexps else '(.{%d})' % max_length
			text_list = re.split(regexp, input_text)
			combined_text = []
			#first segment could be >max_length
			combined_text.extend(split_text_rec(text_list.pop(0), regexps, max_length))
			for val in text_list:
				current = combined_text.pop()
				concat = current + val
				if(len(concat) <= max_length):
					combined_text.append(concat)
				else:
					combined_text.append(current)
					#val could be >max_length
					combined_text.extend(split_text_rec(val, regexps, max_length))
			return combined_text
		return split_text_rec(input_text.replace('\n', ''),['([\,|\.|;]+)', '( )'])

	def save(self, savefile, text):
		output = open(savefile, 'wb')
		combined_text = self.split_text(text)
		#print combined_text
		#download chunks and write them to the output file
		for idx, val in enumerate(combined_text):
			mp3url = "http://translate.google.com/translate_tts?tl=nl&q=%s&total=%s&idx=%s&client=t&ie=UTF-8" % (
				urllib.quote(val),
				len(combined_text),
				idx)
			headers = {	"Host": "translate.google.com",
						"User-Agent": 	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) "
										"AppleWebKit/535.19 (KHTML, like Gecko) "
										"Chrome/18.0.1025.163 Safari/535.19"
			}
			req = urllib2.Request(mp3url, '', headers)
			if len(val) > 0:
				try:
					response = urllib2.urlopen(req)
					output.write(response.read())
					time.sleep(.5)
				except urllib2.URLError as e:
					print ('%s' % e)
		output.close()
		#print('Saved MP3 to %s' % output.name)

class TTSEngine(object):
	def play(self, filename):
		cmd = ['aplay', '-D', 'plughw:1,0', str(filename)]
		with tempfile.TemporaryFile() as f:
			subprocess.call(cmd, stdout=f, stderr=f)
			f.seek(0)
			output = f.read()

class GoogleTTS(Mp3TTSEngine):
	def __init__(self):
		pass

	def say(self, phrase):
		#print(phrase)
		self.save("output.mp3", phrase)
		self.play_mp3("output.mp3")
		os.remove("output.mp3")

class FestivalTTS(TTSEngine):
	def __init__(self):
		pass

	def say(self, phrase):
		cmd = ['text2wave']
		with tempfile.NamedTemporaryFile(suffix='.wav') as out_f:
			with tempfile.SpooledTemporaryFile() as in_f:
            	in_f.write(phrase)
            	in_f.seek(0)
            	with tempfile.SpooledTemporaryFile() as err_f:
            		subprocess.call(cmd, stdin=in_f, stdout=out_f, stderr=err_f)
            		err_f.seek(0)
            		output = err_f.read()
            self.play(out_f.name)