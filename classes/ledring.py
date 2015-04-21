# -*- coding: UTF-8 -*-

from neopixel import *

class LedRing:
	def __init__(self):
		self.ring = Adafruit_NeoPixel(8, 18)
		self.ring.begin()

	def set_color(self, color):
		for i in range(8):
			self.ring.setPixelColor(i, Color(color['red'], color['green'], color['blue']))
			self.ring.show()