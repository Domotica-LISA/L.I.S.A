# -*- coding: UTF-8 -*-
import re
import time
import random
from classes import mic, path_declarations

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
	jokes.append((start, end))
    joke = random.choice(jokes)
    return joke


def handle(text, speaker, profile):
	joke = get_random_joke()

	speaker.say(joke[0])
	time.sleep(2)

	def answer(text):
		speaker.say(joke[1])

	answer(mic.Mic.active_listen())

def is_valid(text):
	return bool(re.search(r'\braadsel\b', text, re.IGNORECASE))