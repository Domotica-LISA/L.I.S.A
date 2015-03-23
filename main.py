from time import clock
import wit
import classes.character

if __name__ == '__main__':
	try:
		wit.init('cards.pcm.default')
		lisa_fsm = classes.character.Lisa()
		while True:
			startTime = clock()
			timeInterval = 1
			while startTime + timeInterval > clock():
				pass
			lisa_fsm.Execute()
	except KeyboardInterrupt:
		wit.close()
		print "Bye Bye!"