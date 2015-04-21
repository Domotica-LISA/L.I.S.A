# -*- coding: UTF-8 -*-

from ctypes import *

class Blocks(Structure):
	_fields_ = [ ("type", c_uint),
		("signature", c_uint),
		("x", c_uint),
		("y", c_uint),
		("width", c_uint),
		("height", c_uint)]

block = Blocks()