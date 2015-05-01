# -*- coding: UTF-8 -*-
import time
import random
from sys import maxint

WORDS = []

PRIORITY = -(maxint + 1)

def handle(text, speaker, mic, profile):
	print 'hoi werkt dit?'
	defanswer = ('Sorry kan je dat herhalen', 'Dat heb ik niet helemaal begrepen', 'Wat was je vraag precies', 'Ik heb je niet verstaan, wat zei je')
	speaker.say(random.choice(defanswer))
	time.sleep(2)

def is_valid(text):
	return True