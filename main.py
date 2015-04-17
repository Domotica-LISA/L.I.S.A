# -*- coding: UTF-8 -*-
import sys
from time import clock
from classes import character, path_declarations

sys.path.append(path_declarations.libPath)

if __name__ == '__main__':
	try:
		lisa_fsm = character.Lisa()
		while True:
			startTime = clock()
			timeInterval = 1
			while startTime + timeInterval > clock():
				pass
			lisa_fsm.execute()
	except KeyboardInterrupt:
		print "Bye Bye!"