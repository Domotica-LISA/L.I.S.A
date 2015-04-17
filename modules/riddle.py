# -*- coding: UTF-8 -*-
import re
import time
import random
from classes import path_declarations

WORDS = ["RAADSEL"]

def get_random_joke(filename=path_declarations.data('JOKES.txt')):
	jokeFile = open(filename, "r")
	jokes = []
	start = ""
	end = ""

	for line in jokeFile.readlines():
		line = line.replace("\n", "")

		if start == "":
			start = line
			continue

		if end == "":
			end = line
			continue

		jokes.append((start, end))
		start = ""
		end = ""


def handle(text, speaker, profile):
	joke = get_random_joke()

	def firstline(text):
		speaker.say(joke[0])
		time.sleep(2)

		def answer(text):
			speaker.say(joke[1])

		answer(speaker)
	firstline(speaker)



def is_valid(text):
	return bool(re.search(r'\braadsel\b', text, re.IGNORECASE))
